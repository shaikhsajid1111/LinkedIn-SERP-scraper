'''
X-Ray (Scraping SERP) is a very useful tool to get the data you are looking for without actually having to visit the page. 
Use Bing to scrape about 50 linkedin urls. You should be able to see a Profile Card on the right if you use x-ray for a particular linkedin profile (attached). 
Use that card and parse it to get the person's current company and current title along with other possible data that you may see.
You might want to use parameters like "setmkt=en-US" in the search url to get the profile card on the right side.

Feel free to call me if you have any questions or need clarity/help. I am available at 7566691762. 



Input is essentially the linkedin url of a person. 
My objective is to find the latest work experience of that person. 
Check what suits best
'''
#import requests
#from selenium import webdriver
#from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from init import Initializer
from selenium.common.exceptions import WebDriverException,NoSuchElementException
import time
import json


class LinkedinSERP:
    def __init__(self,query,browser="firefox"):
        self.browser = browser
        self.query = f'site:linkedin.com/in {query.split("/")[-1]}'
        self.URL = f"https://www.bing.com/search?q={self.query}&setmkt=en-US"
        self.driver = ''
    
    def __start_driver(self):
       """changes the class member driver value to driver on call"""
       self.driver = Initializer(self.browser).init()

    def __dispose_driver(self):
        """closes the driver instance"""
        self.driver.close()
        self.driver.quit()

    def __css_selector_or_none(self,selector,find_inside_element=None):
        """find element using CSS selector and returns text out of it,if fails returns 'Not Found!'
            if element is not found it returns, 
            if element is found, it returns text of the element that havw been found
        """
        try:
            #if find element is None and find element is not string, it means
            if find_inside_element is None:
                return self.driver.find_element_by_css_selector(selector).text
            elif type(find_inside_element) is str:
                return "Not Found"
            else:
                return find_inside_element.find_element_by_css_selector(selector).text
        except NoSuchElementException:
            return "Not Found!"

    def __find_desc(self):
        """finds description of element, and returns its title attribute,if not returns "Not Found" 
        """
        try:
            return self.driver.find_element_by_css_selector(".spl-spli-desc > span").get_attribute('title')
        except NoSuchElementException:
            return "Not Found"

    def scrap(self):
        """scraps the data from card"""
        self.__start_driver()           #initialize the driver, this creates an instance of webdriver.browser()
        
        self.driver.get(self.URL)   #navigate to the URL
        
        #wait until elements load that element with class .b_caption is visible
        WebDriverWait(self.driver, 45).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.b_caption')))
        try:
            #wait again to check if there is element with h2 tag and class b_entityTitle
            WebDriverWait(self.driver, 45).until(EC.presence_of_element_located((By.CSS_SELECTOR,'h2.b_entityTitle')))
            WebDriverWait(self.driver, 45).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.spl-spli-ftl-tit')))
            
            #time.sleep(5) #for browser not loading quickly, mostly old machine's browser, they take time to render pages, so waiting 5 seconds is sufficient for them
        except WebDriverException:
            #in case if the try block element is not found, it means card did not appear
            self.driver.close() #close the current tab  
            self.driver.quit()  #quit firefox means, create entire process of firefox
            return json.dumps({"error":"Card did not appeared!"})
        
        name = self.__css_selector_or_none('.spl-spli-ftl-tit > h2')
        profession = self.__css_selector_or_none(".spl-spli-ftl-prof") #current profession of a person
        bio = self.__find_desc()

        #scraping through experience and education section
        experience_company = self.__css_selector_or_none(".spl-spli-dg-group-head-data") 
        experience_profession = self.__css_selector_or_none(".splm-spli-dg-group-prp-highlight")
        tenure = self.__css_selector_or_none(".spl-spli-dg-group-prp > span.b_demoteText")
        try:
            education = self.driver.find_elements_by_css_selector(".spl-spli-dg-group")
            #len of experience and education must be 3, for education and experience to available
            if len(education) > 2:
                education = education[-1]
            elif len(education) <= 2:
                education = ''
        except NoSuchElementException:
            education = ''

        institute = self.__css_selector_or_none("a.spl-spli-dg-group-prp",education) #find element inside element thats why passing education variable
        course = self.__css_selector_or_none("div.splm-spli-dg-group-prp-highlight",education)
        course_tenure = self.__css_selector_or_none(".spl-spli-dg-group-prp > span.b_demoteText",education)
        
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
        self.__dispose_driver()
        return json.dumps(data)

        


ln = LinkedinSERP('https://www.linkedin.com/in/jim-tuccillo-02378a6')
print(ln.scrap())

























#try:
#    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#    URL = "https://www.bing.com/search?q=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fbrett&qs=n&form=QBRE&sp=-1&pq=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fbrett&sc=0-33&sk=&cvid=52A121142D6748FD8F800B9362E0161B&setmkt=en-US"
#    URL = "https://www.bing.com/search?q=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fghoshkoushik&qs=n&form=QBRE&sp=-1&pq=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fghoshkoushik&sc=1-40&sk=&cvid=7B2B6D9B0915488685818377717B5114&setmkt=en-US"
#    driver.get(URL)
#    
#    #WebDriverWait(driver,45).until(EC.presence_of_element_located((By.CLASS_NAME,'b_caption')))
#    WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.b_caption')))
#    
#    name = driver.find_element_by_css_selector(".b_entityTitle")
#    position = driver.find_elements_by_css_selector(".b_entitySubTitle")
#    desc = driver.find_element_by_css_selector(".spl-spli-desc > span")
#
#
#    pos = [elem.text for elem in position]
#    names = name.text    
#    print(desc.get_attribute("title"))
#
#    driver.close()
#    driver.quit()
#
#    print(pos,names)
#except Exception as ex:
#    print(ex)

