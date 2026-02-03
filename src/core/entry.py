from py_compile import main
import click
from view.monitor import KesherMenu


@click.group()
def cli():
    pass

@click.command()
@click.argument("path", type=str)
@click.option("-n", "--name", type=str, help="Name of the Kesher instance")
def start(path, name):
    if name:
        click.echo(f"Starting Kesher engine '{name}'... {path}")
    else:
        click.echo(f"Starting Kesher engine... {path}")

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
