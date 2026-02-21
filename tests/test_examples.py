from examples import add, hypo

def test_add():
    expected = 3
    actual = add(1, 2)
    assert actual == expected

def test_hypo():
    # testdata: a=5, b=12, =13
    expected = 13
    actual = hypo(5, 12)
    assert actual == expected