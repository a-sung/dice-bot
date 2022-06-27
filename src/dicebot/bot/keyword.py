def find(text):
    k1 = text.find('[')
    k2 = text.find(']')

    key = text[k1 + 1:k2]
    details = None

    if k1 == -1 or k2 == -1 or k1 > k2:
        # if keyword is not in mention, return
        # todo: exception, logging
        print("Error: keyword is not in your mention")
        return None

    if 'd' in key:
        # todo: random dice (ex. 1d4, 1d3+1)
        print("Error: not supported")
        return None

    return key, details
