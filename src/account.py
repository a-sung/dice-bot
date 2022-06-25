import tweepy
import random

class Mention:
    def __init__(self, api, bot, gc):
        self.last_reply_id = 1
        self.api = api
        self.bot = bot
        self.mentions = None
        self.receiver = None
        self.gc = gc

    def get_mentions(self):
        # get new mentions after last_reply_id
        self.mentions = self.api.mentions_timeline(since_id=self.last_reply_id)
        self.mentions.reverse()

    def check_mentions(self):
        if self.mentions is None:
            print("no new mentions")
            return
        for mention in self.mentions:
            # check user in spreadsheet
            receiver = mention.author
            if receiver.id != self.bot.id:
                try:
                    sh = self.gc.worksheet(receiver.screen_name)
                    self.check_keywords(mention, sh)
                except:
                    print(receiver.screen_name, "not founded in spreadsheet")
                    pass

    def check_keywords(self, mention, sh):
        # find keyword in mention text
        text = mention.text
        keyword = ""
        k1 = text.find("[")
        k2 = text.find("]")
        keyword = text[k1+1:k2]
        if k1 == -1 or k2 == -1 or k1 > k2:
            # if keyword is not in mention, return
            print("keyword is not in your mention")
            return

        # find keyword in spreadsheet
        cell = sh.find(keyword)

        # keyword is not in spreadsheet, return
        if cell is None:
            print("keyword is not in spreadsheet")
            return

        # get dice value
        dice = random.randint(1, 100)
        print("dice:", dice)

        # results success or fail
        row = cell.row
        col = cell.col
        success = {"normal":-1, "hard":-1, "extreme":-1, "critical":1}
        if row < 10:
            # 특성치
            success["normal"] = sh.cell(row, col+2).value
            success["hard"] = sh.cell(row, col+4).value
            success["extreme"] = sh.cell(row+1, col+4).value
            print(success)
        elif row < 39:
            # 기능치
            success["normal"] = sh.cell(row, col+5).value
            success["hard"] = sh.cell(row, col+6).value
            success["extreme"] = sh.cell(row, col+7).value
            print(success)
        else:
            # 전투
            pass
        self.make_reply(keyword, success)

    def make_reply(self, keyword, success):
        if success["normal"] == -1 : return




