def test_substring(full_string, substring):
    # сообщение об ошибке
    assert str(substring) in str(full_string), f"expected "+  '\''+ substring + '\'' + " to be substring of " + '\''+ full_string + '\''
    return "Match results"