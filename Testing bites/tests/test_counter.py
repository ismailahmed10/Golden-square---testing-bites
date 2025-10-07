from lib.counter import Counter

def test_checking_number_counted():
    current_count = Counter()
    current_count.add(5)
    assert current_count.report() == "Counted to 5 so far."

def test_checking__multiple_numbers_counted():
    current_count = Counter()
    current_count.add(5)
    current_count.add(10)
    assert current_count.report() == "Counted to 15 so far."