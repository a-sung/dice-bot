from src.dicebot.auth.twitter import TwitterAuth, TwitterBot
from src.dicebot.auth.google import GoogleAuth
from src.dicebot.bot import tweet, keyword, sheet, dice
from datetime import datetime
import time


def main():
    api = TwitterAuth().get_auth()
    bot = TwitterBot(api).get_bot()

    gc = GoogleAuth().get_auth()

    tw = tweet.Tweet(api, bot)
    while True:
        mentions = tw.get()
        for mention in mentions:
            key, details = keyword.find(mention.text)
            if key is None:
                continue
            if details is None:
                # Determining outcome of stats, skills or battle
                value = dice.roll()
                outcome = sheet.determine(gc, mention.author.screen_name, value, key)
            if outcome is None:
                continue

            # reply mention
            now = datetime.now()
            nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
            author = mention.author
            text = f'@{author.screen_name}{author.name}의 {key}판정\n주사위 값: {value}\n판정 결과: {outcome}\n\n{nowDatetime}'

            tw.reply(text, mention.id_str)
        time.sleep(60)

if __name__ == "__main__":
    main()