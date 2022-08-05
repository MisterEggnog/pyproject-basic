import os
import sys
import shutil

repo_name = '{{cookiecutter.repo_name }}'

def set_python_version():
    python_version = str(sys.version_info.major) + "." + str(sys.version_info.minor)

    file_names = ["Dockerfile", "Pipfile", ".github/workflows/test.yml"]
    for file_name in file_names:
        with open(file_name) as f:
            contents = f.read()
            contents = contents.replace(r"{python_version}", python_version)
        with open(file_name, "w") as f:
            f.write(contents)

def convert_from_yn(arg):
    if arg == "y" or arg == "Y":
        return True
    if arg == "n" or arg == "N":
        return False
    raise RuntimeError("Arg ({arg}) not in format \"yYnN\" this should have been checked before this call.")

def remove_main_if_lib():
    is_lib = '{{ cookiecutter.binary }}'
    main_file_path = os.path.join(repo_name, '__main__.py')
    if not (is_lib == "y" or is_lib == "Y"):
        os.remove(main_file_path)

def remove_docker_files():
    add_docker = '{{ cookiecutter.add_docker }}'
    if not (add_docker == "y" or add_docker == "Y"):
        os.remove('.dockerignore')
        os.remove('Dockerfile')

def remove_precommit_file():
    precommit = convert_from_yn('{{ cookiecutter.precommit }}')
    if not precommit:
	    os.remove('.pre-commit-config.yaml')

def remove_github_action_dir():
    if True:
        shutil.rmtree('.github')

SUCCESS = "\x1b[1;32m"
INFO = "\x1b[1;33m"
TERMINATOR = "\x1b[0m"


def main():
    set_python_version()
    remove_main_if_lib()
    remove_docker_files()
    remove_precommit_file()
    remove_github_action_dir()
    print(SUCCESS + "Project successfully initialized" + TERMINATOR)


if __name__ == "__main__":
    main()
