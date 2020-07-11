from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.implicitly_wait(3)

driver.get("file:///C:/Users/admin/Desktop/eshop/eshop/index.html")

driver.maximize_window()

driver.close