import re
import sys

MODULE_REGEX = r"^[a-zA-Z][_a-zA-Z0-9]+$"
module_name = "{{ cookiecutter.repo_name }}"

if not re.match(MODULE_REGEX, module_name):
    print("ERROR: %s is not a valid Python module name!" % module_name)
    sys.exit(1)

def valid_yn_form(arg):
    return arg in {"n", "N", "y", "Y"}

yn_args = ["{{ cookiecutter.binary }}", "{{ cookiecutter.add_docker }}"]
for yn in yn_args:
    if not valid_yn_form(yn):
        print("ERROR: % is not a valid Y/N argument." % yn)
        sys.exit(1)
