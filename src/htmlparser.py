from bs4 import BeautifulSoup
import requests

class HTMLParser:
    def __init__(self, io, io_constants, url):
        self.io = io
        self.io_constants = io_constants
        self.url = url
        self.records = []
        self.table = None

    def parse(self):
        try:
            self.page = requests.get(self.url)
            self.soup = BeautifulSoup(self.page.text, features="html.parser")
        except Exception as e:
            self.io.write(self.io_constants.BOLD + self.io_constants.BG_RED + f"[ERRR] Error while parsing HTML page '{self.url}'.")
            self.io.write(f"       {str(e)}.")
    
    def get_table(self):
        try:
            self.table = self.soup.find_all("tr", class_="tumma") + self.soup.find_all("tr", class_="vaalea")
        except Exception as e:
            self.io.write(self.io_constants.BOLD + self.io_constants.BG_RED + "[ERRR] Error while reading tables from parsed HTML page.")
            self.io.write(f"       {str(e)}.")

    def initialize_records(self):
        if self.table and len(self.table) > 0:
            for record in self.table:
                data = record.find_all("td")

                record = {
                    "species": data[0].text,
                    "body": data[2].text
                }

                self.records.append(record)
        
        else:
            self.io.write(self.io_constants.BOLD + "[rslt] No records initialized!")
            self.io.write(self.io_constants.BOLD + "[rslt] Parsed table seems to be empty.")
    
    def get_records(self):
        self.parse()
        self.get_table()
        self.initialize_records()

        return self.records