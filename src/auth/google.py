from oauth2client.service_account import ServiceAccountCredentials
import gspread

class GoogleAuth():
    def __init__(self):
        self.scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        self.keyfile = "../../t-bots-06202329-0a7625fa5fa6.json"
        self.filename = "coc-dice-bot"

    def get_auth(self):
        credit = ServiceAccountCredentials.from_json_keyfile_name(self.keyfile, self.scope)
        client = gspread.authorize(credit)
        gc = client.open(self.filename)
        return gc


# # 시트 탭 선택 함수
# def select_sheet(sheet_name):
#     worksheet = wks.get_worksheet(0) # 시트 인덱스로 접근
#     # worksheet = wks.worksheet(sheet_name) # 시트 이름으로 접근
#     return worksheet
