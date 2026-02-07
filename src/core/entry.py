"""Entry point for the Kesher application."""

import click

from view.monitor import KesherTUI

from .engine import delete as delete_app
from .engine import log as log_app
from .engine import restart as restart_app
from .engine import start as start_app
from .engine import status as status_app
from .engine import stop as stop_app


@click.group()
def cli():
    pass


@click.command()
@click.argument("path", type=str)
@click.option("--name", type=str, default=None, help="Name of the process")
@click.option("--auto-start", is_flag=True, help="Enable auto-start for the process")
def start(path, name, auto_start):
    start_app(path, name, auto_start)


@click.command()
@click.argument("id", type=str)
def stop(id):
    stop_app(id)


@click.command()
@click.argument("id", type=str)
def restart(id):
    restart_app(id)


@click.command()
@click.argument("id", type=str)
def delete(id):
    delete_app(id)


@click.command()
@click.argument("id", type=str)
def status(id):
    status_app(id)


@click.command()
@click.argument("id", type=str)
def log(id):
    log_app(id)


@click.command()
def monitor():
    KesherTUI().run()


cli.add_command(start)
cli.add_command(monitor)
cli.add_command(stop)
cli.add_command(status)
cli.add_command(log)
cli.add_command(restart)
cli.add_command(delete)
