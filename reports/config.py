import configparser
from genericpath import exists
from pathlib import Path
from typing import Any, Dict, List, NamedTuple

import typer
from reports import (__app_name__, DIR_ERROR, FILE_ERROR, CONFIG_WRITE_ERROR, CONFIG_READ_ERROR, SUCCESS, REPORTS_PATH_ERROR, SOURCE_PATH_ERROR, API_TOKEN_ERROR)

CONFIG_DIR_PATH = Path(typer.get_app_dir(__app_name__))
CONFIG_FILE_PATH = CONFIG_DIR_PATH / "config.ini"

class ConfigParamsReading(NamedTuple):
    params: Dict[str, Any]
    error: int

def init_app() -> int:
    """Initialize the application."""
    config_code = _init_config_file()
    if config_code != SUCCESS:
        return config_code
    return SUCCESS

def set_source_path(source_path: str) -> int:
    return  _set_config_param(param = "Source", value = source_path)

def set_reports_path(reports_path: str) -> int:
    return  _set_config_param(param = "Reports", value = reports_path)

def set_token(api_token: str) -> int:
    return  _set_config_param(param = "api token", value = api_token)

def set_time_zone(tz: str) -> int:
    return  _set_config_param(param = "timezone", value = tz)

def _set_config_param(param: str, value: str) -> int:
    config_parser = configparser.ConfigParser()
    try:
        config_parser.read(CONFIG_FILE_PATH)
    except OSError:
        return CONFIG_READ_ERROR

    config_parser[param] = {param: value}
    try:
        with CONFIG_FILE_PATH.open("w") as file:
            config_parser.write(file)
    except OSError:
        return CONFIG_WRITE_ERROR
    return SUCCESS


def _init_config_file() -> int:
    try:
        CONFIG_DIR_PATH.mkdir(exist_ok=True)
    except OSError:
        return DIR_ERROR
    try:
        CONFIG_FILE_PATH.touch(exist_ok=True)
    except OSError:
        return FILE_ERROR
    return SUCCESS

def get_params() -> ConfigParamsReading:
    report_params = {}
    config_parser = configparser.ConfigParser()
    config_parser.read(CONFIG_FILE_PATH)
    
    try:
        report_params["source_path"] =  Path(config_parser["Source"]["source"])
    except:
        return ConfigParamsReading(report_params, SOURCE_PATH_ERROR)

    try:
        report_params["reports_path"] =  Path(config_parser["Reports"]["reports"])
    except:
        return ConfigParamsReading(report_params,REPORTS_PATH_ERROR)

    try:
        report_params["api_key"] = config_parser["api token"]["api token"]
    except:
        return ConfigParamsReading(report_params, API_TOKEN_ERROR)
    
    try:
        report_params["timezone"] = config_parser["timezone"]["timezone"]
    except:
        pass

    if not report_params["source_path"].exists():
        return ConfigParamsReading(report_params, SOURCE_PATH_ERROR)
    if not report_params["reports_path"].exists():
        return ConfigParamsReading(report_params,REPORTS_PATH_ERROR)
    
    return ConfigParamsReading(report_params, SUCCESS)