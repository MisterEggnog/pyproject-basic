
def test_includes_main_by_default(cookies):
	result = cookies.bake()
	assert result.project_path.name == "best_practices"
	main_file = result.project_path / result.project_path.name / "__main__.py"
	assert main_file.is_file()

