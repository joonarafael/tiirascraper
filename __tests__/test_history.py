import pytest
import tempfile
import os
from pathlib import Path
from src.history import History
from datetime import datetime, timedelta

class MockIO:
    def __init__(self):
        self.messages = []

    def write(self, message):
        self.messages.append(message)

class MockIOConstants:
    BOLD = ""
    BG_RED = ""
    FG_CYAN = ""
    BG_MAGENTA = ""

@pytest.fixture
def temp_history_files():
    with tempfile.TemporaryDirectory() as tmp_dir:
        history_path = os.path.join(tmp_dir, "history.txt")
        creation_path = os.path.join(tmp_dir, "creation.txt")

        with open(history_path, "w") as f:
            f.write("Event1\nEvent2\nEvent3\n")

        with open(creation_path, "w") as f:
            f.write("2000-01-01\n")

        yield history_path, creation_path

@pytest.fixture
def temp_current_history_files():
    with tempfile.TemporaryDirectory() as tmp_dir:
        history_path = os.path.join(tmp_dir, "history.txt")
        creation_path = os.path.join(tmp_dir, "creation.txt")

        with open(history_path, "w") as f:
            f.write("Event1\nEvent2\nEvent3\n")

        current_date = datetime.now().date()
        with open(creation_path, "w") as f:
            f.write(str(current_date) + "\n")

        yield history_path, creation_path

def test_history_read_files(temp_history_files):
    history_path, creation_path = temp_history_files
    history = History(MockIO(), MockIOConstants())

    history.path = history_path
    history.creation_path = creation_path

    history.read_file_history()
    history.read_file_creation()

    assert history.history == ["Event1", "Event2", "Event3"]
    assert history.creation_time == ["2000-01-01"]

def test_history_get_history_creation_time(temp_history_files):
    _, creation_path = temp_history_files
    history = History(MockIO(), MockIOConstants())

    history.creation_path = creation_path

    creation_time = history.get_history_creation_time()

    assert creation_time == "2000-01-01"

def test_history_check_if_history_is_expired(temp_history_files):
    _, creation_path = temp_history_files
    history = History(MockIO(), MockIOConstants())

    history.creation_path = creation_path

    assert history.check_if_history_is_expired()

def test_history_write_history(temp_history_files):
    history_path, creation_path = temp_history_files
    history = History(MockIO(), MockIOConstants())

    history.path = history_path
    history.creation_path = creation_path

    history.write_history("New Event")

    with open(history_path, "r") as f:
        content = f.read()

    assert "New Event" in content

def test_history_get_history(temp_current_history_files):
    history_path, creation_path = temp_current_history_files
    history = History(MockIO(), MockIOConstants())

    history.path = history_path
    history.creation_path = creation_path

    retrieved_history = history.get_history()

    assert retrieved_history == ["Event1", "Event2", "Event3"]
