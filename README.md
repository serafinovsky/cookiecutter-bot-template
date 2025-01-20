# CookieCutter Template: Bot Project Generator

This is a `cookiecutter` template designed to help you quickly generate a simple bot project with a predefined structure, configuration files, and optional example files. The template uses **Django** for managing database migrations and the admin panel, and **python-telegram-bot** for building the Telegram bot.
## Prerequisites

Before using this template, ensure you have the following installed:

* Python 3.11+
* Cookiecutter: Install it using pip:

```bash
pip install cookiecutter ruff
```

## Usage
To generate a new bot project using this template, follow these steps:

### Run the Template
Execute the following command in your terminal:

```bash
cookiecutter https://github.com/serafinovsky/cookiecutter-bot-template.git
```

### Project Generation
After providing the required inputs, the template will generate a new bot project with the specified structure and files.

### Navigate to the Project
Change into the newly created project directory:

```bash
cd {{cookiecutter.project_slug}}
```

### Install Dependencies and Run the Bot
Follow the instructions in the generated project's README.md to run and develop your bot.