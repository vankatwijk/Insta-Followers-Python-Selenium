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
        following = self._get_names()

        # get a list of followers
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self._get_names()

        
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

    def _get_names(self):
        sleep(2)


        # after click follower link, wait until dialog appear
        self.driver.find_element_by_css_selector('div[role="dialog"]')
        # now scroll - inject javascript to scroll
        self.driver.execute_script('''
        var fDialog = document.querySelector('div[role="dialog"] .isgrP');
        fDialog.scrollTop = fDialog.scrollHeight
        ''')
        # wait for the lazy loading to activate
        sleep(2)
        # select the scroll box
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        last_ht, ht = 0, 1
        # compare the height to trick lazy loading to load more content
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            # scroll more if the page has more content to load
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)

        # sugs = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul')
        # self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
        # sleep(2)
        # scroll_box = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[2]")
        # last_ht, ht = 0, 1
        # while last_ht != ht:
        #     last_ht = ht
        #     sleep(1)
        #     ht = self.driver.execute_script("""
        #         arguments[0].scrollTo(0, arguments[0].scrollHeight); 
        #         return arguments[0].scrollHeight;
        #         """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")\
            .click()
        return names


my_bot = InstaBot('pieter.vankatwijk',pw)
my_bot.get_unfollowers()
my_bot._get_names()