import os
import json
import requests
import virtualenv
from pip._internal import main
import click

@click.group()
def cli():
    pass

# Import existing project with kep.json
@cli.command()
def init():
    click.echo('Initializing kep.json file in working directory')

# Cache dataset to location for retrieval
@cli.command()
@click.argument('location')
@click.argument('name')
def dataset(location, name):
    click.echo('Caching dataset ' + name + ' to ' + location)

# Creating a new project with/without scaffold
@cli.command()
@click.option('--blank', default=True, help='initialize new folder without scaffold')
@click.option('--framework', default=None, help='initialize with framework added as a dependency')
@click.argument('name')
def create(name, blank, framework):
    click.echo("\n🤖 New project named '" + name + "':")

    click.echo("\n✨ Creating folder with kep.json...")
    kep_file = "./project/kep.json"
    os.makedirs(os.path.dirname(kep_file), exist_ok=True)
    with open(kep_file, "w") as f:
        config = {"name": name, "license": "MIT", "start": "source venv/bin/activate"}
        json.dump(config, f)

    click.echo("\n✨ Cloning boilerplate files...")
    url = "https://raw.githubusercontent.com/kirubarajan/keplet/master/scaffold/model.py"
    response = requests.get(url)
    if response.status_code == 200:
        with open("./project/model.py", 'wb') as f:
            f.write(response.content)

    url = "https://raw.githubusercontent.com/kirubarajan/keplet/master/scaffold/data.py"
    response = requests.get(url)
    if response.status_code == 200:
        with open("./project/data.py", 'wb') as f:
            f.write(response.content)
    
    click.echo("\n✨ Creating virtual environment...")
    venv_dir = os.path.dirname("./project/venv/venv")
    virtualenv.create_environment(venv_dir)
    
    click.echo("\n✨ Generating README file...")
    with open("./project/README.md", "w") as f:
        f.write("# " + name + "\n")

    if framework:
        click.echo("\n✨ Adding framework dependency...")
        with open("./project/requirements.txt", "w") as f:
            f.write(framework + "\n")
    
    click.echo("\n🤖 Success! Access your project by running:\n 1. cd " + name + "\n 2. pip install -r requirements.txt\n 3. keplet start")

# Running Flask server on given port
@cli.command()
@click.option('--port', default=5000, help='start server on given port')
@click.argument('name')
def start(name, port):
    click.echo("Running REST API at http://localhost:" + port)

if __name__ == '__main__':
    cli()