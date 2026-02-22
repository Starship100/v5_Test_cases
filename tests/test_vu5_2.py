from vu5_2 import sum_list

def test_empty_list():
    #expected = 0
    #actual = sum_list([])
    #assert actual == expected
    assert sum_list([]) == 0

def test_number_list():
    # testa med listor som har 1, 2 respektive 5 element
    assert sum_list([5]) == 5
    assert sum_list([4, 5]) == 9
    assert sum_list([1, 2, 3, 4, 5]) == 15