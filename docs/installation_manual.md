# INSTALLATION MANUAL

This document contains the instructions for the installation of the project. Installation procedure is automated for the _UNIX_ systems. If you're running a _Windows_ system, you may not run the automated _bash_ scripts to perform the installation. In such case, please check the listed dependencies from the list given down below and install them manually.

## Download the Project

The source code can be downloaded either by executing

```
git clone https://github.com/joonarafael/tiirascraper.git
```

or alternatively by downloading the project as a _ZIP_ archive (or _tar.gz_) from [this site](https://github.com/joonarafael/tiirascraper/releases "Tiirascraper Releases").

## Automated Dependency Installation

Install all required dependencies by executing the bash script

```
./setup.sh
```

located at root. Installation requires _sudo_ permissions.

**Remember**! Never execute unknown bash scripts on your machine! Before executing, read the content of the script first with

```
cat ./setup.sh
```

**Remember**! Execution rights for a bash script can be given with

```
chmod u+x script_name.sh
```

The `setup.sh` script will run the _Python_ file `./check.py` as the last step. It tries the importing of all necessary modules and raises exceptions if some of them are not available.

**If exceptions are raised**, read closely the details of the error and try to figure out which module is not working. Maybe the automated installation procedure failed to install it correctly? Has _pip_ worked without problems on your machine in the past?

## Manual Dependency Installation

If the `setup.sh` bash script does not work for you (or you are facing some other problems), you may also install the dependencies yourself by any alternative methods.

### Required Dependencies / Modules

- `beautifulsoup4`
- `requests`
- `schedule`

Always check the successful installation of dependencies with the `./check.py` Python file.
