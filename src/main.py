from src.auth.twitter import TwitterAuth, TwitterBot
from src.auth.google import GoogleAuth
from account import Mention
import time

def main():
    api = TwitterAuth().get_auth()
    bot = TwitterBot(api).get_bot()

    gc = GoogleAuth().get_auth()

    m = Mention(api, bot, gc)
    while True:
        print("start")
        m.get_mentions()
        m.check_mentions()
        time.sleep(20)

if __name__ == "__main__":
    main()