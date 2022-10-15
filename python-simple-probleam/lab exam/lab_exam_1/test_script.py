def make_upper(text):
    return text.upper()


def make_capital(text):
    return text.capitalize()


def make_lower(text):
    return text.lower()


if __name__ == '__main__':
    make_upper("rafe")
    make_capital("rafe")
    make_lower("RAFE")


def test_script():
    assert make_upper("rafe")
    assert make_capital("rafe")
    assert make_lower("RAFE")
