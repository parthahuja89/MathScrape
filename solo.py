from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.mathjax.org/#samples")

#loading for a css selector
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#samples > h4:nth-child(4)")))


page_source = driver.page_source

driver.close()


soup = BeautifulSoup(page_source, "html.parser")
script = soup.findAll("script")
print(script)

#scraping for math script



for math in soup.find('script', attrs={'type':'math/tex; mode=display'}):
    print(math)


#adding pandas?