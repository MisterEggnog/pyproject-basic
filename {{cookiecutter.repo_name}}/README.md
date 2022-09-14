# {{cookiecutter.project_name}}

## Setup
```sh
# Install dependencies
pipenv install --dev

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

## Credits
This package was created with Cookiecutter and the [MisterEggnog/pyproject-basic](https://github.com/MisterEggnog/pyproject-basic) project template.
