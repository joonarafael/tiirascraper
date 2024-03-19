class Formatter():
    def __init__(self):
        pass

    def format_records(self, records):
        formatted_records = "New observations have been found!\n\n"

        for i, record in enumerate(records):
            species = record["species"]
            body = record["body"]
            formatted_records += f"{str(i + 1).zfill(2)}: {species}: {body}\n\n"

        return formatted_records