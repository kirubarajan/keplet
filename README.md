# Keplet CLI
Keplet is a non-intrusive CLI for developing and interacting with machine learning projects by scafolding common architectures and abstracting model management (e.g. dependencies, documentation, containerization). Keplet supports any model architecture and is compatible with any framework, making it easier to publish reproducable models and deploy pre-trained instances.

## Example
Running: `keplet create chatbot --framework torch` will create a virtual environment (with PyTorch pre-installed) and scaffold:

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
  create
  start
  train
  predict
  readme
  dataset
```

## License
MIT
