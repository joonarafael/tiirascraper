from bs4 import BeautifulSoup
import requests

class HTMLParser:
    def __init__(self, url):
        self.url = url
        self.records = []

    def parse(self):
        try:
            self.page = requests.get(self.url)
            self.soup = BeautifulSoup(self.page.text, features="html.parser")
        except Exception as e:
            print("Error while parsing HTML page", self.url)
            print(e)
    
    def get_table(self):
        try:
            self.table = self.soup.find_all("tr", class_="tumma") + self.soup.find_all("tr", class_="vaalea")
        except Exception as e:
            print("Error while reading tables from parsed HTML page.")
            print(e)

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
            print("No records initialized:")
            print("Parsed table seems to be empty.")
    
    def get_records(self):
        self.parse()
        self.get_table()
        self.initialize_records()

        return self.records