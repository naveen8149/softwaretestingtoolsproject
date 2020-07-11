from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.implicitly_wait(3)

driver.get("file:///C:/Users/admin/Desktop/eshop/eshop/index.html")

driver.maximize_window()

target = driver.find_element(By.XPATH, "/html/body/div/div[5]/div/div/div/div/div/div[1]/div/div[2]/div[3]/a")

time.sleep(2)

actions = ActionChains(driver)
actions.move_to_element(target)
actions.perform()
