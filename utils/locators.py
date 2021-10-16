from selenium.webdriver.common.by import By


class SignInPageLocator(object):
    email = (By.XPATH, '//*[@id="email"]')
    password = (By.XPATH, '//*[@id="pass"]')
    signInBtn = (By.XPATH, '//button[@data-testid="royal_login_button"]')


class common_locators(object):
    def pagination(page_number):
        page_locator = (By.XPATH, f"//a[contains(text(),'{page_number}')]")
        return page_locator


class Bdjobs(object):
    advertisement = (By.XPATH, '//img[@title="Close"]')
    searchField = (By.XPATH, "//input[@id='txtKeyword']")
    clickSearchButton = (By.XPATH, '//input[@type="submit"]')
    alljobcontainer = (By.XPATH, '//div[@aria-label="browse jobs section"]')
    alljobPost = (By.XPATH, './/*[@class="norm-jobs-wrapper"]')
    titleName = (By.XPATH, './/div[@class="job-title-text"]')
    companyName = (By.XPATH, './/div[@class="comp-name-text"]')
    location = (By.XPATH, './/div[@class="locon-text-d"]')
    Experience = (By.XPATH, './/div[@class="exp-text-d"]')
    deadline = (By.XPATH, './/div[@class="dead-text-d"]')
    url_locator = (By.XPATH, './/div[@class="job-title-text"]//a')


class BaytLocator(object):
    advertisement = (By.XPATH, '//a[@class="modal-close is-attached is-outer d"]')
    form_cancel_btn = (By.XPATH, "//button[contains(text(),'Cancel')]")
    SearchField = (By.XPATH, '//input[@id="text_search"]')
    SearchButton = (By.XPATH, '//button[@type="submit"]')
    alljobpost = (By.XPATH, '//li[@class="has-pointer-d"]')
    titleName = (By.XPATH, './/a[@data-js-aid="jobID"]')
    companyName = (By.XPATH, './/b[@class="p10r"]')
    location = (By.XPATH, '//ul[@class="list is-basic t-small"]//span')
    Experience = (By.XPATH, '/html[1]/body[1]/div[4]/section[1]/div[2]/div[1]/div[1]/div[2]/dl[2]/div[2]/dd[1]')
    deadline = (By.XPATH, '')
    url_locator = (By.XPATH, './/a[@data-js-aid="jobID"]')

    def pagination(page_number):
        page_locator = (By.XPATH, f"//a[contains(text(),'{page_number}')]")
        return page_locator


class DiceLocator():
    advertisement = (By.XPATH, '//a[@class="modal-close is-attached is-outer d"]')
    form_cancel_btn = (By.XPATH, "//button[contains(text(),'Cancel')]")
    SearchField = (By.XPATH, '//input[@id="typeaheadInput"]')
    SearchButton = (By.XPATH, "//button[@id='submitSearch-button']")
    alljobpost = (By.XPATH, '//dhi-search-card[@data-cy="search-card"]')
    titleName = (By.XPATH, './/a[@data-cy="card-title-link"]')
    companyName = (By.XPATH, './/a[@data-cy="search-result-company-name"]')
    location = (By.XPATH, './/span[@id="searchResultLocation"]')
    Experience = (By.XPATH, '')
    deadline = (By.XPATH, '//span[@data-cy="card-posted-date"]')
    url_locator = (By.XPATH, './/a[@data-cy="card-title-link"]')

    def pagination(page_number):
        page_locator = (By.XPATH, f"//a[contains(text(),'{page_number}')]")
        return page_locator

class Upwork():
    email = (By.XPATH, "//input[@id='login_username']")
    continue_to_password = (By.XPATH, "//button[@id='login_password_continue']")
    password = (By.XPATH, "//input[@id='login_password']")
    login = (By.XPATH, "//button[@id='login_control_continue']")
    search_box = (By.XPATH, "//input[@id='search-box-el']")
    search_button = (By.XPATH, '//label[@class="input-group-btn"]')
    all_job_post = (By.XPATH, '//section[@class="job-tile air-card-hover m-0-top ng-scope"]')
    titleName = (By.XPATH, './/h4[@class="job-title m-0 p-sm-right ng-isolate-scope"]//a')
    job_nature = (By.XPATH, './/span[@data-job-type="::jsuJobTileMediumController.job"]')
    connection = (By.XPATH, "//body/up-c-slider[@id='job-details-slider']/div[1]/nuxt-job-details-loader[1]/div[1]/div[1]/div[1]/div[1]/div[2]/aside[1]/div[1]/div[2]/div[1]/div[1]/span[2]")
    Experience = (By.XPATH, './/span[@data-job-tier="::jsuJobTileMediumController.job"]')
    hourly_rate = (By.XPATH, '//span[@data-cy="card-posted-date"]')
    url_locator = (By.XPATH, './/h4[@class="job-title m-0 p-sm-right ng-isolate-scope"]//a')

class MonsterLocator():
    advertisement = (By.XPATH, '')
    form_cancel_btn = (By.XPATH, "")
    SearchField = (By.XPATH, '//body[1]/div[1]/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/label[1]/div[1]/input[1]')
    SearchButton = (By.XPATH, '(//button[@role="button"])[2]')
    alljobpost = (By.XPATH, '//div[@class="results-card "]')
    titleName = (By.XPATH, './/div[@class="title-company-location"]//a')
    companyName = (By.XPATH, './/h3[@name="card_companyname"]')
    location = (By.XPATH, './/span[@name="card_job_location"]')
    Experience = (By.XPATH, )
    deadline = (By.XPATH, './/div[@name="datePostedMeta"]')
    url_locator = (By.XPATH, './/div[@class="title-company-location"]//a')
