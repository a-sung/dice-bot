import tweepy
import random
import datetime

class Mention:
    def __init__(self, api, bot, gc):
        self.timeline_list = api.user_timeline(user_id=bot.id)
        self.last_reply_id = self.timeline_list[0].id_str
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
                # sh = self.gc.worksheet(receiver.screen_name)
                # self.check_keywords(mention, sh)
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

        # results success or fail
        row = cell.row
        col = cell.col
        success = {"normal":-1, "hard":-1, "extreme":-1, "critical":1}
        if row < 13:
            # 특성치
            success["normal"] = sh.cell(row, col+2).value
            success["hard"] = sh.cell(row, col+4).value
            success["extreme"] = sh.cell(row+1, col+4).value
        elif row < 39:
            # 기능치
            success["normal"] = sh.cell(row, col+5).value
            success["hard"] = sh.cell(row, col+6).value
            success["extreme"] = sh.cell(row, col+7).value
        else:
            # 전투
            pass

        dice = random.randint(1, 100)
        isSuccess = self.roll_keyward_dice(dice, success)
        msg = self.make_reply(sh.acell('E5').value, dice, keyword, isSuccess)
        self.reply_mention(mention, msg)


    def roll_keyward_dice(self, dice, success):
        if success["normal"] == -1:
            return None
        if dice == 1:
            return "대성공"
        elif dice <= int(success["extreme"]):
            return "극단적 성공"
        elif dice <= int(success["hard"]):
            return "어려운 성공"
        elif dice <= int(success["normal"]):
            return "성공"
        else:
            if dice == 100 or (int(success["normal"]) < 50 and dice > 95):
                return "대실패"
            else:
                return "실패"


    def make_reply(self, name, dice, keyword, isSuccess=None):
        now = datetime.datetime.now()
        nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
        msg = f'다시 시도해 주시기 바랍니다.\n\n{nowDatetime}'
        if isSuccess is not None:
            msg = f'{name}의 {keyword}판정\n주사위 값: {dice}\n판정 결과: {isSuccess}\n\n{nowDatetime}'
        return msg

    def reply_mention(self, mention, message):
        msg = '@' + mention.author.screen_name + '\n' + message
        try:
            self.api.update_status(msg, in_reply_to_status_id=mention.id_str)
            self.last_reply_id = mention.id_str
        except:
            print("error for replying mention")
            pass
        return



