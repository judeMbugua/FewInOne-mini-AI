from selenium import webdriver
from selenium.webdriver.edge.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

url = 'https://www.google.com'

search = input("Enter your search: ")



options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
options.add_argument('log-level=3')
driver = webdriver.Edge(r"C:\Users\judew\Documents\code projects\python\sel\msedgedriver.exe",options=options)


driver.get(url)
wait = WebDriverWait(driver, 10)
searchBar = wait.until(EC.presence_of_element_located((By.NAME, 'q'))).send_keys(search)
send =driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]').submit()

driver.maximize_window()
