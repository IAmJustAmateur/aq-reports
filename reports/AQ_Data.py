import pytz
import pandas as pd
from datetime import datetime, date, time
import os
from reports.utils import last_day_of_month
from reports.params import aq_data_path, day_start, day_end
import configparser
from reports.config import CONFIG_DIR_PATH, CONFIG_FILE_PATH
from pathlib import Path
from reports import (SOURCE_PATH_ERROR, REPORTS_PATH_ERROR, API_TOKEN_ERROR)

class AQ_Data():
    '''
    Prepare Environmental data from csv file to create reports

    '''
    def __init__(self, aq_folder: str, aq_file: str, tz: pytz.timezone):
        '''
        read data from aq_folder, aq_file and parsing based on time zone tz
        split by months
        '''
        self.tz = tz
        self.read_data(aq_folder, aq_file)
        self.aq_data_process() 
        self.split_by_periods(period='M')
        self.aq_months = []
        for aq_month in self.aq_periods:
            if not aq_month.empty:
                self.aq_months.append(aq_month)
        self.months = list(get_months(self.aq_months))

    def is_day(self, aq_data)->bool:
        return (aq_data["time"] >= day_start) & (aq_data["time"] <= day_end)

    def is_night(self, aq_data)->bool:
        return (aq_data["time"] <=day_start) | (aq_data["time"] >= day_end)

    def select_data_for_period(self, start_date: date, end_date: date) -> pd.DataFrame:
        '''
        select data for specific period
        '''
        period_data = self.aq_data[(self.aq_data["date_day"] >= start_date) &  (self.aq_data["date_day"] <= end_date)]
        return period_data

    def read_data(self, folder: str, file: str):
        '''
        read aq data from csv
        '''
        file_path = os.path.join(aq_data_path, folder, file)
        self.aq_data = pd.read_csv(file_path)
        self.aq_data.fillna(0, inplace=True)

    def get_day_data_by_hours(self, year, month, day):
        aq_data = self.get_date_data(year = year, month = month, day = day)
        day_data = aq_data[self.is_day(aq_data)]
        return day_data

    def get_night_data_by_hours(self, year, month, day):
        aq_data = self.get_date_data(year = year, month = month, day = day)
        night_data = aq_data[self.is_night(aq_data)]
        return night_data   
        
    def get_month_data(self, year: int, month: int) -> pd.DataFrame:
        '''
        get aq data for specific month
        
        '''
        start_date = date(year = year, month = month, day = 1)
        end_date = last_day_of_month(start_date)
        month_data = self.select_data_for_period(start_date, end_date)
        return month_data

    def get_date_data(self, day: int, month: int, year: int)  -> pd.DataFrame:
        '''
        get aq data for specific date
        
        '''
        current_date = date(year = year, month = month, day = day)
        aq_data = self.aq_data[(self.aq_data["date_day"] == current_date)]
        return aq_data

    def get_day_data(self, day: int, month: int, year: int)  -> pd.DataFrame:
        '''
        get aq data for specific day
        
        '''
        aq_date_data = self.get_date_data(day, month, year)
        aq_day_data = aq_date_data[self.is_day(aq_date_data)]

        return aq_day_data

    def get_night_data(self, day: int, month: int, year: int)  -> pd.DataFrame:
        '''
        get aq data for specific night
        
        '''
        aq_date_data = self.get_date_data(day, month, year)
        aq_night_data = aq_date_data[self.is_night(aq_date_data)]

        return aq_night_data

    def get_month_days_data(self, month, year) -> pd.DataFrame:
        aq_data = self.get_month_data(month = month, year =  year)
        aq_data = aq_data[self.is_day(aq_data)]
        return aq_data

    def get_month_nights_data(self, month, year)  -> pd.DataFrame:
        aq_data = self.get_month_data(month = month, year=year)
        aq_data = aq_data[self.is_night(aq_data)]
        return aq_data

    def mean_by_date(self, aq_data)-> pd.DataFrame:
        '''
        average values for a specific day
        '''
        aq_data.drop("hour", axis = 1, inplace = True)
        aq_data.drop("time", axis = 1, inplace = True)
        aq_data = aq_data.groupby(['date_day']).mean()
        aq_data = aq_data.reset_index(level = "date_day")
        return aq_data

    def get_month_by_days(self, month, year) -> pd.DataFrame:
        aq_data = self.get_month_days_data(month, year)
        aq_data = self.mean_by_date(aq_data)
        return aq_data

    def get_month_by_nights(self, month, year) -> pd.DataFrame:
        aq_data = self.get_month_nights_data(month, year)
        aq_data = self.mean_by_date(aq_data)
        return aq_data
                
    def aq_data_process(self):
        '''
        set timezone
        Calculation of average values for each hour
        '''
        self.aq_data["date"] = self.aq_data["date"].apply(lambda t: datetime.fromtimestamp(t, tz=self.tz))
        self.split_date_time()
        self.aq_data = self.aq_data.groupby(['date_day', 'hour']).mean()
        self.aq_data = self.aq_data.reset_index(level = "date_day")
        self.aq_data = self.aq_data.reset_index(level = "hour")
        self.aq_data["date"] = self.aq_data.apply(lambda row: datetime.combine(row["date_day"], time(row["hour"],0,0)),axis=1)
        self.aq_data["time"] = self.aq_data["hour"].apply(lambda h: time(h,0,0))
                    
    def split_by_periods(self, period: str):
        g = self.aq_data.groupby(pd.Grouper(key='date', freq=period))
        self.aq_periods = [group for _,group in g]

    def split_date_time(self):
        '''
        split date into date and time
        '''
        self.aq_data["time"] = self.aq_data["date"].apply(datetime.time)
        self.aq_data["date_day"] = self.aq_data["date"].apply(datetime.date)
        self.aq_data["hour"] = self.aq_data["time"].apply(lambda t: t.hour)

    def get_month_dates(self, year, month) -> list:
        aq_data = self.get_month_days_data(year = year, month = month)
        dates = aq_data["date_day"].unique().tolist()
        days = [d.day for d in dates]
        return days
   
def get_data_files() -> tuple([[], []]):
    aq_folders = os.listdir(aq_data_path)
    aq_files = {}
    for aq_folder in aq_folders:
        aq_folder_path = os.path.join(aq_data_path, aq_folder)
        folder_files = [f for f in os.listdir(aq_folder_path) if f[-4:]=='.csv']
        aq_files[aq_folder] = folder_files
    return aq_files, aq_folders


def get_months(aq_months: list) -> list:
    dates = map( lambda aq_month: aq_month["date_day"].iloc[0], aq_months)
    months = map (lambda d: (d.month, d.year), dates)
    return months

def get_days(aq_days: pd.DataFrame) -> pd.DataFrame:
    days = aq_days.groupby(['date_day']).mean()
    days.reset_index(inplace = True)
    return days

def get_hours(aq_periods: pd.DataFrame) -> list:
    hours = aq_periods['hour'].tolist()
    return hours