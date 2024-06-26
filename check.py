from __future__ import print_function
from bs4 import BeautifulSoup
import requests
import schedule
from pathlib import Path
from src.env import TELEGRAM_BOT_API_KEY, CHAT_IDS

print("")
print("")

print("If no error was raised, you're good to go! Required dependencies seem to be alright.")
print("Before running the project, set your configuration files and initialize environment variables!")
print("Consult the './docs/user_manual.md' file for more information.")