from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyautogui import press
import time
import re

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get("https://twitter.com")
        press('F11')
        time.sleep(1.5)
        username = bot.find_element_by_name("session[username_or_email]")
        password = bot.find_element_by_name("session[password]")
        username.clear()
        password.clear()
        username.send_keys(self.username)
        username.send_keys(Keys.F11)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweets_by_hashtag(self, hashtag):
        bot = self.bot
        bot.get("https://twitter.com/search?q=%23{}&src=typed_query".format(hashtag))
        time.sleep(5)
        while True:
            tweets = bot.find_elements_by_xpath('//article[@role="article"]')
            for tweet in tweets:
                tweet_code = tweet.get_attribute('innerHTML')
                tweet_id = re.search(r'/\S*/*/status/[0-9]*', tweet_code)
                tweet_link = 'https://twitter.com' + tweet_id.group()
                bot.execute_script("window.open('');")
                bot.switch_to.window(bot.window_handles[1])
                time.sleep(0.5)
                bot.get(tweet_link)
                time.sleep(1)
                like_buttons = bot.find_elements_by_xpath('//div[@data-testid="like"]')
                like_buttons[0].click()
                time.sleep(2)
                bot.close()
                bot.switch_to.window(bot.window_handles[0])
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(5)