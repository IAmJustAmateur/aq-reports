from turtle import bgcolor
import typer
import logging

from pathlib import Path

app = typer.Typer()
log = logging.getLogger("cli_app")
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(levelname)s %(message)s',
                filename='cli.log', filemode='w')


from typing import List, Optional

from reports import (
    ERRORS, SUCCESS, __app_name__, __version__, config
)
import pytz

@app.command()
def init() -> None:
    """Initialize  app"""
    app_init_error = config.init_app()
    if app_init_error:
        typer.secho(
            f'Creating config file failed with "{ERRORS[app_init_error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)

@app.command()
def source(
    source_path: Path = typer.Argument(..., help="path for source data"),
) -> None:
    """Set source path."""
    if not source_path.is_dir():
        typer.secho(f'path {source_path} does not exist', fg = typer.colors.RED, bg = typer.colors.WHITE)
        raise typer.Exit(1)
    error = config.set_source_path(source_path)
    if error:
        typer.secho(
            f'Saving config file failed with "{ERRORS[error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    typer.secho(f'path for source files set {source_path}', fg = typer.colors.BLUE)

@app.command()
def dest(
    reports_path: Path = typer.Argument(..., help="destination path for reports"),
) -> None:
    """Set path for reports."""
    if not reports_path.is_dir():
        typer.secho(f'path {reports_path} does not exist', fg = typer.colors.RED, bg = typer.colors.WHITE)
        raise typer.Exit(1)
    error = config.set_reports_path(reports_path)
    if error:
        typer.secho(
            f'Saving config file failed with "{ERRORS[error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    typer.secho(f'path for reports files set {reports_path}', fg = typer.colors.BLUE)

@app.command()
def token(
    api_token: str = typer.Argument(..., help="api token"),
) -> None:
    """Set path for reports."""
    error = config.set_token(api_token)
    if error:
        typer.secho(
            f'Saving config file failed with "{ERRORS[error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    typer.secho('api token was saved', fg = typer.colors.BLUE)

@app.command()
def time_zone(
    tz: str = typer.Argument(..., help="time zone"),
) -> None:
    """
    Set time zone
    """
    if not tz in list (pytz.all_timezones_set):
        typer.secho(
            f'can not set such timezone: {tz}',
            fg=typer.colors.RED,
        )
        return
    error = config.set_time_zone(tz)
    if error:
        typer.secho(
            f'Saving config file failed with "{ERRORS[error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    typer.secho(f'time zone was set')

@app.command()
def report(report_type: str = typer.Argument(..., help="report type: 'office' or 'home'"), 
           report_period: str= typer.Argument(..., help="report period: 'months' or 'days'")) -> None:
    """
    Create reports: home or office, days or months
    """
    typer.secho(f'report type is {report_type}, report periods are {report_period} ')
    params_read = config.get_params()
    if params_read.error != SUCCESS:
       
        log.debug(f"Some error while reading params: {ERRORS[params_read.error]}")
        typer.secho(f'error is {ERRORS[params_read.error]}')
