def _check(loc, fn):
    if fn:
        return eval(loc + fn)
    return loc


def zero(fn=None):
    return _check("0", fn)


def one(fn=None):
    return _check("1", fn)


def two(fn=None):
    return _check("2", fn)


def three(fn=None):
    return _check("3", fn)


def four(fn=None):
    return _check("4", fn)


def five(fn=None):
    return _check("5", fn)


def six(fn=None):
    return _check("6", fn)


def seven(fn=None):
    return _check("7", fn)


def eight(fn=None):
    return _check("8", fn)


def nine(fn=None):
    return _check("9", fn)


def plus(fn):
    symbol = "+"

    return symbol + fn


def minus(fn):
    symbol = "-"

    return symbol + fn


def times(fn):
    symbol = "*"

    return symbol + fn


def divided_by(fn):
    symbol = "//"

    return symbol + fn
