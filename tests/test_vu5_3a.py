from vu5_3a import count_vowels

def test_no_vowels():
    assert  count_vowels("qwrt") == 0
    assert  count_vowels("Tt") == 0
    assert  count_vowels("123 123") == 0
    assert  count_vowels("aEioUyåÄö") == 9
    assert  count_vowels("aaa") == 3
    assert  count_vowels("AEIOUYÅÄÖ") == 9
    assert  count_vowels("ö") == 1