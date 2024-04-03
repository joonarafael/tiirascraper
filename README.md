# TIIRASCRAPER (PYTHON WEB SCRAPER)

![main workflow](https://github.com/joonarafael/tiirascraper/actions/workflows/main.yml/badge.svg) [![codecov](https://codecov.io/gh/joonarafael/tiirascraper/graph/badge.svg?token=XCLKOTSKCW)](https://codecov.io/gh/joonarafael/tiirascraper)

Check the [Installation Manual](https://github.com/joonarafael/tiirascraper/blob/main/docs/installation_manual.md "Installation Manual") and the [User Manual](https://github.com/joonarafael/tiirascraper/blob/main/docs/user_manual.md "User Manual") before advancing further. Even with correct dependencies installed, the application will run into a runtime error if you do not set up the proper environment variables first.

## About

This is a simple web scraper software built with _Python_. Automated testing included as part of CI pipeline. Coverage report uploaded to [Codecov](https://app.codecov.io/gh/joonarafael/tiirascraper/tree/main/ "Codecov Coverage Report").

It fetches the _index_ page of a popular bird observation site [Tiira](https://www.tiira.fi/ "Tiira.fi") and parses the latest most interesting bird observation records.

The program also enables the ability to **create filters for individual cities and species**, so that any records without matching criteria will be disregarded.

In addition, the program supports automated _Telegram_ messaging feature. By configuring your own Telegram bot and applying relevant environment variables, **you can get the latest records straight to your Telegram**!

The program has been built to run "as a server"; it will automatically perform the procedure explained above every 5 minutes. It will read the configuration files and history again and check for a change on the site. The program also recovers from previous errors and e.g. unsuccessful connection attempts.
