class Tweet():
    def __init__(self, api, bot):
        self.api = api
        self.timeline_list = api.user_timeline(user_id=bot.id)
        self.last_reply_id = self.timeline_list[0].id_str

    def get(self):
        # get new mentions after last_reply_id
        mentions = self.api.mentions_timeline(since_id=self.last_reply_id)
        mentions.reverse()
        return mentions

    def reply(self, text, id):
        # reply mention to id
        try:
            self.api.update_status(text, in_reply_to_status_id=id)
            self.last_reply_id = id
        except:
            print("error: can't replying mention")
            pass
        return
