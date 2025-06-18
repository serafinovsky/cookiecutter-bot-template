#!/usr/bin/env python
import os
import shutil
import subprocess


def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        raise


def remove_file_or_dir(path):
    if os.path.isfile(path):
        os.remove(path)
        print(f"Deleted file: {path}")
    elif os.path.isdir(path):
        shutil.rmtree(path)
        print(f"Deleted directory: {path}")
    else:
        print(f"File or directory not found: {path}")


def main():
    need_examples = "{{ cookiecutter.need_examples }}"

    if need_examples == "no":
        for path in [
            "{{cookiecutter.project_slug}}/handlers/examples.py",
            "{{cookiecutter.project_slug}}/templates/start.html"
        ]:
            remove_file_or_dir(path)
    
    try:
        run_command("pip install ruff")
    except subprocess.CalledProcessError:
        run_command("uv pip install ruff")
    run_command("ruff format .")
    run_command("ruff check --preview --fix .")


if __name__ == "__main__":
    main()
