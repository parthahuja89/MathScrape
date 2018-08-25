from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get("https://www.mathjax.org/#samples")

#loading for a css selector
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#MathJax-Element-1-Frame")))


page_source = driver.page_source

driver.quit()



soup = BeautifulSoup(page_source, "html.parser")
script = soup.findAll("script")
print(script)

#scraping for math script



for math in soup.find('script', attrs={'type':'math/tex; mode=display'}):
    print('ELEMENT FOUND' + math)

for normal in soup.find('script', attrs = {'id': 'MathJax-Element-a'}):
    print('ELEMENT FOUND' +normal)

for elements in soup.find('script', attrs = {'id': 'MathJax-Element-1'}):
    print('ELEMENT FOUND' + elements)

#for multiple elements?
