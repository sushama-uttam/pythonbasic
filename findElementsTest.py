import time

from selenium import webdriver
from chromatic import chromatic
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\Sushama Chavan\\Desktop\\chromedriver.exe")
driver.get("https://www.makemytrip.com/")
time.sleep(10)
chromatic = chromatic(projectToken="YOUR_CHROMATIC_PROJECT_TOKEN")

driver.find_element(By.ID,"fromCity").click()
driver.find_element(By.CSS_SELECTOR,"input[placeholder='From']").send_keys("del")
time.sleep(2)
driver.save_screenshot("a.png")
cities =driver.find_element(By.CSS_SELECTOR,"p[class*='blackText']")
for city in cities:
    if city.text =="Del Rio, United States":
        city.click()
        break


driver.find_element(By.XPATH,"//p[text()='Delhi, India']").click()



