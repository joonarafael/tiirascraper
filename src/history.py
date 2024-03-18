from pathlib import Path

class History:
    def __init__(self, io, io_constants):
        self.io = io
        self.io_constants = io_constants
        absolute_path = str(Path(__file__).absolute())

        self.path = absolute_path[:len(absolute_path)-10] + "history/history.txt"

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
    
    def write_history(self, addition):
        if addition:
            try:
                with open(self.path, "a+") as f:
                    f.write(f"{str(addition)}\n")
            
            except Exception as e:
                self.io.write(self.io_constants.BOLD + self.io_constants.BG_RED + "[ERRR] Error while writing history to file.")
                self.io.write(f"       {str(e)}")
                self.io.write(f"       Make sure the file {self.path} actually exists and is intact.")
                self.io.write(f"       Additionally ensure the program has required permissions to read and write to the file.")
                self.io.write(self.io_constants.FG_CYAN + f"       Program execution continues without the recorded history.")

    def get_history(self):
        self.read_file_history()

        return self.history