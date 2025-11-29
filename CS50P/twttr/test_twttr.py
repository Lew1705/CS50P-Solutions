from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("apple") == "ppl"
    assert shorten("bottle") == "bttl"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("BUTTER") == "BTTR"
    assert shorten("LAPTOP") == "LPTP"

def test_mixedcase():
    assert shorten("Programming") == "Prgrmmng"
    assert shorten("CompUTer") == "CmpTr"
    assert shorten("Lab") == "Lb"

def test_numbers_and_symbols():
    assert shorten("12345") == "12345"
    assert shorten("!$%^%^&*&^%$£") == "!$%^%^&*&^%$£"
    assert shorten("T3st1ng") == "T3st1ng"

def test_empty_string():
    assert shorten("") == ""

#["a" ,"e", "i", "o", "u"]:
