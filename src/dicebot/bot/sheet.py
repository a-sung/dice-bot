def determine(gc, name, keyword, details=None):
    sh = open(gc, name)
    cell = find(sh, keyword)
    if cell is None:
        return None

    row = cell.row
    col = cell.col
    success = {"normal": -1, "hard": -1, "extreme": -1, "critical": 1}
    if row < 13:
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

    return success


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