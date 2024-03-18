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

## Create Filters

Create your config files for the filtering functionality to the subdirectory `./src/config/`. The program exclusively searches **only** for the files named `cities.txt` and `species.txt`.

If a config file is found, the software will only allow those cities and species through. All other records are ignored.

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
