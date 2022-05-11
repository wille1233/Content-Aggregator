
# Content Aggregator

## Description

This program scrapes data from a website. Mainly made for news. Send the data to optional mail or save to a txt file.

## Built with

- Python

## Requirements/Prerequisites

- Python 3.7+
- Requests
- BeautifulSoup4
- lxml
- datetime
- smtplib
- email.message
Email function requires an smtp enabled email account, add to code.

## Installation

This project has been tested on Python 3.7+. To install Python you can visit 
(https://www.python.org/downloads/)

1. Clone Git Repository
```cmd
    git clone https://github.com/wille1233/Content-Aggregator
```
2. Install Requests
```cmd
    pip install Requests
```
3. Install bs4
```cmd
    pip install bs4
```
4. Install lxml
```cmd
    pip install lxml
```
5. Install datetime
```cmd
    pip install datetime
```
6. Install smtplib
```cmd
    pip install smtplib
```
7. Install email.message
```cmd
    pip install email.message
```
7. Add mail account information to Main.py(Optional)
```
    line 45-46
```

## Code conventions

### Standrads:
- PEP8
- Docstrings

## Usage

This project can be used for getting news without searching on the webb.

## Example

https://github.com/wille1233/Content-Aggregator/issues/1#issue-1232525345

## To do/Roadmap

- [x] Create readme
- [X] Get requests to work
- [ ] Improve visuals
- [ ] Languages 
    - [ ] Swedish
    - [X] English

## Changelog

### Version 1.0.1

#### Added or Changed

- Added request 
- Made a simple web scraper

### Version 1.0.2

#### Added or Changed

- Used lxml to filter out paragraphs
- Improved code

### Version 1.0.3

#### Added or Changed

- Added the save to txt file function
- Added a check_request function

### Version 1.0.4

#### Added or Changed

- Added a Menu
- Date to txt file 
- Choose website function

### Version 1.0.5

#### Added or Changed

- Added mail function

#### Removed

- Removed previous website chooser function and made a improved new one

## Contribution

As this assessment has not yet been handed in, no pull requests are allowed. As soon as an assessment has been handed in, this will be allowed.

In the event of major changes, I want an issue to be opened up for discussion about what should be changed.

Då bedömning ännu ej är gjord på uppgiften så tillåts inga pull requests. Så fort bedömning är gjord kommer detta tillåtas.  

Vid större förändringar önskar jag att en issue öppnas för diskussion om vad som ska förändras.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contact


William Eriksson - officiellawilliam@gmail.com

Projectlink: https://github.com/wille1233/content-aggregator

## Acknowledgments

- [Images to ReadMe](https://www.youtube.com/watch?v=nvPOUdz5PL4)
- [Python Send Mail](https://www.youtube.com/watch?v=BsVQ_cBmEwg&t=438s)
- Dan Hermansson
