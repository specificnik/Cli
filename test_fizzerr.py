import fizzerr


def test_fizzbuzz_fizz():
    # Test for multiples of 3
    assert fizzerr.fizzbuzz(3) == "fizz"


def test_fizzbuzz_fizz_2():
    # Test for multiples of 3
    assert fizzerr.fizzbuzz(30) == "fizzbuzz"
