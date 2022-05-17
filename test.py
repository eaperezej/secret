from main import (
    one,
    three,
    four,
    five,
    seven,
    eight,
    nine,
    times,
    plus,
    minus,
    divided_by
)


def test_times():
    assert four(times(five())) == 20


def test_plus():
    assert one(plus(eight())) == 9


def test_minus():
    assert seven(minus(three())) == 4


def test_divided_by():
    assert nine(divided_by(three())) == 3
