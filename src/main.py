from src.dicebot.auth.twitter import TwitterAuth, TwitterBot
from src.dicebot.auth.google import GoogleAuth
from src.dicebot.bot import tweet, keyword, sheet, dice
from datetime import datetime
from pytz import timezone
import time


def main():
    api = TwitterAuth().get_auth()
    bot = TwitterBot(api).get_bot()

    gc = GoogleAuth().get_auth()

    tw = tweet.Tweet(api, bot)
    while True:
        mentions = tw.get()
        for mention in mentions:

            # get time of replying mention
            now = datetime.now(timezone('Asia/Seoul'))
            nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
            author = mention.author
            text = None

            key, details = keyword.find(mention.text)
            if key is None:
                continue

            if 'd' in key:
                # Determining outcome of dice
                if len(key) == 3:
                    value = dice.roll(int(key[0]), int(key[2]))
                else:
                    value = dice.roll(int(key[0]), int(key[2]), key[3], int(key[4]))
                key = ''.join(key)
                text = f'@{author.screen_name}{author.name}의 {key}판정\n주사위 값: {value}\n\n{nowDatetime}'
            elif details is None:
                # Determining outcome of stats, skills or battle
                value = dice.roll()
                outcome = sheet.determine(gc, mention.author.screen_name, value, key)
                if outcome is None:
                    continue
                text = f'@{author.screen_name}{author.name}의 {key}판정\n주사위 값: {value}\n판정 결과: {outcome}\n\n{nowDatetime}'

            # reply mention
            if text is not None:
                tw.reply(text, mention.id_str)
        time.sleep(60)

if __name__ == "__main__":
    main()