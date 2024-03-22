import schedule 
import time
from datetime import datetime

from prettyio.prettyio import PrettyIO
from prettyio.ioconstants import IOConstants
from config import Config
from htmlparser import HTMLParser
from history import History
from filter import Filter
from messenger import Messenger
from formatter import Formatter

def application():
    io_handler = PrettyIO()
    io_constants = IOConstants()

    io_handler.write(io_constants.BOLD + f"[time] {str(datetime.now())}")

    # START LOADING CONFIGS AND HISTORY

    io_handler.write("[info] Loading configs...")

    config_handler = Config(io_handler, io_constants)
    config = config_handler.get_config()

    io_handler.write("[info] Configuration loading finished.")

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

    # ACTUAL HTML REQUEST AND DATA PARSING + FILTERING

    io_handler.write("[info] Requesting 'https://www.tiira.fi/', parsing HTML, and reading the table...")

    parser_handler = HTMLParser(io_handler, io_constants, "https://www.tiira.fi/")
    parsed_records = parser_handler.get_records()

    io_handler.write("[info] Parsing finished.")
    io_handler.write("[info] Performing the record filtering against config files and history...")

    filter_handler = Filter(io_handler, io_constants, config, history_handler)
    filtered_records = filter_handler.filter_records(parsed_records)

    io_handler.write(f"[info] Filtering finished.")
    io_handler.write(io_constants.BOLD + f"[rslt] Found a total of {len(filtered_records)} new records that match the allowed cities & species.")
    io_handler.write(io_constants.BOLD + io_constants.BG_MAGENTA + "[rslt] THE FILTERED RECORDS ARE:")

    for i, record in enumerate(filtered_records):
        if i % 2 == 0:
            io_handler.write(io_constants.FG_CYAN + f"  {str(i + 1).zfill(4)} {str(record)}")
        else:
            io_handler.write(f"  {str(i + 1).zfill(4)} {str(record)}")

    if len(filtered_records) == 0:
        io_handler.write(f"       (None)")

    # MESSAGE SENDING LOGIC
    # COMMENT OUT IF YOU DON'T HAVE THE TELEGRAM BOT INITIALIZED!
    
    message_handler = Messenger(io_handler, io_constants)
    formatting_handler = Formatter()
        
    if len(filtered_records) > 0:
        formatted_records = formatting_handler.format_records(filtered_records)
        message_handler.send_message(formatted_records)

if __name__ == "__main__":
    application()
    schedule.every(5).minutes.do(application) 
    
    while True:
        schedule.run_pending() 
        print("[info] Waiting... Terminate process at anytime with 'Ctrl + C'.")
        time.sleep(60) 
