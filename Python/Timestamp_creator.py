# Clay
# https://replit.com/@ClayPotato/TimestampCreator?v=1

import time
import datetime
import os
import pyperclip
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def format(y,m,d,h,mi):
    print(f"{bcolors.OKGREEN}Formatting.. ")
    dt = datetime.datetime(year=int(y), month=int(m), day=int(d), hour=int(h), minute=int(mi))
    strt = str(dt.timestamp()).split(".")
    print(f"{bcolors.WARNING}TIMESTAMP: {strt[0]}")
    pyperclip.copy(strt[0])

def run():
    print("Make sure the time is UTC")
    year = input(f"{bcolors.BOLD}Year: {bcolors.OKCYAN}")
    month = input(f"{bcolors.BOLD}{bcolors.ENDC}Month: {bcolors.OKCYAN}")
    day = input(f"{bcolors.BOLD}{bcolors.ENDC}Day: {bcolors.OKCYAN}")
    hour = input(f"{bcolors.BOLD}{bcolors.ENDC}Hour (24hr): {bcolors.OKCYAN}")
    minute = input(f"{bcolors.BOLD}{bcolors.ENDC}Minute: {bcolors.OKCYAN}")

    print(f"""
{bcolors.BOLD}{bcolors.ENDC}
PLEASE CONFIRM:
    Year: {bcolors.OKCYAN}{year}{bcolors.ENDC}
    Month: {bcolors.OKCYAN}{month}{bcolors.ENDC}
    Day: {bcolors.OKCYAN}{day}{bcolors.ENDC}
    Hour: {bcolors.OKCYAN}{hour}{bcolors.ENDC}
    Minute: {bcolors.OKCYAN}{minute}{bcolors.ENDC}
    """)

    verdict = input("Continue? (y/n): ")
    if verdict.lower() == "y":
        format(year, month, day, hour, minute)
    if verdict.lower() == "n":
        fv = input(f"{bcolors.WARNING} Are you sure? (y/n): {bcolors.ENDC}")
        if fv.lower() == "n":
            format(year, month, day, hour, minute)
        else:
            print(f"{bcolors.FAIL} CLEARING CONSOLE AND RESTARTING IN 5 SECONDS.. {bcolors.ENDC}")
            time.sleep(5)
            os.system("cls")
            run()



run()
