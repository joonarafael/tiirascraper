# USER MANUAL

## Before Running

Create your _config files_ for the filtering functionality into the subdirectory `./src/config/`. The program exclusively searches **only** for the files named `cities.txt` and `species.txt`.

If a config file is found, the software will only allow those cities and species through. All other records are ignored. **Without config files, all elements will get through**. The config files are therefore so-called "whitelists".

Individual entries in the config files should be separated with line breaks. Config files **are not** case-sensitive (applies to both cities and species).

**For example**, config file for city filtering at `./src/config/cities.txt` could look like this:

```
Helsinki
Espoo
vantaa
Kirkkonummi
```

In this case, only records for these listed cities would get processed.

**_IMPORTANT_**: The program will parse the cities and species from the observations table by cutting the string at first space character. Do not include any space characters in your config file. **Subspecies (or city districts) cannot be thus specified**.

**This means that** if the parsed observation from _Tiira_ is, for example, `Sepelhanhi (alalaji bernicla)`, program will only consider `Sepelhanhi`. Filtering functions will only search for an exact match from your allowed species list.

## _Telegram_ Bot & Environment Variables

If you wish to use a _Telegram_ bot, create your own bot and add the API key to a file `./src/env.py` (check the imports for `./src/messenger.py`). Also add the recipient ID(s) to the `CHAT_IDS` constant.

An example `env.py` would look like this:

```
TELEGRAM_BOT_API_KEY = "1234567890abcdefghijklmnopqrstuvwxyz"
CHAT_IDS = ["1234567890", "0987654321"]
```

located at `./src/env.py`.

**_IMPORTANT_**: **Comment out the message sending logic out from** `main.py` **if you do not have the Telegram bot and/or environment initialized**. Program execution will halt to a runtime exception if environment variables are not specified!

**How to get the Telegram ID?**

1. Send a "/start" message to the _Telegram Raw Data_ bot at @_RawDataBot_.

2. Read your ID from the response message (JSON) from `message.chat.id`.

3. Add the ID to the `CHAT_IDS` constant. Now your bot will send you the messages.

## Running the Project

After successful installation of all project dependencies, the application can be run with

```
./run.sh
```

The `setup.sh` script should've given execution rights to all project scripts, but if you're prohibited from running the script, manually change the permissions with

```
chmod u+x script_name.sh
```

If you're running on _Windows_ and/or _bash_ scripts are not an option for you, the project can be always started with

```
python3 ./src/main.py
```

Exit the program anytime with input `Ctrl` + `C`.

## Runtime Exceptions and Other Bugs

The program has quite robust error handling and will explain with high detail every single step during the execution. If the program encounters errors (file I/O, internet connection, etc.), you should receive verbose error messages to the console. Check the output and figure out how to handle the situation.

## History

If need be, history can be deleted by executing

```
./delhistory.sh
```

The program does not support any other automated history deletion options (as it is not an intended use-case). However, the associated history files may be deleted manually at `./src/history/history.txt` and `./src/history/creation.txt`.

Program will reset the history at 00:00 every day.

## Automated Testing

Automated tests can be executed with

```
./test.sh
```
