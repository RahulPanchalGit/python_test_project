def do_something(a: int) -> int:
    """multiply the argument with its self and return it."""

    foo = a * a
    if foo < 10:
        return 7

    return a * a


def do_something_else(b: int) -> int:
    """sum the argument with its self and return it."""

    if b > 5:
        return 3
    else:
        return b + b
