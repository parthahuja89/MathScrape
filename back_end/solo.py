from bs4 import BeautifulSoup
from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

values= []

"""
Scraping scripts using the css_selector
"""


def setup(url , css_selector):
    #works 
    pass
    print(url)
    chrome_bin = os.environ.get('GOOGLE_CHROME_SHIM', None)
    opts = ChromeOptions()
    opts.binary_location = chrome_bin
    driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=opts)
    driver.get(url)

    # loading for a css selector
    wait = WebDriverWait(driver, 10)
    print('css selctor is:'+ css_selector)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))

    page_source = driver.page_source

    driver.quit()

    soup = BeautifulSoup(page_source, "html.parser")
    print(soup)
    return soup;

#Brute forcing all possible attributes 
def scrape_a(soup):
    return_value = False;
    found = soup.find('script', attrs={'type':'math/tex; mode=display'});
    if(found is not None):
       return_value = True;
       for math in found:
          values.append(math)
          print('ELEMENT FOUND' + math)


    return return_value

def scrape_1(soup):
    return_value = False;
    found = soup.find('script', attrs = {'id': 'MathJax-Element-a'});
    if (found is not None):
        return_value = True;
        for math in found:
            values.append(math)
            print('ELEMENT FOUND' + math)

    return return_value

def scrape_ord(soup , tag):
    return_value = False
    found = soup.find('script', attrs = {'id': tag});

    if (found is not None):
        return_value = True
        for math in found:
            values.append(math)
            print('ELEMENT FOUND' + math)


    return return_value
#for multiple elements?

def getValues():
    return values;
