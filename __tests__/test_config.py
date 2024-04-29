import pytest
import tempfile
import os
from pathlib import Path
from src.config import Config

class MockIO:
    def __init__(self):
        self.messages = []

    def write(self, message):
        self.messages.append(message)

class MockIOConstants:
    BOLD = ""
    BG_RED = ""
    FG_CYAN = ""

@pytest.fixture
def temp_files():
    with tempfile.TemporaryDirectory() as tmp_dir:
        cities_path = os.path.join(tmp_dir, "cities.txt")
        species_path = os.path.join(tmp_dir, "species.txt")

        with open(cities_path, "w") as f:
            f.write("City1\nCity2\nCity3\n")

        with open(species_path, "w") as f:
            f.write("Species1\nSpecies2\nSpecies3\n")

        yield cities_path, species_path

def test_config_read_files(temp_files):
    cities_path, _ = temp_files
    config = Config(MockIO(), MockIOConstants())

    config.path = os.path.dirname(cities_path) + "/"

    config.read_file_cities()
    config.read_file_species()

    assert config.cities == ["city1", "city2", "city3"]
    assert config.species == ["species1", "species2", "species3"]

def test_config_get_config(temp_files):
    cities_path, _ = temp_files
    config = Config(MockIO(), MockIOConstants())
    
    config.path = os.path.dirname(cities_path) + "/"

    result = config.get_config()

    assert result["cities"] == ["city1", "city2", "city3"]
    assert result["species"] == ["species1", "species2", "species3"]

def test_config_read_no_files(temp_files):
    cities_path, species_path = temp_files
    config = Config(MockIO(), MockIOConstants())

    config.io.messages = []

    config.path = os.path.dirname(cities_path) + "/"

    os.remove(cities_path)
    os.remove(species_path)

    config.read_file_cities()
    config.read_file_species()

    assert config.cities == []
    assert config.species == []

    assert len(config.io.messages) == 10
    assert "[ERRR] Error while reading configuration file for cities." in config.io.messages[0]

def test_config_get_no_config(temp_files):
    cities_path, species_path = temp_files
    config = Config(MockIO(), MockIOConstants())

    config.path = os.path.dirname(cities_path) + "/"

    config.io.messages = []

    os.remove(cities_path)
    os.remove(species_path)

    result = config.get_config()

    assert result["cities"] == []
    assert result["species"] == []

    assert len(config.io.messages) == 10
    assert "[ERRR] Error while reading configuration file for cities." in config.io.messages[0]