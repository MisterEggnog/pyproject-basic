
def _assert_main_exists(result):
	main_file = result.project_path / result.project_path.name / "__main__.py"
	return main_file.is_file()

def test_includes_main_by_default(cookies):
	result = cookies.bake()
	assert _assert_main_exists(result)

def test_no_main_when_passed_n(cookies):
	result = cookies.bake(extra_context={"binary":"n"})
	assert not _assert_main_exists(result)
	result = cookies.bake(extra_context={"binary":"N"})
