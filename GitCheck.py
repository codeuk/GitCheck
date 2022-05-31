import requests, threading, json, time, os

THREADS = 8

class Colors:
    """ Program Colors """
    red = u"\u001b[31m"
    green  = u"\u001b[32m"
    reset  = u"\u001b[0m"

class GitCheck:
    """ Github Username Checker """
    def __init__(self):
        self.checked = []
        self.banner = """
        -----------------------
        Github Username Checker
        -----------------------
           GITHUB.COM/CODEUK   
        =======================
        """

    @staticmethod
    def StartThreads(func) -> None:
        for i in range(THREADS):
            thread = threading.Thread(target=func, args=[i])
            thread.start()

    @staticmethod
    def Check(username) -> bool:
        r = requests.get(f"https://github.com/{username}")
        match r.status_code:
            case 404: return True
            case 200: return False

    def Log(self, threadNum):
        c = Colors()
        with open('words.txt') as f:
            words = [x.strip() for x in f.readlines()]

        with open('hits.txt', 'a') as file:
            for i, word in enumerate(words):
                if word in self.checked: continue
                else: self.checked.append(word)

                if self.Check(word):
                    print(f'{c.reset}[#{c.green}{i}{c.reset}] HIT: {c.green}{word}')
                    file.write(word + "\n")
                    file.close()
                else:
                    print(f'{c.reset}[#{c.green}{i}{c.reset}] BAD: {c.red}{word}')

    def Main(self) -> None:
        os.system('cls')
        print(self.banner)
        self.StartThreads(self.Log)

gc = GitCheck()
gc.Main()

