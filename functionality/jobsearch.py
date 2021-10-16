import sys, os
from pages.bdjobs_page import JobSearch
from functionality.base_test import BaseTest
from pages.bayt_page import BaytSearch
from pages.dice_page import DiceSearch
from pages.upwork_page import UpworkSearch
from pages.monster_page import MonsterSearch


class TestJobSearch(BaseTest):
    def test_job_search(self):
        # page = JobSearch(self.driver)
        # page.bdjob()
        # page1 = BaytSearch(self.driver)
        # page1.baytjob()
        # page2 = DiceSearch(self.driver)
        # page2.DiceJob()
        # page3= UpworkSearch(self.driver)
        # page3.Upwork()
        page4 = MonsterSearch(self.driver)
        page4.monster_search()
