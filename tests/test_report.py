from reports.AQ_Data import AQ_Data
from reports.params import templates_path, OFFICE_DAY_TEMPLATE, aq_data_path
import pytz
from reports.params import day_start, day_end
from reports.Reports import OfficeDayReport, OfficeMonthReport, HomeDayReport, HomeMonthReport
from reports.cli import (init, source, dest, token, time_zone, report)
from pathlib import Path
from reports import __app_name__
import typer
import os
import configparser
from reports.config import CONFIG_DIR_PATH, CONFIG_FILE_PATH

""" def test_month_night_data():
    tz = pytz.timezone("US/Pacific")
    folder = "JP-home(Oct16toJan15)"
    file = "j0153.csv"
    aq = AQ_Data(folder, file, tz)
    aq_10 = aq.get_month_nights_data(year = 2021, month = 10)
    for i in range(len(aq_10)):
        assert (aq_10.iloc[i]["time"] <= day_start) | (aq_10.iloc[i]["time"] >= day_end)

def test_month_day_data():
    tz = pytz.timezone("US/Pacific")
    folder = "JP-home(Oct16toJan15)"
    file = "j0153.csv"
    aq = AQ_Data(folder, file, tz)
    aq_10 = aq.get_month_days_data(year = 2021, month = 10)
    for i in range(len(aq_10)):
        assert (aq_10.iloc[i]["time"] >= day_start) & (aq_10.iloc[i]["time"] <= day_end)
 """
""" 
def testDayReport():
    tz = pytz.timezone("US/Pacific")
    folder = "JP-home(Oct16toJan15)"
    file = "j0153.csv"
    aq_data = AQ_Data(folder, file, tz)
    r = HomeDayReport( 10,  2021, 17, "j0153", aq_data)
    r.fill_report()
"""
""" 
        r = HomeMonthReport( 10,  2021,  "j0153", aq_data)
    r.fill_report()
    r = OfficeDayReport( 10,  2021, 17, "j0153", aq_data)
    r.fill_report()
    r = OfficeMonthReport( 10,  2021,  "j0153", aq_data)
    r.fill_report() 
"""
""" def test_init():
    init()
    assert os.path.exists( Path(typer.get_app_dir(__app_name__))) == True

def test_source():
    aq_data_path = Path(os.environ["OneDrive"], "Дюс", "Lichba LLC", "Daikin", "Data")
    source(aq_data_path)
        
    config_parser = configparser.ConfigParser()
    config_parser.read(CONFIG_FILE_PATH)
    source_path =  Path(config_parser["Source"]["source"])

    assert source_path == aq_data_path

def test_dest():
    aq_reports_path = Path("D:\\", "reports")
    dest(aq_reports_path)
        
    config_parser = configparser.ConfigParser()
    config_parser.read(CONFIG_FILE_PATH)
    dest_path =  Path(config_parser["Reports"]["reports"])

    assert dest_path == aq_reports_path
"""
""" 
def test_token():
    api_token = "623d80b709d4bd0023a37070"
    token (api_token)
    config_parser = configparser.ConfigParser()
    config_parser.read(CONFIG_FILE_PATH)
    api_key = config_parser["api token"]["api token"]
    
    assert api_key == api_token
"""
""" 
def test_timezone():
    tz = 'US/Pacific'
    time_zone (tz)

    config_parser = configparser.ConfigParser()
    config_parser.read(CONFIG_FILE_PATH)
    timezone = config_parser["timezone"]["timezone"]
    assert tz == timezone
 """
def test_report():
    report("office", "months")
