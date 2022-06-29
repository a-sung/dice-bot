def find(text):
    text = text.replace(' ', '')
    k1 = text.find('[')
    k2 = text.find(']')

    key = text[k1 + 1:k2]
    details = None

    if k1 == -1 or k2 == -1 or k1 > k2:
        # if keyword is not in mention, return
        # todo: exception, logging
        print("Error: keyword is not in your mention")
        return None, None

    if 'd' in key:
        key_list = list(key)
        if len(key_list) == 3 and key_list[0].isdigit() and key_list[1] == 'd' and key_list[2].isdigit():
            return key_list, details
        if len(key_list) == 5 and key_list[0].isdigit() and key_list[1] == 'd' and key_list[2].isdigit() and (key_list[3] == '+' or key_list[3] == '-') and key_list[4].isdigit():
            return key_list, details


    # todo: keyword of edit spread sheet

    return key, details
