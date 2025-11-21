from utils import load_data
import builtins
import sys

def test_load_data_success():
    data = load_data()
    assert "n" in data
    assert "flights" in data
    assert "src" in data
    assert "dst" in data
    assert "k" in data
def test_load_data_file_not_found(monkeypatch):

    def mock_open(*args, **kwargs):
        raise FileNotFoundError

    monkeypatch.setattr(builtins, "open", mock_open)

    try:
        load_data()
    except SystemExit as e:
        assert e.code == 1
    else:
        assert False, "SystemExit not raised"

def test_load_data_invalid_json(monkeypatch):

    def mock_open(*args, **kwargs):
        from io import StringIO
        return StringIO("invalid json")

    monkeypatch.setattr(builtins, "open", mock_open)

    try:
        load_data()
    except SystemExit as e:
        assert e.code == 1
    else:
        assert False, "SystemExit not raised"

def test_load_data_empty_file(monkeypatch):

    def mock_open(*args, **kwargs):
        from io import StringIO
        return StringIO("")

    monkeypatch.setattr(builtins, "open", mock_open)

    try:
        load_data()
    except SystemExit as e:
        assert e.code == 1
    else:
        assert False, "SystemExit not raised"