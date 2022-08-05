
import re
from functools import reduce

def _includes_precommit_file(result):
	return result.project_path / ".pre-commit-config.yaml"

def test_default_include_file(cookies):
	result = cookies.bake()
	assert _includes_precommit_file(result).is_file()

def test_arg_not_include_file(cookies):
	for i in ["n", "N"]:
		result = cookies.bake({"precommit":i})
		assert not _includes_precommit_file(result).is_file()

def test_no_precommit_dependecy(cookies):
	result = cookies.bake()
	rexp = re.compile(r'^pre-commit = "\*"$')
	pipfile = open(result.project_path / "Pipfile")
	pip_lines = pipfile.readlines()
	pip_result = map(lambda l: l.strip(), pip_lines)
	pip_result = map(lambda l: rexp.match(l), pip_result)
	pip_result = map(lambda l: l is not None, pip_result)
	pip_result = any(pip_result)
	pipfile.close()
	assert pip_result
