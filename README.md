# Keplet CLI
Keplet is a non-intrusive CLI for developing and interacting with machine learning projects by scafolding common architectures and abstracting model management (e.g. dependencies, documentation, containerization). Keplet supports any model architecture and is compatible with any framework, making it easier to publish reproducable models and deploy pre-trained instances.

## Features
- Virtual environments provisioner for environment variables and dependencies
- Dataset directory cache for use across multiple projects
- File directory usage for project management
- Command line documentation (by using the `--help` flag)
- Automatic REST API creation for model predictions over HTTP

## Example
Creating new project: `keplet create chatbot --framework torch`

```
🤖 New project named 'chatbot':
✨ Creating folder with kep.json...
✨ Cloning boilerplate files...
✨ Creating virtual environment...
✨ Generating README file...
✨ Installing PyTorch...

🤖 Success! Access your project by running:
 1. cd chatbot
 2. pip install -r requirements.txt
 3. keplet start
```

Resulting project architecture (with PyTorch-enabled virtual environment):

    chatbot/
    ├── /venv                    # virtual environment location
    ├── kep.json                 # Model/dataset definition and  misc. metadata
    ├── data.py                  # Data loader from either Keplet cache or by path
    ├── model.py                 # Model class with interface to make predictions
    ├── server.py                # REST API dynamically generated from kep.py config
    ├── requirements.txt         # Dependency tracker for use with pip/anaconda
    └── README.md                # Boilerplate README.md with file instructions

Additionally, running `keplet start` will launch a Flask server in `server.py`. By default, the server listens at `localhost:5000/predict` and returns JSON-encoded predictions over HTTP.

## Usage
After installing Keplet using `pip install keplet`:

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
