import dhooks
import time
import requests
import colorama
import subprocess
import platform
from colorama import Fore, Style, init
from dhooks import Webhook

init(autoreset=True)

GREEN = Fore.GREEN
RESET = Style.RESET_ALL

logo = """
██████  ██████  ██ ███████ ███    ███  ██████ 
██   ██ ██   ██ ██    ███  ████  ████ ██    ██ 
██████  ██████  ██   ███   ██ ████ ██ ██    ██ 
██      ██   ██ ██  ███    ██  ██  ██ ██    ██ 
██      ██   ██ ██ ███████ ██      ██  ██████  
                                            
"""

def clear_screen():
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)

clear_screen()

print(f"{GREEN}{logo}{RESET}")

delay = int(input(f"{GREEN}Delay (seconds): {RESET}"))
amount = int(input(f"{GREEN}Amount of messages: {RESET}"))
webhook_url = input(f"{GREEN}Webhook URL: {RESET}").strip()
message = input(f"{GREEN}Message: {RESET}")

for i in range(amount):
    time.sleep(delay)
    payload = {"content": message}
    response = requests.post(webhook_url, json=payload)
    if response.status_code != 204:
        print(f"{GREEN}Failed to send message: {response.status_code}{RESET}")
    else:
        print(f"{GREEN}Message sent successfully!{RESET}")

