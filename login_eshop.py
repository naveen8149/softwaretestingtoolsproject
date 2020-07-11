from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.implicitly_wait(3)

driver.get("file:///C:/Users/admin/Desktop/eshop/eshop/index.html")

driver.maximize_window()

driver.find_element(By.XPATH, "/html/body/div/div[2]/nav/ul/li[3]/a").click()

driver.find_element(By.ID, "inputEmail").send_keys("uday@gmail.com")

driver.find_element(By.ID, "inputPassword").send_keys("Hyderabad@123")

time.sleep(2)

driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div/div/div[2]/form/button").click()

time.sleep(3)

driver.quit()
