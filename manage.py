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
@click.option('--blank', default=True, help='whether to initialize with kep.py')
@click.argument('name')
def create(name, blank):
    click.echo("Creating new project named '" + name + "'")

@cli.command()
@click.argument('name')
def start(name):
    click.echo("Running REST API")

if __name__ == '__main__':
    cli()