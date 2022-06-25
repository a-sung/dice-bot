import tweepy

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

        # find keyword in spreadsheet
        cell = sh.find(keyword)
        row = cell.row
        col = cell.col
        if row < 10:
            # 특성치
            success = sh.cell(row, col + 2).value
            print(success)
        elif row < 39:
            # 기능치
            success = sh.cell(row, col + 5).value
            print(success)
        else:
            # 전투
            pass






