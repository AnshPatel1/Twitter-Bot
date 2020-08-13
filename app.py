from twitterbot import *
from MyPasswordPrivatizer import GetPassword
Bot = TwitterBot("annssshhhh_", GetPassword("password.txt"))
Bot.login()
Bot.like_tweets_by_hashtag("coding")