from datetime import datetime

import gspread

gc = gspread.service_account(filename="service_account.json")
sh = gc.open("Аутрич")
ws = sh.worksheet("Linkedin Helper Campaign Events")


def insert_row(ld_url, event="Message sent", campaign="", ld_account="Alexandra Gavri"):
    row = [
        ld_url,
        event,
        datetime.now().strftime("%a, %B %-d, %Y"),
        campaign,
        ld_account,
        '=TEXT(C2, "DD.MM.YYY")'
    ]

    ws.insert_row(row, index=2, value_input_option="USER_ENTERED")
