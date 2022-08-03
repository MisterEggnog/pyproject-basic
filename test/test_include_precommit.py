
def _includes_precommit_file(result):
	return result.project_path / ".pre-commit-config.yaml"

def test_default_include_file(cookies):
	result = cookies.bake()
	assert _includes_precommit_file(result).is_file()

def test_arg_not_include_file(cookies):
	for i in ["n", "N"]:
		result = cookies.bake({"precommit":i})
		assert not _includes_precommit_file(result).is_file()
