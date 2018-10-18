import os
import json
import click
import virtualenv
import requests

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
    click.echo("🤖 New project named '" + name + "':")

    click.echo("✨ Creating folder with kep.json...")
    kep_file = "./" + name + "/kep.json"
    os.makedirs(os.path.dirname(kep_file), exist_ok=True)
    with open(kep_file, "w") as f:
        config = {"name": name, "license": "MIT"}
        json.dump(config, f)

    click.echo("✨ Cloning boilerplate files...")
    url = "https://raw.githubusercontent.com/kirubarajan/keplet/master/scaffold/model.py"
    response = requests.get(url)
    if response.status_code == 200:
        with open("./" + name + "/model.py", 'wb') as f:
            f.write(response.content)

    url = "https://raw.githubusercontent.com/kirubarajan/keplet/master/scaffold/data.py"
    response = requests.get(url)
    if response.status_code == 200:
        with open("./" + name + "/data.py", 'wb') as f:
            f.write(response.content)

    url = "https://raw.githubusercontent.com/kirubarajan/keplet/master/scaffold/server.py"
    response = requests.get(url)
    if response.status_code == 200:
        with open("./" + name + "/server.py", 'wb') as f:
            f.write(response.content)
    
    click.echo("✨ Creating virtual environment...")
    venv_dir = os.path.dirname("./" + name + "/venv/venv")
    virtualenv.create_environment(venv_dir)
    
    click.echo("✨ Generating README file...")
    with open("./" + name + "/README.md", "w") as f:
        f.write("# " + name)

    if framework:
        click.echo("✨ Adding framework dependency...")
        with open("./" + name + "/requirements.txt", "w") as f:
            f.write(framework)
    
    click.echo("\n🤖 Success! Access your project by running: \n 0. cd "+ name + 
        "\n 1. source venv/bin/activate" + 
        "\n 2. pip install -r requirements.txt\n 3. keplet start")

# Running Flask server on given port
@cli.command()
@click.option('--name', default=".", help='use project from given path')
@click.option('--port', default=5000, help='start server on given port')
@click.argument('name')
def start(name, port):
    click.echo("Running REST API at http://localhost:" + port)
    # TODO start Flask server

@cli.command()
def list():
    for project in [f.path[2:] for f in os.scandir('.') if f.is_dir() and 'kep.json' in os.listdir(f.path)]:
        click.echo("💾 " + project)

@cli.command()
def containerize():
    # build Docker image
    pass

if __name__ == '__main__':
    cli()