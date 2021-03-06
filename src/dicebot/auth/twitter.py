import tweepy
import os

from dotenv import load_dotenv
load_dotenv()

class TwitterAuth:
    def __init__(self):
        self.API_KEY = os.environ.get('API_KEY')
        self.API_KEY_SECRET = os.environ.get('API_KEY_SECRET')
        self.ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
        self.ACCESS_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')

    def get_auth(self):
        auth = tweepy.OAuthHandler(self.API_KEY, self.API_KEY_SECRET, 'oob')
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        return api


class TwitterBot:
    def __init__(self, api):
        self.api = api

    def get_bot(self):
        bot = self.api.verify_credentials()
        return bot
