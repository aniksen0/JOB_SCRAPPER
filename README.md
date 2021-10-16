# Facebook automation tools

## Installation
##### Use the package manager pip to install project dependency

    $ cd to the directory where requirements.txt is located
    $ run: pip3 install -r requirements.txt


## Run Project

    $ cd to the "functionality" directory
    $ run: python3 testconf/runtest.py


## Run individual testcase

 ##### run test using unittest

    $ cd to the "functionality" directory
    $ python3 -m unittest TestCase.TC_file_name (without.py)
    
##### run test with allure report

    $ cd to the "functionality" directory
    $ python -m pytest -s functonality/TC_file_name.py --alluredir=ReportAllure &&  allure serve ReportAllure/

# Python-Selenium-auto-job-listing-with-keyword
A Python script use Selenium to achieve automatically listing all the jobs from various job posting site in a single excel file .

Setup
----------
 - First of all, install [Python 3](https://www.python.org/downloads/) into your machine
 
 - Then insall selenium:
   ```
   pip install selenium
   ```
 - Download the [Chrome Driver](http://chromedriver.chromium.org/downloads) and place it in the same directory with the script.
 
Configure the script
----------
You need to edit the script to provide your search keyword on tescase_data file under utils folder
 
After that, run the script by double click on it. Enjoy!

###extended configuration