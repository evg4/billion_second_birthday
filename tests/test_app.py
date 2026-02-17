from lib.app import find_billion_birthday

def test_24th_dec(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda: '1994 12 24 12 00 00')
    assert find_billion_birthday() == "You will turn one billion seconds old on 1st September 2026 at 13:46:40!"

def test_25th_dec(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda: '1994 12 25 12 00 00')
    assert find_billion_birthday() == "You will turn one billion seconds old on 2nd September 2026 at 13:46:40!"

def test_26th_dec(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda: '1994 12 26 12 00 00')
    assert find_billion_birthday() == "You will turn one billion seconds old on 3rd September 2026 at 13:46:40!"

def test_1st_jan(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda: '1995 01 01 12 00 00')
    assert find_billion_birthday() == "You will turn one billion seconds old on 9th September 2026 at 13:46:40!"

def test_3rd_jan(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda: '1995 01 03 12 00 00')
    assert find_billion_birthday() == "You will turn one billion seconds old on 11th September 2026 at 13:46:40!"

def test_4th_jan(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda: '1995 01 04 17 00 00')
    assert find_billion_birthday() == "You will turn one billion seconds old on 12th September 2026 at 18:46:40!"

def test_5th_jan(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda: '1995 01 05 17 32 15')
    assert find_billion_birthday() == "You will turn one billion seconds old on 13th September 2026 at 19:18:55!"