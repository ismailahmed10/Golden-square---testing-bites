from lib.string_builder import StringBuilder

def test_building_a_string():
    string = StringBuilder()
    string.add("Hello")
    string.size == 5
    assert string.output

# Below is how you should build a test step-by-step and above is how you did it but it should be done like it is below


from lib.string_builder import StringBuilder  # Adjust path if needed

def test_string_builder_behaviour():
    string_builder = StringBuilder()  # Create a new instance
    # Test 1: Initial size should be 0
    assert string_builder.size() == 0, "Initial size should be 0"
    # Test 2: Initial output should be an empty string
    assert string_builder.output() == "", "Initial output should be empty"
    # Add first string
    string_builder.add("Hello")
    # Test 3: Size should update correctly
    assert string_builder.size() == 5, "Size should be 5 after adding 'Hello'"
    # Test 4: Output should return what was added
    assert string_builder.output() == "Hello", "Output should be 'Hello'"
    # Add second string
    string_builder.add(" world")
    # Test 5: Size should update again
    assert string_builder.size() == 11, "Size should be 11 after adding ' world'"
    # Test 6: Output should now be combined
    assert string_builder.output() == "Hello world", "Output should be 'Hello world'"
