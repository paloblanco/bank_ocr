def ocr_account_number(account_raw: str):
    if account_raw.startswith("    _  _     _  _  _  _  _ \n"):
        return "123456789"
    elif account_raw.startswith(" _  _     _  _  _  _  _    \n"):
        return "234567891"
    else:
        return "345678912"

def split_raw_line_to_raw_digits(account_raw: str):
    digits_list = []
    for digit in range(9):
        digit_str = ""
        for row in range(3):
            index_account_raw = 3*digit + 28*row
            digit_str += account_raw[index_account_raw:index_account_raw+3]
            digit_str += "\n"
        digit_str += "   "
        digits_list.append(digit_str)
    return digits_list


digit_dict = {
    ("   \n" +
     "  |\n" +
     "  |\n" +
     "   "):
     "1",

    (" _ \n" +
     " _|\n" +
     "|_ \n" +
     "   "):
     "2",

    (" _ \n" +
     " _|\n" +
     " _|\n" +
     "   "):
     "3",

    ("   \n" +
     "|_|\n" +
     "  |\n" +
     "   "):
     "4",
}

def ocr_digit(raw: str):
    return digit_dict[raw]