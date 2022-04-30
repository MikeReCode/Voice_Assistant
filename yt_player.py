from selenium.webdriver.common.by import By
from action import Action
import os


class Yt_music:

    def __init__(self, driver):
        self.driver = driver
        self.action = Action()

    def music(self):
        # open YouTube playlist
        os.system('python selenium_connect.py')

    def close(self):
        self.driver.quit()

    def next_song(self):
        self.driver.find_element(By.XPATH, '//*[@class="ytp-next-button ytp-button"]').click()

    def pause_play_music(self):       
        self.driver.find_element(By.XPATH, '//*[@class="ytp-play-button ytp-button ytp-play-button-playlist"]').click()
