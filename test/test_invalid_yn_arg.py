
def test_fails_with_giberish(cookies):
	result = cookies.bake(extra_context={"add_docker":"sfdfdsf"})
	assert result.exit_code != 0
