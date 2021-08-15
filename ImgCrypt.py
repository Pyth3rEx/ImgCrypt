import os
from colorama.initialise import reset_all
from pyfiglet import Figlet
from colorama import init
init()
from colorama import Fore, Back, Style
from stegano import lsb
import glob

#Vars
version = '0.01'

#Functions
def banner_printer ():
    custom_fig = Figlet(font='ogre')
    print(Fore.GREEN + custom_fig.renderText('ImgCrypt'))
    print('Pyth3rSearch v' + version)
    print('Made by Pyth3rEx')
    print('===============')
    print(Style.RESET_ALL)
    return

#Start of UI
os.system('cls' if os.name == 'nt' else 'clear') #clear the terminal
banner_printer()
print("Welcome to ImgCypt. Chose an Option:")
print(Fore.MAGENTA + '[1]' + Fore.RESET +' Encrypt Message' + Fore.RESET)
print(Fore.MAGENTA + '[2]' + Fore.RESET +' Decrypt Message' + Fore.RESET)
option = input()
if option == str(1):
    print('Chose the message to encrypt:')
    message = input()
    os.system('cls' if os.name == 'nt' else 'clear') #clear the terminal
    print('Chose image to encrpt to:')
    num = 0
    images = glob.glob('Images/*.png', recursive=True)
    for i in images:
        print('[' + str(num) + ']' + i)
        num = num + 1
    selectedImage = input()
    if not int(selectedImage) < int(num):
        print(Fore.RED + 'ERROR 0003')
        print('exiting...')
        input()
        exit(1)
    else:
        print('Crpting...')
        imgPath = images[int(selectedImage)]
        secret = lsb.hide(imgPath, message)
        print('Saving...')
        newImgPath = imgPath.removesuffix('.png')
        newImgPath = newImgPath + '_crypt.png'
        secret.save(newImgPath)
        print('Saved...')
        input()
elif option == str(2):
    print('Decrypting...')
    print(lsb.reveal("testImg_crpt.png"))
else:
    print(Fore.RED + 'ERROR 0001')
    print('exiting...')
    input()
    exit(1)