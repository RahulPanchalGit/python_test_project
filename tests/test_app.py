from app import do_something, do_something_else


def test_do_something_25():
    """provide 5 as an argument and expect 25 to be returned. just test"""

    result = do_something(a=5)
    assert result == 25


def test_do_something_else_8():
    """provide 4 as an arg and expect back 8."""

    result = do_something_else(b=4)
    assert result == 8


def test_do_something_else_3():
    """provide 6 as an arg and expect back 3."""

    result = do_something_else(b=6)
    assert result == 3
