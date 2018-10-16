# Keplet CLI
A command line tool for managing machine learning projects and their associated resources. Keplet allows you to create new machine learning projects that scaffold commonly needed structure. For example, running

`keplet create chatbot --pytorch` 

will create a virtual environment (with PyTorch pre-installed) and scaffold the following structure:

    .
    ├── build/                   # Compiled files (alternatively `dist`)
    ├── docs/                    # Documentation files (alternatively `doc`)
    ├── data.py                  # Data loader from either Keplet cache or by path
    ├── model.py                 # Model class with interface to make predictions
    ├── venv/                    # Virtual environment location
    ├── requirements.txt         # Dependency tracker
    ├── kep.py                   # Model/dataset definition and  misc. metadata
    └── README.md                # Boilerplate README.md with file instructions

Running `keplet start` will then launch a REST API listening at `localhost:5000` that
returns an HTTP respose by POST to the `/predict` route. 

## Features
- Virtual environments provisioner for environment variables and dependencies
- Dataset location cache for use across multiple projects
- File directory usage for project management
- Command line documentation
- Automatic REST API creation for model predictions over HTTP (Flask integration)

## Usage
```
Usage: manage.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Learn more about the standard Keplet commands.

Commands:
  init
  create
  start
  train
  predict
  readme
  dataset
```