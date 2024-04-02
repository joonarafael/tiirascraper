class Filter:
    def __init__(self, io, io_constants, config, history_handler):
        self.io = io
        self.io_constants = io_constants
        self.config_cities = config["cities"]
        self.config_species = config["species"]
        self.history_handler = history_handler
        self.history = self.history_handler.get_history()
    
    def check_city_against_config(self, body):
        blankspace_split = body.split()
        extracted_city = blankspace_split[0]

        if self.config_cities and len(self.config_cities) > 0:
            result = False
            
            for city in self.config_cities:
                if city in extracted_city:
                    result = True
            
            return result

        return True
    
    def check_species_against_config(self, species_input):
        blankspace_split = species_input.split()
        extracted_species = blankspace_split[0]

        if self.config_species and len(self.config_species) > 0:
            result = False
            
            for species in self.config_species:
                if species in extracted_species:
                    result = True
            
            return result
        
        return True
    
    def check_record_against_history(self, record):
        if self.history and len(self.history) > 0:
            result = False
            
            for history_record in self.history:
                if history_record == str(record):
                    result = True
            
            if result is False:
                self.history_handler.write_history(record)

            return result

        self.history_handler.write_history(record)
        return False
    
    def filter_records_against_config(self, records):
        filtered_records = []
        
        for record in records:
            if self.check_city_against_config(record["body"].lower()) and self.check_species_against_config(record["species"].lower()):
                filtered_records.append(record)
        
        return filtered_records

    def filter_records_against_history(self, records):
        filtered_records = []

        for record in records:
            if not self.check_record_against_history(record):
                filtered_records.append(record)
        
        return filtered_records
    
    def filter_records(self, records):
        self.history = self.history_handler.get_history()
        filtered_records = self.filter_records_against_config(records)
        filtered_records = self.filter_records_against_history(filtered_records)
        
        return filtered_records