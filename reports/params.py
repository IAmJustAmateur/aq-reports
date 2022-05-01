from datetime import time
import os

day_start = time(hour=8, minute = 0, second = 0)
day_end = time(hour=20, minute = 0, second = 0)

aq_data_path = os.path.join(os.environ["OneDrive"], "Дюс", "Lichba LLC", "Daikin", "Data")

OFFICE_MONTH_TEMPLATE = "office_month_report_template_with_CH2O.docx"
OFFICE_DAY_TEMPLATE = "office_day_report_template_with_CH2O.docx"
HOME_MONTH_TEMPLATE = "home_month_report_template_with_CH2O.docx"
HOME_DAY_TEMPLATE = "home_day_report_template_with_CH2O.docx"

templates_path = os.path.join(os.environ["Onedrive"], "Дюс", "Lichba LLC", "Daikin", "reports", "templates")
#DOCX_REPORTS_PATH = os.path.join(os.environ["Onedrive"], "Дюс", "Lichba LLC", "Daikin", "reports", "DOCX")
DOCX_OFFICE_REPORTS_PATH = os.path.join("D:\\reports_CH2O", "reports", "Office","DOCX")
DOCX_HOME_REPORTS_PATH = os.path.join("D:\\reports_CH2O", "reports", "HOME","DOCX")
#DOCX_REPORTS_PATH = os.path.join("D:\\reports", "reports", "HOME","DOCX")
#PDF_REPORTS_PATH = os.path.join(os.environ["Onedrive"], "Дюс", "Lichba LLC", "Daikin", "reports", "PDF")

templates_path = os.path.join(os.environ["Onedrive"], "Дюс", "Lichba LLC", "Daikin", "reports", "templates")
#DOCX_REPORTS_PATH = os.path.join(os.environ["Onedrive"], "Дюс", "Lichba LLC", "Daikin", "reports", "DOCX")
DOCX_OFFICE_REPORTS_PATH = os.path.join("D:\\reports_CH2O", "reports", "Office","DOCX")
DOCX_HOME_REPORTS_PATH = os.path.join("D:\\reports_CH2O", "reports", "HOME","DOCX")
#DOCX_REPORTS_PATH = os.path.join("D:\\reports", "reports", "HOME","DOCX")
#PDF_REPORTS_PATH = os.path.join(os.environ["Onedrive"], "Дюс", "Lichba LLC", "Daikin", "reports", "PDF")

