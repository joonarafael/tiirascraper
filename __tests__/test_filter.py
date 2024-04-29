import pytest
from src.filter import Filter

class MockHistoryHandler:
    def __init__(self):
        self.history = []

    def get_history(self):
        return self.history

    def write_history(self, record):
        self.history.append(str(record))

@pytest.fixture
def filter_instance():
    cities = ["city1", "city2", "city3"]
    species = ["species1", "species2", "species3"]
    config = {"cities": cities, "species": species}

    history_handler = MockHistoryHandler()
    io = None
    io_constants = None

    return Filter(io, io_constants, config, history_handler)

@pytest.fixture
def empty_configs_filter_instance():
    cities = []
    species = []
    config = {"cities": cities, "species": species}

    history_handler = MockHistoryHandler()
    io = None
    io_constants = None

    return Filter(io, io_constants, config, history_handler)

def test_check_city_against_config(filter_instance, empty_configs_filter_instance):
    assert filter_instance.check_city_against_config("city1 some other data") == True
    assert filter_instance.check_city_against_config("city4 some other data") == False

    assert empty_configs_filter_instance.check_city_against_config("city1 some other data") == True
    assert empty_configs_filter_instance.check_city_against_config("city4 some other data") == True

def test_check_species_against_config(filter_instance, empty_configs_filter_instance):
    assert filter_instance.check_species_against_config("species1 subspecies") == True
    assert filter_instance.check_species_against_config("species4") == False

    assert empty_configs_filter_instance.check_species_against_config("species1 subspecies") == True
    assert empty_configs_filter_instance.check_species_against_config("species4") == True

def test_check_record_against_history(filter_instance):
    record = {"body": "some body", "species": "some species"}

    assert filter_instance.check_record_against_history(record) == False

    assert filter_instance.check_record_against_history(record) == True

def test_filter_records_against_config(filter_instance):
    records = [
        {"body": "city1 some species", "species": "species1"},
        {"body": "city4 some species", "species": "species1"}
    ]
    filtered_records = filter_instance.filter_records_against_config(records)
    assert len(filtered_records) == 1
    assert filtered_records[0] == records[0]

def test_filter_records_against_history(filter_instance):
    records = [
        {"body": "some body", "species": "some species"},
        {"body": "another body", "species": "another species"}
    ]
    filtered_records = filter_instance.filter_records_against_history(records)
    assert len(filtered_records) == 2

    filtered_records = filter_instance.filter_records_against_history(records)
    assert len(filtered_records) == 0

def test_filter_records(filter_instance):
    records = [
        {"body": "city1 some species", "species": "species1"},
        {"body": "city4 some species", "species": "species1"},
        {"body": "city3 some species", "species": "species4"},
        {"body": "city2 some species", "species": "species3"},
    ]

    filtered_records = filter_instance.filter_records(records)
    assert len(filtered_records) == 2
