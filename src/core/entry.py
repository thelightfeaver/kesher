import click

from view.monitor import KesherMenu

from .engine import start as start_app


@click.group()
def cli():
    pass


@click.command()
@click.argument("path", type=str)
def start(path):
    start_app(path)


@click.command()
@click.argument("id", type=str)
def stop(id):
    click.echo(f"Stopping Kesher engine with ID: {id}")


@click.command()
@click.argument("id", type=str)
def status(id):
    click.echo(f"Status of Kesher engine with ID: {id}")


@click.command()
def monitor():
    KesherMenu().run()


cli.add_command(start)
cli.add_command(monitor)
cli.add_command(stop)
cli.add_command(status)
