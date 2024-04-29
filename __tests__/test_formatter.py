import unittest

from src.formatter import Formatter

class TestFormatter(unittest.TestCase):
    def test_format_records_single_record(self):
        formatter = Formatter()
        records = [{
            "species": "species0 subspecies",
            "body": "city district province country, observer"
        }]
        expected_output = (
            "New observations have been found!\n\n"
            "01: species0 subspecies: city district province country, observer\n\n"
        )
        self.assertEqual(formatter.format_records(records), expected_output)

    def test_format_records_multiple_records(self):
        formatter = Formatter()
        records = [
            {
                "species": "species0 subspecies",
                "body": "city1 district1 province1 country1, observer1"
            },
            {
                "species": "species1 subspecies",
                "body": "city2 district2 province2 country2, observer2"
            },
            {
                "species": "species2 subspecies",
                "body": "city3 district3 province3 country3, observer3"
            }
        ]
        expected_output = (
            "New observations have been found!\n\n"
            "01: species0 subspecies: city1 district1 province1 country1, observer1\n\n"
            "02: species1 subspecies: city2 district2 province2 country2, observer2\n\n"
            "03: species2 subspecies: city3 district3 province3 country3, observer3\n\n"
        )
        self.assertEqual(formatter.format_records(records), expected_output)

    def test_format_records_empty_records(self):
        formatter = Formatter()
        records = []
        expected_output = "New observations have been found!\n\n"
        self.assertEqual(formatter.format_records(records), expected_output)

if __name__ == '__main__':
    unittest.main()
