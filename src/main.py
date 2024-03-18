from prettyio.prettyio import PrettyIO
from prettyio.ioconstants import IOConstants
from config import Config
from htmlparser import HTMLParser
from history import History
from filter import Filter

if __name__ == "__main__":
    io_handler = PrettyIO()
    io_constants = IOConstants()

    io_handler.write(f'       ' + io_constants.BOLD + 'LAUNCHING ' + io_constants.FG_GREEN + 'TIIRASCRAPER')
    io_handler.write("[info] Loading configs...")

    config_handler = Config(io_handler, io_constants)
    config = config_handler.get_config()

    io_handler.write("[info] Configuration loading finished. Relaunch the software for a new config.")

    city_count = len(config["cities"])

    if city_count == 0:
        city_count = "inf"

    species_count = len(config["species"])

    if species_count == 0:
        species_count = "inf"

    io_handler.write(io_constants.BOLD + f"[rslt] Recognized {city_count} allowed cities and {species_count} allowed species.")
    io_handler.write("[info] Loading history...")

    history_handler = History(io_handler, io_constants)
    history = history_handler.get_history()

    io_handler.write(io_constants.BOLD + f"[rslt] History currently includes {len(history)} records.")
    io_handler.write("[info] Requesting 'https://www.tiira.fi/', parsing HTML, and reading the table...")

    parser_handler = HTMLParser(io_handler, io_constants, "https://www.tiira.fi/")
    parsed_records = parser_handler.get_records()

    io_handler.write("[info] Parsing finished.")
    io_handler.write("[info] Performing the record filtering against config files and history...")

    filter_handler = Filter(io_handler, io_constants, config, history_handler)
    filtered_records = filter_handler.filter_records(parsed_records)

    io_handler.write(f"[info] Filtering finished.")
    io_handler.write(io_constants.BOLD + f"[rslt] Found a total of {len(filtered_records)} records that match the allowed cities & species.")
    io_handler.write(io_constants.BOLD + "[rslt] " + io_constants.BG_MAGENTA + "THE FILTERED RECORDS ARE:")

    for i, record in enumerate(filtered_records):
        if i % 2 == 0:
            io_handler.write(io_constants.FG_CYAN + f"  {str(i).zfill(4)} {str(record)}")
        else:
            io_handler.write(f"  {str(i).zfill(4)} {str(record)}")

    if len(filtered_records) == 0:
        io_handler.write(f"       (None)")

    