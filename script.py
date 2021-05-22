#!/usr/bin/env python3

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from init import Initializer
from selenium.common.exceptions import TimeoutException, WebDriverException,NoSuchElementException
import time
import json
from random import randint
import argparse

class LinkedinSERP:
    def __init__(self,browser="firefox"):
        self.browser = browser
        self.driver = ''

    def __start_driver(self):
       """changes the class member driver value to driver on call"""
       self.driver = Initializer(self.browser).init()

    def __dispose_driver(self):
        """closes the driver instance"""
        self.driver.close()
        self.driver.quit()

    def __css_selector_or_not_found(self,selector,find_inside_element=None):
        """find element using CSS selector and returns text out of it,if fails returns 'Not Available on card!'
            if element is Not Available on card it returns,
            if element is found, it returns text of the element that havw been found
        """
        try:
            #if find element is None and find element is not string, it means
            if find_inside_element is None:
                return self.driver.find_element_by_css_selector(selector).text
            elif type(find_inside_element) is str:
                return "Not Available on card"
            else:
                return find_inside_element.find_element_by_css_selector(selector).text
        except NoSuchElementException:
            return "Not Available on card!"

    def __find_desc(self):
        """finds description of element, and returns its title attribute,if not returns "Not Available on card"
        """
        try:
            return self.driver.find_element_by_css_selector(".spl-spli-desc > span").get_attribute('title')
        except NoSuchElementException:
            return "Not Available on card"

    def __navigate(self,URL):
        if self.driver == "":
            self.__start_driver() #initialize the driver, this creates an instance of webdriver.browser()
        self.driver.get(URL)

    def scrap_multiple(self,list_of_profile):
        data = {}
        for URL in list_of_profile:
            time.sleep(randint(3,7))
            data[f"{URL}"] = self.scrap(URL,is_list=True)
        self.__dispose_driver()
        return data


    def scrap(self,URL,is_list=False):
        """scraps the data from card"""
        query = f'site:linkedin.com/in {URL.split("/")[-1]}'
        navigate_url = f"https://www.bing.com/search?q={query}&setmkt=en-US"
        self.__navigate(navigate_url)

        #wait until elements load that element with class .b_caption is visible
        try:
            WebDriverWait(self.driver, 45).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.b_caption')))
        except TimeoutException:
            if not is_list: #if theres a list then do not close the tab, just change the URL
                #close the current
                self.__dispose_driver()  #quit firefox means, create entire process of firefox
                return {"error":"Results itself did not appear"}
            return {"error":"Results itself did not appear"}

        try:
            #wait again to check if there is element with h2 tag and class b_entityTitle
            WebDriverWait(self.driver, 45).until(EC.presence_of_element_located((By.CSS_SELECTOR,'h2.b_entityTitle')))
            WebDriverWait(self.driver, 45).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.spl-spli-ftl-tit')))

            time.sleep(2) #for browser not loading quickly, mostly old machine's browser, they take time to render pages, so waiting 5 seconds is sufficient for them
        except WebDriverException:
            #in case if the try block element is Not Available on card, it means card did not appear
            if not is_list: #if theres a list then do not close the tab, just change the URL
                #close the current
                self.__dispose_driver()  #quit firefox means, create entire process of firefox
                return {"error":"Card did not appeared!"}
            return {"error":"Card did not appeared!"}
        except TimeoutException:
            if not is_list: #if theres a list then do not close the tab, just change the URL
                #close the current
                self.__dispose_driver()  #quit firefox means, create entire process of firefox
                return {"error":"Card did not appeared!"}
            return {"error":"Results itself did not appear"}

        name = self.__css_selector_or_not_found('.spl-spli-ftl-tit > h2')
        profession = self.__css_selector_or_not_found(".spl-spli-ftl-prof") #current profession of a person
        bio = self.__find_desc()

        #scraping through experience and education section
        experience_company = self.__css_selector_or_not_found(".spl-spli-dg-group-head-data")
        experience_profession = self.__css_selector_or_not_found(".splm-spli-dg-group-prp-highlight")
        tenure = self.__css_selector_or_not_found(".spl-spli-dg-group-prp > span.b_demoteText")
        try:
            education = self.driver.find_elements_by_css_selector(".spl-spli-dg-group")
            #len of experience and education must be 3, for education and experience to available
            if len(education) > 2:
                education = education[-1]
            elif len(education) <= 2:
                education = ''
        except NoSuchElementException:
            education = ''

        institute = self.__css_selector_or_not_found("a.spl-spli-dg-group-prp",education) #find element inside \
        #element thats why passing education variable
        course = self.__css_selector_or_not_found("div.splm-spli-dg-group-prp-highlight",education)
        course_tenure = self.__css_selector_or_not_found(".spl-spli-dg-group-prp > span.b_demoteText",education)

        data = {
            "name" : name,
            "bio" : bio,
            "profession" : profession,
            "experience" : {
                "company" : experience_company,
                "experience_profession" : experience_profession,
                "tenure" : tenure
            },
            "education" : {
                "institute" : institute,
                "course" : course,
                "course_tenure" : course_tenure
            }
        }

        if not is_list:
            self.__dispose_driver() #close the browser and all its window
        return data #returns data in JSON format





def read_file(filename):
    URLS = list()
    with open(filename,'r',encoding='utf-8') as file:
        URLS.extend([line for line in file if line != '' and line != '\n'])
        file.close()
    return URLS



if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--filename",help="Input CSV File which contains all the linked URLs")
  parser.add_argument("--linkedin_url",help="Single LinkedIn Profile URL")
  args = parser.parse_args()
  filename = args.filename
  linkedin_url = args.linkedin_url
  scraper = LinkedinSERP()

  if filename is not None:
    URLS = read_file(filename)
    data = scraper.scrap_multiple(URLS)
  elif linkedin_url is not None:
    data = scraper.scrap(linkedin_url)
  else:
    print("Please try python3 script.py -h for help")
    exit()
  print(json.dumps(data))

















