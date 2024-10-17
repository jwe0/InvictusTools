from colorama import Fore
from datetime import datetime

def success(message):
    print(f"{Fore.LIGHTBLACK_EX}{datetime.now().strftime('%H:%M:%S')}{Fore.RESET} • {Fore.LIGHTGREEN_EX}{message}{Fore.RESET}")

def error(message):
    print(f"{Fore.LIGHTBLACK_EX}{datetime.now().strftime('%H:%M:%S')}{Fore.RESET} • {Fore.LIGHTRED_EX}{message}{Fore.RESET}")

def info(message, end="\r"):
    print(f"{Fore.LIGHTBLACK_EX}{datetime.now().strftime('%H:%M:%S')}{Fore.RESET} • {Fore.LIGHTBLUE_EX}{message}{Fore.RESET}", end=end)

def warning(message):
    print(f"{Fore.LIGHTBLACK_EX}{datetime.now().strftime('%H:%M:%S')}{Fore.RESET} • {Fore.LIGHTYELLOW_EX}{message}{Fore.RESET}")

def inpt(message):
    return input(f"{Fore.LIGHTBLACK_EX}{datetime.now().strftime('%H:%M:%S')}{Fore.RESET} • {Fore.LIGHTCYAN_EX}{message}{Fore.RESET}")