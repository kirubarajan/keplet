# Keplet CLI
A command line tool for managing machine learning projects and their associated resources. Keplet allows you to create new machine learning projects that scaffold commonly needed structure. As a result, publishing reproducable models and deploying pre-trained models

For example, running: `keplet create chatbot --framework torch` will create a virtual environment (with PyTorch pre-installed) and scaffold:

    chatbot/
    ├── kep.json                 # Model/dataset definition and  misc. metadata
    ├── data.py                  # Data loader from either Keplet cache or by path
    ├── model.py                 # Model class with interface to make predictions
    ├── server.py                # REST API dynamically generated from kep.py config
    ├── requirements.txt         # Dependency tracker for use with pip/anaconda
    └── README.md                # Boilerplate README.md with file instructions

Additionally, running `keplet start` will launch a Flask server in `server.py`. By default, the server listens at `localhost:5000/predict` and returns JSON-encoded predictions over HTTP.

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
  list
  create
  start
  train
  predict
  run
```

Where `run` can execute scripts defined in `kep.json`. 

## License
MIT