# ai-stack
General template for AI

# Install the dependencies

### Clone the repo
```bash
git clone git@github.com:kittipatkampa/ai-stack.git
cd ai-stack
```

### Install python using `pyenv`
You need to have `pyenv` first before using the commands below.
```
pyenv local 3.12.2

# If python 3.12.2 doesn't exist, just install it via pyenv
pyenv install 3.12.2
```

Verify that the correct Python version is being used:

```bash
pyenv versions
```

### Install python dependencies using `poetry`
Install (poetry)[https://python-poetry.org/docs/#installation], if you don't have it.
Then you can use the command below to install from the dependency file `pyproject.toml`.
```
poetry install
```

### Store your credentials
We will store credentials in 2 places:
1. For development streamlit app, we store at `.streamlit/secrets.toml` file.
2. For production, we store at `.env` file. Under your root folder, create an empty `.env` file and add your credentials there. Please refer to `.env.example` for the format. For example:
```
ANTHROPIC_API_KEY = ""
OPENAI_API_KEY = "sk-XXXX"
AWS_ACCESS_KEY_ID = "XXXX"
AWS_SECRET_ACCESS_KEY = "XXXX"
```
Whatever you added there can be used in `common/settings.py`


