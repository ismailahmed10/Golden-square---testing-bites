from lib.check_codeword import check_codeword

def test_checks_if_codeword_is_correct():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_if_codeword_is_wrong():
    result = check_codeword("water")
    assert result == "WRONG!"

def test_if_codeword_is_close():
    result = check_codeword("house")
    assert result == "Close, but nope."

def test_if_codeword_is__quite_close():
    result = check_codeword("mouse")
    assert result == "WRONG!"

def test_if_codeword_is_quite_close_2nd():
    result = check_codeword("hat")
    assert result == "WRONG!"