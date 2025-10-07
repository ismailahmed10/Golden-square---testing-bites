from lib.gratitudes import Gratitudes 

def test_initial_format_is_empty():
    g = Gratitudes()
    assert g.format() == "Be grateful for: "
    #"Should return base message when no gratitudes are added"

def test_add_single_gratitude():
    g = Gratitudes()
    g.add("my family")
    assert g.format() == "Be grateful for: my family"
    # "Should return one gratitude"

def test_add_multiple_gratitudes():
    g = Gratitudes()
    g.add("my friends")
    g.add("good health")
    g.add("opportunities")
    expected = "Be grateful for: my friends, good health, opportunities"
    assert g.format() == expected
    # "Should return all gratitudes comma-separated"

def test_add_empty_string():
    g = Gratitudes()
    g.add("")
    assert g.format() == "Be grateful for: "
    # "Empty string should still result in correct format"
