def determine(gc, name, value, keyword, details=None):
    sh = open(gc, name)
    cell = find(sh, keyword)
    if cell is None:
        return None

    row = cell.row
    col = cell.col
    success = {"normal": -1, "hard": -1, "extreme": -1, "critical": 1}
    if keyword == "이성":
        success["normal"] = sh.cell(row + 1, col + 2).value
        success["hard"] = int(success["normal"]//2)
        success["extreme"] = int(success["normal"]//5)

    elif row < 13:
        # stats
        success["normal"] = sh.cell(row, col + 2).value
        success["hard"] = sh.cell(row, col + 4).value
        success["extreme"] = sh.cell(row + 1, col + 4).value
    elif row < 39:
        # skills
        success["normal"] = sh.cell(row, col + 5).value
        success["hard"] = sh.cell(row, col + 6).value
        success["extreme"] = sh.cell(row, col + 7).value
    else:
        # battle
        pass

    if success["normal"] == -1:
        return None
    if value == 1:
        return "대성공"
    elif value <= int(success["extreme"]):
        return "극단적 성공"
    elif value <= int(success["hard"]):
        return "어려운 성공"
    elif value <= int(success["normal"]):
        return "성공"
    else:
        if value == 100 or (int(success["normal"]) < 50 and value > 95):
            return "대실패"
        else:
            return "실패"


def open(gc, name):
    try:
        sh = gc.worksheet(name)
    except:
        print(f"Error: {name} not founded in spreadsheet")
        pass
    return sh


def find(sh, keyword):
    cell = sh.find(keyword)
    if cell is None:
        print("Error: keyword is not in spreadsheet")
        return None
    return cell