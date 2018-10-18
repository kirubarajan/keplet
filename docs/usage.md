# Usage
A list of Keplet's command line functionality. Instructions page is a work in progress during development.

## `create`
Start a new Keplet project by creating a directory with a given name and initializing a config file named `kep.json`
containing the project metadata.

### Flags
- `--framework` (specify pip library to install and add to README)

### Example
**Execute**: 

`keplet create chatbot --framework torch`

**Output**:

```
🤖 New project named 'chatbot':
✨ Creating folder with kep.json...
✨ Cloning boilerplate files...
✨ Creating virtual environment...
✨ Generating README file...
✨ Installing torch...

🤖 Success! Access your project by running:
 0. cd chatbot
 1. source venv/bin/activate
 2. pip install -r requirements.txt
 3. keplet start
```

## `list`
**Execute**: 

`keplet list`

**Output**:

```
🤖 project1
🤖 project2
🤖 project3
```