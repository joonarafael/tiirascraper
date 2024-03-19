# PYTHON WEB SCRAPER FOR TIIRA.FI

## Install Dependencies and Setup the Project

(_sudo permissions required_)

Start by allowing the execution for the dependency script:

```
chmod u+x ./setup.sh
```

and then run the script with

```
./setup.sh
```

## Running the Project

The application can be now run with

```
./run.sh
```

or alternatively with

```
python3 ./src/main.py
```

History can be deleted at anytime by executing

```
./delhistory.sh
```

## Create Filters

Create your config files for the filtering functionality to the subdirectory `./src/config/`. The program exclusively searches **only** for the files named `cities.txt` and `species.txt`.

If a config file is found, the software will only allow those cities and species through. All other records are ignored. Without config files, all elements will get through.

Separate individual entries in the config files with line breaks.

**For example**, `cities.txt` could look like this:

```
Helsinki
Espoo
Kauniainen
Vantaa
Kirkkonummi
Sipoo
```

In this case, only records for these listed cities would get processed.

## Messager Bot

If you wish to use a Telegram bot, create your own bot and add the API key to a file named `env.py` within `./src/`. Also add the recipient ID(s) to the `CHAT_IDS` constant.

**How to get the Telegram ID?**

1. Send a real message (no commands or anything) to the bot.

2. Fetch your ID with an HTTP request. With Python, it can be achieved like this:

```
import requests
TOKEN = "{your_bot_api_token}"

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
r = requests.get(url).json()
print(r)
```

You may now retrieve your ID from the JSON object `r.result.chat.id`.

3. Add the ID to the `CHAT_IDS` constant. Now you will receive the automated messages.
