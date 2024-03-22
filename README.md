# PYTHON WEB SCRAPER FOR TIIRA.FI

## Install Dependencies and Setup the Project

Start by allowing the execution for the dependency script:

```
chmod u+x ./setup.sh
```

and then run the script with

```
./setup.sh
```

(_sudo permissions required_)

## Running the Project

The application can be now run with

```
./run.sh
```

or alternatively with

```
python3 ./src/main.py
```

Exit the program anytime with input `Ctrl` + `C`.

History can be deleted by executing

```
./delhistory.sh
```

History will be automatically deleted at 00:00 every 24 hours.

You may have to specify the execution rights for the scripts with `chmod` as described earlier.

## Create Filters (Configs)

Create your config files for the filtering functionality to the subdirectory `./src/config/`. The program exclusively searches **only** for the files named `cities.txt` and `species.txt`.

If a config file is found, the software will only allow those cities and species through. All other records are ignored. **Without config files, all elements will get through**. The config files are therefore "whitelists".

Individual entries in the config files should be separated with line breaks.

**For example**, config file for city filtering at `./src/config/cities.txt` could look like this:

```
Helsinki
Espoo
Kauniainen
Vantaa
Kirkkonummi
Sipoo
```

In this case, only records for these listed cities would get processed.

## Messager Bot & Environment Variables

If you wish to use a Telegram bot, create your own bot and add the API key to a file `./src/env.py` (check the imports for `./src/messenger.py`). Also add the recipient ID(s) to the `CHAT_IDS` constant.

An example `env.py` would look like this:

```
TELEGRAM_BOT_API_KEY = "1234567890abcdefghijklmnopqrstuvwxyz"
CHAT_IDS = ["1234567890", "0987654321"]
```

located at `./src/env.py`. **Please comment out the message sending logic out from** `main.py` **if you do not have the Telegram bot and/or environment initialized**.

**How to get the Telegram ID?**

1. Send a "/start" message to the Telegram Raw Data bot at @_RawDataBot_.

2. Read your ID from the response message (JSON) from `message.chat.id`.

3. Add the ID to the `CHAT_IDS` constant. Now you will receive the automated messages.
