from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

values= []

def setup(url):
    #editing this file 
    driver = webdriver.Chrome('/usr/bin/google-chrome')
    url = 'https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference'
    driver.get(url)

    # loading for a css selector
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#MathJax-Element-1-Frame")))

    page_source = driver.page_source

    driver.quit()

    soup = BeautifulSoup(page_source, "html.parser")
    return soup;

#scraping for math script

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

def scrape_ord(soup):
    return_value = False
    found = soup.find('script', attrs = {'id': 'MathJax-Element-1'});

    if (found is not None):
        return_value = True
        for math in found:
            values.append(math)
            print('ELEMENT FOUND' + math)


    return return_value
#for multiple elements?

def getValues():
    return values;


    