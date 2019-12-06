import a

def test_algorithm_with_a_in_name():
    assert a.algorithm("iordanis") == "iord1nis"

def test_algorithm_without_a_in_name():
    assert a.algorithm("without") == "without"