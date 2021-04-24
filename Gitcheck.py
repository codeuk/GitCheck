import requests, re, json, time, os
from colorama import init, Fore
init(autoreset=True)

os.system('cls')

def check(username):
    s = requests.Session()

    req = s.get("https://github.com/" + username)
    if (req.status_code == 404):
        return ("hit")
    elif (req.status_code == 200):
        return ("taken")
    elif (req.status_code == 429):
        return ("timeout")
    else:
        return ("Unknown Error")


if __name__ == "__main__":
    with open('words.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    for word in content:
        file = open('hits.txt', 'a')
        resp = check(word)
        if resp == "hit":
            print(Fore.GREEN + 'HIT: ' + Fore.RESET + Fore.GREEN + word)
            file.write(word + "\n")
            file.close()
        elif resp == "taken":
            print(Fore.RED + 'BAD: ' + Fore.RESET + Fore.RED + word)
        elif resp == "timeout":
            print(Fore.WHITE + "Timeout")
            time.sleep(1000)
        else:
            print(Fore.YELLOW + "UNKNOWN ERROR - CODE PROBLEM?")
            time.sleep(1000)
print(f"{Fore.RESET}[{Fore.YELLOW}CHECKER FINISHED - HITS SAVED TO FILE{Fore.RESET}]")
print(" ")
print(f"{Fore.RESET}[{Fore.GREEN}Created by github.com/u6m ~ doop{Fore.RESET}]")
file.close()

