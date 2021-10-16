import time
from pages.base_page import BasePage
from utils import locators
from utils import testcase_data
from utils.openpyxlfunction import *
import pathlib
import requests
from bs4 import BeautifulSoup


class PageFunctionality(BasePage):
    def __init__(self, driver):
        self.locator = locators.DiceLocator
        self.filepath = pathlib.Path(__file__).parent.parent / f"utils/{testcase_data.filename}"
        self.sheetname = testcase_data.bdjobsheet
        super(PageFunctionality, self).__init__(driver)

    def go_to_website(self, UrlLink):
        self.driver.get(UrlLink)

    def close_ad(self, *locator):
        try:
            self.click(*locator)
            self.click(*locator)
        except:
            print("no advertisement found")

    def searchquery(self, search_locator_input, data, search_locator_button):
        self.find_element2(*search_locator_input).send_keys(data)
        time.sleep(2)
        self.click(*search_locator_button)
        time.sleep(2)

    def filter(self, data):
        data2 = testcase_data.RequiredParameter.split(",")
        if str(data2[0]).lower() in str(data[0]).lower() or str(data2[1]).lower() in str(data[0]).lower():
            writecolautomatic(self.filepath, self.sheetname, data)

    def search_result(self,alljobpostLocator,titlename,company_name,joblocation,experience_required, url_locator,deadline_time):
        # self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)
        self.close_ad()
        singleJob = self.driver.find_elements(alljobpostLocator)
        print(singleJob)
        print(f"this len of singlejob {len(singleJob)}")
        for job in singleJob:
            try:
                self.wait_till_visibility_of_element_located(2, titlename)
                title = job.find_element(titlename).text
            except:
                title = "No data found"
            try:
                self.wait_till_visibility_of_element_located(2, company_name)
                companyname = job.find_element(company_name).text
            except:
                companyname = "No data found"
            try:
                self.wait_till_visibility_of_element_located(2,joblocation)
                location = job.find_element(*self.locator.location).text
            except:
                location = "no data found"
            try:
                self.wait_till_visibility_of_element_located(10, experience_required)
                experience = job.find_element(experience_required).text
            except:
                experience = "No data found"
            try:
                self.wait_till_visibility_of_element_located(2, url_locator)
                url = job.find_element(url_locator).get_attribute('href')
            except:
                url = "No data found"
            try:
                self.wait_till_visibility_of_element_located(2, deadline_time)
                deadline = job.find_element(deadline_time).text
            except:
                deadline = "No data found"

            print(title)
            print(companyname)
            print(location)
            print(experience)
            print(deadline)
            print(url)
            data = [title, companyname, location, experience, "Posted:" + deadline, url]
            self.filter(data)

    def page(self, page_number):
        pagelocator = self.locator.pagination(page_number)
        return pagelocator

    def pagination(self):
        for i in range(2, 6):
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

    def DiceJob(self):
        self.go_to_website("https://www.monster.com/")
        time.sleep(2)
        self.close_ad()
        time.sleep(2)
        self.searchquery()
        self.search_result()
        self.pagination()
