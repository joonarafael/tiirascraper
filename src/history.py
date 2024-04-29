from pathlib import Path
from datetime import datetime

class History:
    def __init__(self, io, io_constants):
        self.io = io
        self.io_constants = io_constants
        absolute_path = str(Path(__file__).absolute())

        self.path = absolute_path[:len(absolute_path)-10] + "history/history.txt"
        self.creation_path = absolute_path[:len(absolute_path)-10] + "history/creation.txt"

        self.creation_time = []

        try:
            with open(self.creation_path, "r") as f:
                self.io.write("[info] History creation time file has been found and successfully opened.")
        
        except Exception as e:
            self.io.write(self.io_constants.BOLD + self.io_constants.BG_RED + "[ERRR] Error while reading the history creation file.")
            self.io.write(f"       {str(e)}")
            self.io.write(f"       Make sure the file '{self.creation_path}' actually exists and is intact.")
            self.io.write("       Additionally ensure the program has required permissions to read and write to the file.")
            self.io.write(self.io_constants.BOLD + self.io_constants.FG_CYAN + "       Program will launch without considering the possibility of expired history.")
            self.io.write(self.io_constants.FG_CYAN + "       However, the program will continue to try to write new history.")

        try:
            with open(self.path, "r") as f:
                self.io.write("[info] History file has been found and successfully opened.")
        
        except Exception as e:
            self.io.write(self.io_constants.BOLD + self.io_constants.BG_RED + "[ERRR] Error while reading the history file.")
            self.io.write(f"       {str(e)}")
            self.io.write(f"       Make sure the file '{self.path}' actually exists and is intact.")
            self.io.write("       Additionally ensure the program has required permissions to read and write to the file.")
            self.io.write(self.io_constants.BOLD + self.io_constants.FG_CYAN + "       Program will launch without any previous history.")
            self.io.write(self.io_constants.FG_CYAN + "       However, the program will continue to try to write new history.")

    def read_file_creation(self):
        try:
            with open(self.creation_path, "r") as f:
                self.creation_time = f.read().splitlines()
        
        except Exception:
            pass

    def get_history_creation_time(self):
        self.creation_time = []
        self.read_file_creation()

        if self.creation_time and len(self.creation_time) > 0:
            return self.creation_time[0]
        
        return None
    
    def check_if_history_is_expired(self):
        creation_time = self.get_history_creation_time()

        if creation_time:
            current_time = datetime.now()
            current_date = current_time.date()

            if str(creation_time) != str(current_date):
                self.io.write(self.io_constants.BOLD + self.io_constants.BG_MAGENTA + "[info] History has expired!")
                self.io.write("       Resetting history.")
                return True
        
        return False

    def read_file_history(self):
        try:
            with open(self.path, "r") as f:
                self.history = f.read().splitlines()
        
        except Exception:
            pass

    def create_history_file(self):
        try:
            with open(self.path, "w") as _:
                with open(self.creation_path, "w") as d:
                    time = datetime.now()
                    date = time.date()

                    d.write(f"{date}")
        
        except Exception:
            pass
    
    def write_history(self, addition):
        if addition:
            self.read_file_history()

            if self.history and len(self.history) > 0:
                if self.check_if_history_is_expired():
                    self.create_history_file()

                try:
                    with open(self.path, "a") as f:
                        f.write(f"{str(addition)}\n")
                
                except Exception:
                    pass
            
            else:
                self.create_history_file()

                try:
                    with open(self.path, "a") as f:
                        f.write(f"{str(addition)}\n")
                
                except Exception:
                    pass

    def get_history(self):
        if self.check_if_history_is_expired():
            self.create_history_file()

        self.read_file_history()

        if len(self.history) == 0:
            self.create_history_file()

        return self.history