import time
from pages.base_page import BasePage
from utils import locators
from utils import testcase_data
from utils.openpyxlfunction import *
import pathlib


class JobSearch(BasePage):
    def __init__(self, driver):
        self.locator = locators.Bdjobs
        super(JobSearch, self).__init__(driver)

    def go_to_website(self):
        self.driver.get("https://bdjobs.com/")

    def close_ad(self):
        try:
            self.click(*self.locator.advertisement)
        except:
            print("no advertisement found")

    def searchquery(self):
        self.find_element2(*self.locator.searchField).send_keys(testcase_data.searchkeyword)
        time.sleep(5)
        self.click(*self.locator.clickSearchButton)
        time.sleep(5)
        child = self.driver.window_handles[1]
        self.driver.switch_to.window(child)

    def filter(self,data):
        data2 = testcase_data.RequiredParameter.split(",")
        print(data2)
        print(data[0])
        print(data2[0])
        print(data2[1])
        if str(data2[0]).lower() in str(data[0]).lower() or str(data2[1]).lower() in str(data[0]).lower():
            filepath = pathlib.Path(__file__).parent.parent / f"utils/{testcase_data.filename}"
            sheetname = testcase_data.bdjobsheet
            writecolautomatic(filepath, sheetname,data)

    def search_result(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)
        singleJob = self.driver.find_elements(*self.locator.alljobPost)
        print(singleJob)
        print(f"this len of singlejob {len(singleJob)}")
        for job in singleJob:
            title = job.find_element(*self.locator.titleName).text
            companyname = job.find_element(*self.locator.companyName).text
            location = job.find_element(*self.locator.location).text
            experience = job.find_element(*self.locator.Experience).text
            deadline = job.find_element(*self.locator.deadline).text
            url = job.find_element(*self.locator.url_locator).get_attribute('href')
            print(title)
            print(companyname)
            print(location)
            print(experience)
            print(deadline)
            print(url)
            data = [title, companyname, location, experience, "Deadline"+deadline, url]
            self.filter(data)

    def bdjob(self):
        self.go_to_website()
        time.sleep(5)
        self.close_ad()
        time.sleep(5)
        self.searchquery()
        self.search_result()
