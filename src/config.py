from pathlib import Path

class Config:
    def __init__(self, io, io_constants):
        self.io = io
        self.io_constants = io_constants
        absolute_path = str(Path(__file__).absolute())

        self.path = absolute_path[:len(absolute_path)-9] + "config/"

        self.cities = []
        self.species = []
    
    def read_file_cities(self):
        self.cities_path = self.path + "cities.txt"

        try:
            with open(self.cities_path, "r") as f:
                self.cities = f.read().splitlines()

                for i, city in enumerate(self.cities):
                    self.cities[i] = city.lower()

        except Exception as e:
            self.io.write(self.io_constants.BOLD + self.io_constants.BG_RED + "[ERRR] Error while reading configuration file for cities.")
            self.io.write(f"       {str(e)}")
            self.io.write(f"       Make sure the file '{self.cities_path}' actually exists and is intact.")
            self.io.write("       Additionally ensure the program has required permissions to read the file.")
            self.io.write(self.io_constants.BOLD + self.io_constants.FG_CYAN + "       Program execution continues without any configured cities.")

    def read_file_species(self):
        self.species_path = self.path + "species.txt"

        try:
            with open(self.species_path, "r") as f:
                self.species = f.read().splitlines()

                for i, species in enumerate(self.species):
                    self.species[i] = species.lower()

        except Exception as e:
            self.io.write(self.io_constants.BOLD + self.io_constants.BG_RED + "[ERRR] Error while reading configuration file for species.")
            self.io.write(f"       {str(e)}")
            self.io.write(f"       Make sure the file '{self.species_path}' actually exists and is intact.")
            self.io.write("       Additionally ensure the program has required permissions to read the file.")
            self.io.write(self.io_constants.BOLD + self.io_constants.FG_CYAN + "       Program execution continues without any configured species.")

    def get_config(self):
        self.read_file_cities()
        self.read_file_species()

        return {
            "cities": self.cities,
            "species": self.species
        }