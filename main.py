from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

MY_EMAIL = "your_email"
PASSWORD = "your_password"
chrome_driver_path = "C:\\Users\\Hp EliteBook\\Desktop\\chrome Driver\\chromedriver.exe"

PROMISED_UP = 21.4
PROMISED_DOWN = 10.10


class InternetSpeedTwitterBot:
    def __init__(self, chrome_driver_path):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(5)
        go_button = self.driver.find_element_by_class_name('start-text')
        go_button.click()
        time.sleep(120)
        self.download_speed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div['
                                                           '2]/div[3]/div[3]/div/div[3]/div/div/div[2]/d'
                                                           'iv[1]/div[2]/div/div[2]/span').text
        print(f'down : {self.download_speed}')
        self.upload_speed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div['
                                                         '2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                         '3]/div/div[2]/span').text
        print(f'up : {self.upload_speed}')

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com')
        time.sleep(5)
        sign_in_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div['
                                                           '1]/div[1]/div/div[3]/div[5]/a/div/span')
        sign_in_button.click()
        time.sleep(5)
        email_button = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                         '2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                                                         '5]/label/div/div[2]/div/input')
        email_button.send_keys(MY_EMAIL)
        time.sleep(5)
        next_button = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                        '2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div/span/span')
        next_button.click()
        time.sleep(5)
        password_entry = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                           '2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                                                           '3]/div/label/div/div[2]/div[1]/input')
        password_entry.send_keys(PASSWORD)
        time.sleep(1)
        password_entry.send_keys(Keys.ENTER)

        tweet_compose = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div['
            '2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed  {self.download_speed} down/{self.upload_speed}up when I pay for " \
                f"{PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div['
            '2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot(chrome_driver_path)
bot.get_internet_speed()
bot.tweet_at_provider()
