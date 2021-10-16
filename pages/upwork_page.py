import time
from pages.base_page import BasePage
from utils import locators
from utils import testcase_data
from utils.openpyxlfunction import *
import pathlib
import pages.signin_page
import requests
from bs4 import BeautifulSoup


class UpworkSearch(BasePage):
    def __init__(self, driver):
        self.locator = locators.Upwork
        self.filepath = pathlib.Path(__file__).parent.parent / f"utils/{testcase_data.filename}"
        self.sheetname = testcase_data.upworkjobsheet
        super(UpworkSearch, self).__init__(driver)

    def sign_in_upwork(self):
        self.find_element2(*self.locator.email).send_keys(testcase_data.account)
        self.click(*self.locator.continue_to_password)
        time.sleep(15)
        self.find_element2(*self.locator.password).send_keys(testcase_data.password)
        self.find_element2(*self.locator.login).click()

    def go_to_website(self):
        self.driver.get("https://www.upwork.com/ab/account-security/login")

    def close_ad(self):
        try:
            self.click(*self.locator.advertisement)
            self.click(*self.locator.form_cancel_btn)
        except:
            print("no advertisement found")

    def searchquery(self):
        self.find_element2(*self.locator.search_button).send_keys(testcase_data.searchkeyword)
        time.sleep(2)
        self.click(*self.locator.search_button)
        time.sleep(2)

    def filter(self, data):
        data2 = testcase_data.RequiredParameter.split(",")
        if str(data2[0]).lower() in str(data[0]).lower() or str(data2[1]).lower() in str(data[0]).lower():
            writecolautomatic(self.filepath, self.sheetname, data)

    def search_result(self):
        # self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)
        self.close_ad()
        singleJob = self.driver.find_elements(*self.locator.all_job_post)
        print(singleJob)
        print(f"this len of singlejob {len(singleJob)}")
        for job in singleJob:

            try:
                self.wait_till_visibility_of_element_located(2, self.locator.titleName)
                title = job.find_element(*self.locator.titleName).text
            except:
                title = "No data found"

            try:
                self.wait_till_visibility_of_element_located(2, self.locator.job_nature)
                jobnature = job.find_element(*self.locator.job_nature).text
            except:
                jobnature = "No data found"

            try:
                self.wait_till_visibility_of_element_located(2, self.locator.location)
                location = job.find_element(*self.locator.location).text
            except:
                location = "no data found"

            try:
                self.wait_till_visibility_of_element_located(2, self.locator.Experience)
                experience = job.find_element(*self.locator.Experience).text
            except:
                experience = "No data found"

            try:
                self.wait_till_visibility_of_element_located(2, self.locator.url_locator)
                url = job.find_element(*self.locator.url_locator).get_attribute('href')
            except:
                url = "No data found"
            job.click()

            try:
                self.wait_till_visibility_of_element_located(2, self.locator.connection)
                connection = job.find_element(*self.locator.Experience).text
            except:
                connection = "No data found"

            print(title)
            print(jobnature)
            print(location)
            print(experience)
            print(url)
            data = [title, "Connection", jobnature, experience, "Hourly Rate", url]
            self.filter(data)


    def Upwork(self):

        self.go_to_website()
        time.sleep(2)
        self.sign_in_upwork()
        time.sleep(2)
        self.searchquery()
        self.search_result()

