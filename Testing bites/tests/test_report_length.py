from lib.report_length import report_length

def test_the_length_of_a_string():
    result = report_length('hello')
    assert f"This string was {5} characters long."

