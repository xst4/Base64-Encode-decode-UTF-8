from colorama import init, Fore
import fade, colorama
import base64
import sys
import re
import os
import getopt
__author__ = "xstrong"
__version__ = "v0.1"

r = Fore.RED
y = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLACK_EX
b = Fore.BLUE
def ps_decode(encoded_data):
    decoded_data = base64.b64decode(encoded_data.encode()).decode("utf-8")
    return decoded_data
def ps_encode(data):
    blank_command = ""
    powershell_command = ""
    n = re.compile(u'(\xef|\xbb|\xbf)')
    for char in (n.sub("", data)):
        blank_command += char + "\x00"
    powershell_command = blank_command
    powershell_command = base64.b64encode(powershell_command.encode())
    return powershell_command.decode("utf-8")
def print_logo():
    colorama.deinit()
    for char in loggo:
        # time.sleep(0.001)
        sys.stdout.write(char)
        sys.stdout.flush()
loggo = fade.fire(f""" 

                                                                                  
                                         ,.   (   .      )        .      "          
                                       ("     )  )'     ,'        )  . (`     '`  ("
                                     .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"  .;   
                                    _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '.. _"
                                    ██████╗  █████╗ ███████╗███████╗ ██████╗ ██╗  ██╗
                                    ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝ ██║  ██║
                                    ██████╔╝███████║███████╗█████╗  ███████╗ ███████║
                                    ██╔══██╗██╔══██║╚════██║██╔══╝  ██╔═══██╗╚════██║
                                    ██████╔╝██║  ██║███████║███████╗╚██████╔╝     ██║
                                    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝      ╚═╝   {lb}Version : {r}{__version__}

                                                {lb}   Author : {r}{__author__}
                                                {lb}    github.com/{r}xst4
                                                {lb}    .gg/{r}8q6DpMV3e4
{r}╔═══            Base64            ═══╗
{r}║                                    ║ 

{r}          ({lb}01{r}) {lb}> Encode 
{r}          ({lb}02{r}) {lb}> Decode 
   
{r}║                                    ║
{r}╚═══                              ═══╝ 
    """)
def cls2():
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    print_logo()
    choice = input(f"{r}┌──<@BASE64>─[~]\n└──╼ $ {Fore.LIGHTBLACK_EX}:> {y}")
    if choice == "1":
        script = input(f"{r}┌──<@{lb}Enter Data To Encode{r}>─[~]\n└──╼ $ {Fore.LIGHTBLACK_EX}:> {y}")
        print(f"{r}┌──<@Encoded>─[~]\n└──╼ $ {Fore.LIGHTBLACK_EX}:> {r}{ps_encode(script)}")
        input(f"{lb}Press enter to continue ...")
        cls2()
        main()
    if choice == "2":
        decodescript = input(f"{r}┌──<@{lb}Enter Data To Decode{r}>─[~]\n└──╼ $ {Fore.LIGHTBLACK_EX}:> {y}")
        print(f"{r}┌──<@Decoded>─[~]\n└──╼ $ {Fore.LIGHTBLACK_EX}:> {r}{ps_decode(decodescript)}")
        input(f"{lb}Press enter to continue ...")
        cls2()
        main()


if __name__ == "__main__":
    main()
