# SOFTWARE REQUIREMENTS SPECIFICATION

## General

Build a simple web scraper. Fetch recently published bird observation records from [Tiira](https://www.tiira.fi/ "Tiira.fi") and filter the records against predetermined configuration files.

The configuration files include lists for allowed cities and species. Only records with a whitelisted city and species will get through the filtering process.

After the initial filtering against configs, check history. If a record already exists in history, it can be safely discarded. History will reset every 24 hours.

New observations that match the configuration criteria and do not already appear in the history, should be then sent via _Telegram_ to specific recipients.

## Technical Details

Software will be built with _Python_.

The software will be built specifically around the [Tiira](https://www.tiira.fi/ "Tiira.fi") front page and its observation records table. The URL and _HTML_ parsing logic will be hardcoded into the software.

Only the driver code and general logic for the Telegram messaging service will be available, users need to configure their own bots to actually utilize this functionality.

The software will be built as an "server" program, it runs indefinitely and performs the fetching and parsing procedure every 5 minutes to check for changes at the source site.

There will not be a ready `.exe` file or pretty website for the program, only the source code will be available and a fair bit of technical know-how is required to get the program up and running. Extensive installation manual and user manual is provided, of course.
