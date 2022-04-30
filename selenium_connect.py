from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from action import Action
import time
import os
import dotenv
from selenium.webdriver.common.by import By

# load enviroment variables
dotenv.load_dotenv()

action = Action()

options = webdriver.ChromeOptions()
ser = Service(os.getenv("chrmoedriver_path"))  # Path to chrmoedriver
options.add_argument("user-data-dir=" + os.getenv("google_chrome_profile_path"))  # Path to your chrome profile
driver = webdriver.Chrome(service=ser, options=options)

executor_url = driver.command_executor._url
session_id = driver.session_id
action.save_session_in_file(executor_url, session_id)
driver.implicitly_wait(10)

# print(executor_url)
# print(session_id)

driver.get("https://www.google.com/")
time.sleep(1)

driver.get(os.getenv("playlist"))

driver.find_element(By.XPATH, '//*[@aria-label="Lista aleatoria"]').click()
driver.find_element(By.XPATH, '//*[@class="ytp-next-button ytp-button"]').click()
tab = driver.current_window_handle

action.save_browser_tabas(tab, "_", "_")
