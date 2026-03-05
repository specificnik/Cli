import subprocess


def left_pad(s: str, i: int) -> str:
    """Pads a string with spaces on the left, so that its minimum length is i."""
    return (" " * i + s)[-i:]


def fizzbuzz(i) -> str:
    """Fizzbuzz for a single number i.

    Returns 'fizz' for multiples of 3, 'buzz' for multiples of 5, 'fizzbuzz'
    for multiples of both, and the number itself otherwise."""
    if i % 3 == 0:
        return "fizz"
    if i % 5 == 0:
        return "buzz"
    if i % 15 == 0:
        return "fizzbuzz"
    else:
        return i


def div(a: int, b: int) -> int:
    if b == 0:
        msg = "divide by zero"
        raise ValueError(msg)
    return a // b


def get_file_contents(filename: str) -> str:
    return subprocess.check_output(f"cat {filename}", shell=True)
