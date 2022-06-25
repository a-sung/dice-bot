import tweepy

class Mention:
    def __init__(self, api, bot):
        self.last_reply_id = 1
        self.api = api
        self.bot = bot
        self.mentions = None
        self.receiver = None

    def get_mentions(self):
        # get new mentions after last_reply_id
        self.mentions = self.api.mentions_timeline(since_id=self.last_reply_id)
        self.mentions.reverse()

    def check_mentions(self):
        if self.mentions is None:
            print("no new mentions")
            return
        for mention in self.mentions:
            print(mention)

