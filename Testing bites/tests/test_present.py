import pytest
from lib.present import Present

def test_if_contents_have_been_wrapped():
    wrapped_contents = Present()
    wrapped_contents.wrap("naruto")  # First wrap is fine
    with pytest.raises(Exception) as err:
        wrapped_contents.wrap("saskue")  # Second wrap should fail
    error_message = str(err.value)
    assert error_message == "A contents has already been wrapped."

def test_if_no_contents_are_not_wrapped():
    non_wrapped_contents = Present()
    with pytest.raises(Exception) as err:
        non_wrapped_contents.unwrap()  # <-- Don't forget parentheses!
    error_message1 = str(err.value)
    assert error_message1 == "No contents have been wrapped."
