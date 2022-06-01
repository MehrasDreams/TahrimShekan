# Import module
import time
from sys import platform, exit
from colorama import Fore
import command
from os import system as terminal

# Dns

dns1 = '185.51.200.2'
dns2 = '178.22.122.100'


# Check the os

def check_os():
    check_os_val = platform

    # Check if os == Windows

    if check_os_val == 'win32' or check_os_val == 'Win32' or check_os_val == 'Windows' or check_os_val == 'windows':
        print(Fore.RED + "This program is not working on windows :( just only on macos and linux and another os")
        exit()


# check if user is root
def is_root():
    root_val = command.run('whoami')
    if root_val.output == b'root':
        print(Fore.GREEN + "Ok, you are root user")
        time.sleep(3)
        print(Fore.YELLOW + "Pleas wait a second to change the dns :)\n")
        time.sleep(2)
        terminal('clear')

    elif root_val.output != b'root':
        print(Fore.RED + "This program must be run as root :( ")
        exit()


# Write the config file function
def config():
    with open('resolv.conf', 'w') as config:
        config.write(f'nameserver {dns1} \noptions edns0 trust-ad \nsearch domain.name ')


# Run the functions
check_os()
is_root()
config()

# Remove and rewrite the resolve.conf in /etc

terminal('rm -r /etc/resolv.conf')  # To remove the resolv.conf file
terminal('cp resolv.conf /etc/resolv.conf')  # To add the config file to the etc
git_hub_link = Fore.GREEN + "https://github.com/MehrasDreams"
print(Fore.BLUE + f'dns has ben changed you can use any boycott service like spotify and ...\n pleas subscribe me on '
                 f'the git hub\n My git hub {git_hub_link}')


