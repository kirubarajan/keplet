import click

@click.group()
def cli():
    pass

@cli.command()
def init():
    click.echo('Initializing kep.py file in working directory')

@cli.command()
@click.argument('location')
@click.argument('name')
def dataset(location, name):
    click.echo('Caching dataset location')

@cli.command()
@click.option('--blank', default=True, help='initialize new folder without scaffold')
@click.option('--pytorch', default=True, help='initialize new foler with pytorch installed')
@click.option('--tensorflow', default=True, help='initialize new foler with tensorflow installed')
@click.argument('name')
def create(name, blank, pytorch, tensorflow):
    click.echo("Creating new project named '" + name + "'")

@cli.command()
@click.argument('name')
def start(name):
    click.echo("Running REST API")

if __name__ == '__main__':
    cli()