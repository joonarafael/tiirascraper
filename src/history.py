from pathlib import Path
from datetime import datetime

class History:
    def __init__(self, io, io_constants):
        self.io = io
        self.io_constants = io_constants
        absolute_path = str(Path(__file__).absolute())

        self.path = absolute_path[:len(absolute_path)-10] + "history/history.txt"
        self.creation_path = absolute_path[:len(absolute_path)-10] + "history/creation.txt"

        self.history = []
    
    def read_file_history(self):
        try:
            with open(self.path, "r") as f:
                self.history = f.read().splitlines()
        
        except Exception as e:
            self.io.write(self.io_constants.BOLD + self.io_constants.BG_RED + "[ERRR] Error while reading the history file.")
            self.io.write(f"       {str(e)}")
            self.io.write(f"       Make sure the file {self.path} actually exists and is intact.")
            self.io.write(f"       Additionally ensure the program has required permissions to read the file.")
            self.io.write(self.io_constants.FG_CYAN + f"       Program execution continues without any history.")

    def create_history_file(self):
        try:
            with open(self.path, "w") as f:
                with open(self.creation_path, "w") as d:
                    time = datetime.now()
                    current_time = time.strftime("%H:%M:%S")

                    date = time.date()

                    d.write(f"{date}\n")
                    d.write(f"{current_time}")
        
        except Exception as e:
            self.io.write(self.io_constants.BOLD + self.io_constants.BG_RED + "[ERRR] Error while creating the history file.")
            self.io.write(f"       {str(e)}")
            self.io.write(f"        Ensure the program has required permissions to write the file.")
            self.io.write(self.io_constants.FG_CYAN + f"       Program execution continues without any history.")
    
    def write_history(self, addition):
        if addition:
            self.read_file_history()

            if self.history and len(self.history) > 0:
                try:
                    with open(self.path, "a") as f:
                        f.write(f"{str(addition)}\n")
                
                except Exception as e:
                    self.io.write(self.io_constants.BOLD + self.io_constants.BG_RED + "[ERRR] Error while writing to the history to file.")
                    self.io.write(f"       {str(e)}")
                    self.io.write(f"       Make sure the file {self.path} actually exists and is intact.")
                    self.io.write(f"       Additionally ensure the program has required permissions to read and write to the file.")
                    self.io.write(self.io_constants.FG_CYAN + f"       Program execution continues without the recorded history.")
            
            else:
                self.create_history_file()

                try:
                    with open(self.path, "a") as f:
                        f.write(f"{str(addition)}\n")
                
                except Exception as e:
                    self.io.write(self.io_constants.BOLD + self.io_constants.BG_RED + "[ERRR] Error while writing to the history to file.")
                    self.io.write(f"       {str(e)}")
                    self.io.write(f"       Make sure the file {self.path} actually exists and is intact.")
                    self.io.write(f"       Additionally ensure the program has required permissions to read and write to the file.")
                    self.io.write(self.io_constants.FG_CYAN + f"       Program execution continues without the recorded history.")

    def get_history(self):
            self.read_file_history()

            return self.history