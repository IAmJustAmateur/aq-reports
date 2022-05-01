import os
import docx2pdf
from pathlib import Path
import datetime

#from sympy import source
DOCX_OFFICE_DAYS_REPORTS_PATH = os.path.join("D:\\reports_CH2O", "reports", "Office","DOCX", "DAYS", "US-Home")
PDF_OFFICE_DAYS_REPORTS_PATH = os.path.join("D:\\reports_CH2O", "reports", "Office","PDF", "DAYS", "US-Home")
PDF_OFFICE_REPORTS_PATH = os.path.join("D:\\reports", "reports", "Office","PDF")

DOCX_OFFICE_OFFICE_DAYS_REPORTS_PATH = os.path.join("D:\\reports_CH2O", "reports", "Office","DOCX", "DAYS", "US-Office")

DOCX_HOME_REPORTS_PATH = os.path.join("D:\\reports_CH2O", "reports", "Home","DOCX")
PDF_HOME_REPORTS_PATH = os.path.join("D:\\reports", "reports", "Home","PDF")

REPORTS_PATH = os.path.join("D:\\reports_CH2O", "reports")
OFFICE_REPORTS_PATH = os.path.join(REPORTS_PATH, "OFFICE")
DOCX_OFFICE_REPORTS_PATH = os.path.join(OFFICE_REPORTS_PATH, "DOCX")
DAYS_DOCX_OFFICE_REPORTS_PATH = os.path.join(DOCX_OFFICE_REPORTS_PATH, "DAYS")
JPHOME_DAYS_DOCX_OFFICE_REPORTS_PATH = os.path.join(DAYS_DOCX_OFFICE_REPORTS_PATH, "JP-HOME")
YEARS = ["2021", "2022"]

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

def export_reports(startpath):
    fcounter = 0
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        
        for f in files:
            fcounter+=1

            print('{}{}--{}'.format(subindent, f, fcounter))
            f_docx_path = os.path.join(root, f)
            f_pdf = f.replace("docx", "pdf")
            f_root = root.replace("DOCX", "PDF")
            f_pdf_path = os.path.join(f_root, f_pdf)
            Path(f_root).mkdir(parents=True, exist_ok=True)
            if not os.path.isfile(f_pdf_path):
                print(f'{f_pdf_path} - { datetime.datetime.now().strftime("%H:%M:%S")}')
                try:
                    docx2pdf.convert(f_docx_path, f_pdf_path)
                except:
                    print(f' error in {f_docx_path}')
            else:
                print (f'{f_pdf_path} allready exists')

def export_days (device_list: list, start_path):
    for device in device_list:
        device_path = os.path.join(start_path, device)
        for year in YEARS:
            year_path = os.path.join(device_path, year)
            months = [str(month_number) for month_number in range (1,13)]
            for month in months:
                month_path = os.path.join(year_path, month)
                if os.path.exists(month_path):
                    
                    dest_path = month_path.replace("DOCX", "PDF")
                    Path(dest_path).mkdir(parents=True, exist_ok=True)
                    source_path = month_path + "/"
                    dest_path = dest_path + "/"
                    
                    docx2pdf.convert(source_path, dest_path)



def export_day_folders(start_path):
    folders =  [d for d in os.listdir(start_path) if os.path.isdir(os.path.join( start_path, d))]
    for folder in folders:
        folder_path = os.path.join(start_path, folder)
        device_list = [f for f in os.listdir(folder_path)]
        export_days(device_list, folder_path)

def export_month_folders(start_path):
    folders =  [d for d in os.listdir(start_path) if os.path.isdir(os.path.join( start_path, d))]
    for folder in folders:
        folder_path = os.path.join(start_path, folder)
        device_list = [f for f in os.listdir(folder_path)]
        export_months(device_list, folder_path)

    
def export_months(device_list: list, start_path: str):
    for device in device_list:
        device_path = os.path.join(start_path, device)
        for year in YEARS:
            year_path = os.path.join(device_path, year)
            if os.path.exists(year_path):
                dest_path = year_path.replace("DOCX", "PDF")
                Path(dest_path).mkdir(parents=True, exist_ok=True)
                dest_path = dest_path + "/"
                source_path = year_path + "/"
                docx2pdf.convert(source_path, dest_path)   

if __name__=='__main__':
    #JPHOME_MONTHS_DOCX_OFFICE_REPORTS_PATH = JPHOME_DAYS_DOCX_OFFICE_REPORTS_PATH.replace("DAYS", "MONTHS")
    #jp_home_devices = [f for f in os.listdir(JPHOME_MONTHS_DOCX_OFFICE_REPORTS_PATH)]
    #print(jp_home_devices)
    #export_months(jp_home_devices, JPHOME_MONTHS_DOCX_OFFICE_REPORTS_PATH)
    start_path = os.path.join( DOCX_HOME_REPORTS_PATH, "MONTHS")
    export_month_folders(start_path)
    #export_day_folders(start_path)

