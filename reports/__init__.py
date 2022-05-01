"""Top-level package for reports app"""
# reports/__init__.py

__app_name__ = "reports"
__version__ = "0.3.0"

(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    CSV_READ_ERROR,
    REPORT_SAVING_ERROR,
    CONFIG_WRITE_ERROR,
    CONFIG_READ_ERROR,
    SOURCE_PATH_ERROR,
    REPORTS_PATH_ERROR,
    API_TOKEN_ERROR,
) = range(10)

ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config file error",
    CONFIG_WRITE_ERROR: "error while saving config file",
    SOURCE_PATH_ERROR: "source path error",
    REPORTS_PATH_ERROR: "reports path error",
    API_TOKEN_ERROR: "API token error",
}