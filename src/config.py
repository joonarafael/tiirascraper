from pathlib import Path

class Config:
    def __init__(self):
        absolute_path = str(Path(__file__).absolute())

        self.path = absolute_path[:len(absolute_path)-9] + "config/"

        self.cities = []
        self.species = []
    
    def get_cities(self):
        self.cities_path = self.path + "cities.txt"

        try:
            with open(self.cities_path, "r") as f:
                self.cities = f.read().splitlines()

        except Exception as e:
            print("Error while reading configuration file for cities.")
            print(e)
            print("Make sure the file", self.cities_path, "actually exists and is intact.")
            print("Program execution continues without any configured cities.")

    def get_species(self):
        self.species_path = self.path + "species.txt"

        try:
            with open(self.species_path, "r") as f:
                self.species = f.read().splitlines()

        except Exception as e:
            print("Error while reading configuration file for species.")
            print(e)
            print("Make sure the file", self.species_path, "actually exists and is intact.")
            print("Program execution continues without any configured species.")

    def get_config(self):
        self.get_cities()
        self.get_species()

        return {
            "cities": self.cities,
            "species": self.species
        }