import time
from pages.base_page import BasePage
from utils import locators
from utils import testcase_data
from utils.openpyxlfunction import *
import pathlib
import requests
from bs4 import BeautifulSoup


class MonsterSearch(BasePage):
    def __init__(self, driver):
        self.locator = locators.MonsterLocator
        self.filepath = pathlib.Path(__file__).parent.parent / f"utils/{testcase_data.filename}"
        self.sheetname = testcase_data.monsterjobsheet
        super(MonsterSearch, self).__init__(driver)

    def go_to_website(self):
        self.driver.get("https://www.monster.com/")

    def close_ad(self):
        try:
            self.click(*self.locator.advertisement)
            self.click(*self.locator.form_cancel_btn)
        except:
            print("no advertisement found")

    def searchquery(self):
        self.find_element2(*self.locator.SearchField).send_keys(testcase_data.searchkeyword)
        time.sleep(2)
        self.click(*self.locator.SearchButton)
        time.sleep(2)

    def filter(self, data):
        data2 = testcase_data.RequiredParameter.split(",")
        if str(data2[0]).lower() in str(data[0]).lower() or str(data2[1]).lower() in str(data[0]).lower():
            writecolautomatic(self.filepath, self.sheetname, data)

    def search_result(self):
        # self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)
        self.close_ad()
        singleJob = self.driver.find_elements(*self.locator.alljobpost)
        print(singleJob)
        print(f"this len of singlejob {len(singleJob)}")
        for job in singleJob:
            # job.click()
            time.sleep(5)
            try:
                self.wait_till_visibility_of_element_located(2, self.locator.titleName)
                title = job.find_element(*self.locator.titleName).text
            except:
                title = "No data found"
            try:
                self.wait_till_visibility_of_element_located(2, self.locator.companyName)
                companyname = job.find_element(*self.locator.companyName).text
            except:
                companyname = "No data found"
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
            try:
                self.wait_till_visibility_of_element_located(2, self.locator.deadline)
                deadline = job.find_element(*self.locator.deadline).text
            except:
                deadline = "No data found"

            print(title)
            print(companyname)
            print(location)
            print(experience)
            print(deadline)
            print(url)
            data = [title, companyname, location, experience, deadline, url]
            self.filter(data)

    def page(self, page_number):
        pagelocator = self.locator.pagination(page_number)
        return pagelocator

    def pagination(self):
        for i in range(2, 10):
            pagelocator = self.find_element2(*self.page(i))
            if pagelocator.is_displayed:
                pagelocator.click()
                time.sleep(10)
                self.search_result()
            else:
                print("problem")
                data = ["end of data" * 4]
                writecolautomatic(self.filepath, self.sheetname, data)
                self.filter(data)
                break

    def monster_search(self):
        self.go_to_website()
        time.sleep(2)
        self.close_ad()
        time.sleep(2)
        self.searchquery()
        self.search_result()
