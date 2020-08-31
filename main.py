from selenium import webdriver
from time import sleep
from secrets import pw


class InstaBot:
    def __init__(self, username, pw):
        self.username = username

        # START LOGIN PROCESS
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        # wait for the page to load the DOM
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        # wait for the page to load the DOM
        sleep(4)
        # instagram ask if you want to save login, no clicked
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        # wait for the page to load the DOM
        sleep(2)
        # instagram ask if you want ot turn notification on, no click
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)

        # END LOGIN PROCESS
    
    def get_unfollowers(self):

        # go to the profiles page
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()

        # wait for the page to load
        sleep(2)

        #Get a list of people you are following
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()

        # get a list of followers
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()

 

my_bot = InstaBot('pieter.vankatwijk',pw)
my_bot.get_unfollowers()