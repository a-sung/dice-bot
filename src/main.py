from auth import TwitterAuth, TwitterBot
from account import Mention
import time

def main():
    api = TwitterAuth().get_auth()
    bot = TwitterBot(api).get_bot()

    m = Mention(api, bot)
    while True:
        m.get_mentions()
        m.check_mentions()
        time.sleep(20)

if __name__ == "__main__":
    main()