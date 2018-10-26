# HRSscraper

A Python web scraper for downloading HTML content from the [Hawaii Revised Statutes](https://www.capitol.hawaii.gov/hrscurrent/) as provided by the Hawaii State Legislature.

## Requirements

- [Requests](https://pypi.org/project/requests/)

  ```
  pip install requests
  ```

- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)

  ```
  pip install beautifulsoup4
  ```

## Usage

HRSscraper is configured to run from the terminal via the Mac OS X Python interpreter:

```
#! /usr/bin/env python3
```

If you wish to run the application on Windows or Linux, modify the first line of `HRSscraper.py` according to the requirements of your operating system. Alternatively, run `HRSscraper.py` directly from Python's IDLE.

Once started, the application will create a `/data` directory to store the downloaded and processed HTML files. The process may take approximately 2 hours to complete, depending on your system and network connection.

The repository also includes a `/_data` directory that already contains all of the HTML files obtained from the Hawaii State Legislature's website (current as of Friday, October 26, 2018).

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.
