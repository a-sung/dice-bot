import gspread
import pprint

gc = gspread.service_account(filename="../t-bots-06202329-0a7625fa5fa6.json")
wks = gc.open("coc-dice-bot")


# 시트 탭 선택 함수
def select_sheet(sheet_name):
    worksheet = wks.get_worksheet(0) # 시트 인덱스로 접근
    # worksheet = wks.worksheet(sheet_name) # 시트 이름으로 접근
    return worksheet


# 시트 전체 정보 터미널에 프린트하는 함수
def shop_sheet(worksheet):
    all_shop_info = worksheet.get_all_records()
    pprint.pprint(all_shop_info)


# 파일 내 시트 전체 순회
c = 0
for i in wks:
    worksheet = wks.get_worksheet(c) # 인덱스로 시트 접근
    shop_sheet(worksheet)
    c+=1