from config import Config
from htmlparser import HTMLParser

if __name__ == "__main__":
    print("Launching...")
    print("Reading configs...")

    config_handler = Config()
    config = config_handler.get_config()

    print("Configuration read.")

    city_count = len(config["cities"])

    if city_count == 0:
        city_count = "inf"

    species_count = len(config["species"])

    if species_count == 0:
        species_count = "inf"

    print("Recognized", city_count, "allowed cities and", species_count, "allowed species.")

    print("Parsing HTML and reading the table...")

    parser_handler = HTMLParser("https://www.tiira.fi/")

    parsed_records = parser_handler.get_records()

    if (parsed_records and len(parsed_records) > 0):
        for parsed_record in parsed_records:
            print(parsed_record)