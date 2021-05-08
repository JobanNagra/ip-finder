import colorama
from colorama import Fore, Back, Style

colorama.init()

print(Fore.CYAN  + 'Hi!!')
print('GtaV')


message = 'Author ; Jobanpreet Singh'
print(message)
print()
print()

message = 'Github; Joban Nagra'
print(message)
print()
print()


message = 'This Programme will tell Your Ip'
print(message)
print()
print()


print(Fore.LIGHTGREEN_EX + 'Lets Begin')
print()
print('joban')


import socket
hostn = socket.gethostname()
ipad = socket.gethostbyname(hostn)

print('Your IP Address = ' +ipad)
print()

print('Now you Know your Ip so better Try to hide it from hackers')
input('press enter to close')