class Sheet():
    def __init__(self, gc, name, value, keyword, details=None):
        self.gc = gc
        self.sh = self.open(gc, name)
        self.value = value
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
            outcome = self.judgeStat(row, col)
            return f'주사위 값: {self.value}\n판정 결과: {outcome}'

        elif row < 39:
            # skills
            outcome = self.judgeSkill(row, col)
            return f'주사위 값: {self.value}\n판정 결과: {outcome}'

        else:
            # battle
            outcome = self.judgeBattle(row, col)
            return f'주사위 값: {self.value}\n판정 결과: {outcome}'

    def judgeStat(self, row, col):
        self.success["normal"] = self.sh.cell(row, col + 2).value
        self.success["hard"] = self.sh.cell(row, col + 4).value
        self.success["extreme"] = self.sh.cell(row + 1, col + 4).value
        return self.determine()

    def judgeSkill(self, row, col):
        self.success["normal"] = self.sh.cell(row, col + 5).value
        self.success["hard"] = self.sh.cell(row, col + 6).value
        self.success["extreme"] = self.sh.cell(row, col + 7).value
        return self.determine()

    def judgeBattle(self, row, col):
        self.success["normal"] = self.sh.cell(row, col + 6).value
        self.success["hard"] = self.sh.cell(row, col + 7).value
        self.success["extreme"] = self.sh.cell(row, col + 8).value
        return self.determine()

    def determine(self):
        if self.success["normal"] == -1:
            return None
        if self.value == 1:
            return "대성공"
        elif self.value <= int(self.success["extreme"]):
            return "극단적 성공"
        elif self.value <= int(self.success["hard"]):
            return "어려운 성공"
        elif self.value <= int(self.success["normal"]):
            return "성공"
        else:
            if self.value == 100 or (int(self.success["normal"]) < 50 and self.value > 95):
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

    def find(self, sh, keyword):
        cell = sh.find(keyword)
        if cell is None:
            print("Error: keyword is not in spreadsheet")
            return None
        return cell
