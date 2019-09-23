from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Twli:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get("http://twitter.com")
        time.sleep(2)
        username = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')

        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(2)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/hashtag/'+hashtag+'?src=hashtag_click')
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script(window.scrollTo(0,document.body.scrollHeight))


foysal = Twli("email", "password")


foysal.login()
foysal.like_tweet('100DaysOfCode')
