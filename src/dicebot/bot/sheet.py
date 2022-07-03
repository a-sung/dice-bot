from src.dicebot.bot import dice

class Sheet():
    def __init__(self, gc, name, keyword, details=None):
        self.gc = gc
        self.sh = self.open(gc, name)
        self.keyword = keyword
        self.cell = self.find(self.sh, keyword)
        self.success = {"normal": -1, "hard": -1, "extreme": -1, "critical": 1}

    def result(self):
        if self.cell is None:
            return None

        row = self.cell.row
        col = self.cell.col
        if row < 13:
            # stats
            value = dice.roll()
            self.judgeStat(row, col)
            outcome = self.determine(value)
            return f'주사위 값: {value}\n판정 결과: {outcome}\n\n'

        elif row < 39:
            # skills
            value = dice.roll()
            self.judgeSkill(row, col)
            outcome = self.determine(value)
            return f'주사위 값: {value}\n판정 결과: {outcome}\n\n'

        else:
            # battle
            text = ''
            for i in range (0, int(self.sh.cell(row, col + 18).value)):
                damage_dice = list(self.sh.cell(row, col + 9))
                damage_bonus_cell = self.find("피해보너스")
                damage_bonus_dice = list(self.sh.cell(damage_bonus_cell.row, damage_bonus_cell + 3))

                damage = 0
                bonus_damage = 0
                # todo: 성공 시 데미지 판정
                value = dice.roll()
                self.judgeBattle(row, col)
                outcome = self.determine(value)
                text += f'공격 {i + 1}회\n주사위 값:{value}\n판정 결과:{outcome}\n'
                success_degree = ["성공", "어려운 성공", "극단적 성공"]
                # todo: 피해보너스, ndm+r 데미지 판정, 대성공
                if outcome in success_degree :
                    damage = dice.roll(damage_dice[0], damage_dice[2])
                    if damage_bonus_dice is not 0:
                        bonus_damage = dice.roll(damage_bonus_dice[0], damage_bonus_dice[2])
                    full_damage = damage + bonus_damage
                    text += f'데미지: {damage}+{bonus_damage} = {full_damage}\n\n'


            return text

    def judgeStat(self, row, col):
        self.success["normal"] = self.sh.cell(row, col + 2).value
        self.success["hard"] = self.sh.cell(row, col + 4).value
        self.success["extreme"] = self.sh.cell(row + 1, col + 4).value

    def judgeSkill(self, row, col):
        self.success["normal"] = self.sh.cell(row, col + 5).value
        self.success["hard"] = self.sh.cell(row, col + 6).value
        self.success["extreme"] = self.sh.cell(row, col + 7).value

    def judgeBattle(self, row, col):
        self.success["normal"] = self.sh.cell(row, col + 6).value
        self.success["hard"] = self.sh.cell(row, col + 7).value
        self.success["extreme"] = self.sh.cell(row, col + 8).value

    def determine(self, value):
        if self.success["normal"] == -1:
            return None
        if value == 1:
            return "대성공"
        elif value <= int(self.success["extreme"]):
            return "극단적 성공"
        elif value <= int(self.success["hard"]):
            return "어려운 성공"
        elif value <= int(self.success["normal"]):
            return "성공"
        else:
            if value == 100 or (int(self.success["normal"]) < 50 and value > 95):
                return "대실패"
            else:
                return "실패"

    def open(self, gc, name):
        try:
            sh = gc.worksheet(name)
        except:
            print(f"Error: {name} not founded in spreadsheet")
            pass
        return sh

    def find(self, keyword):
        cell = self.sh.find(keyword)
        if cell is None:
            print("Error: keyword is not in spreadsheet")
            return None
        return cell
