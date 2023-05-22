#This file will include the program design such as the program header.

#Importing color module
from colorama import Back, Fore, Style 

#Create Class
class ProgramDesign:
    #Program header
    def program_header (self):
        print(Fore.LIGHTYELLOW_EX, """
                                    ──────▄▀▄─────▄▀▄
                                    ─────▄█░░▀▀▀▀▀░░█▄ 
                                    ─▄▄──█░░░░░░░░░░░█──▄▄
                                    █▄▄█─█░░▀░░┬░░▀░░█─█▄▄█"""+ Fore.LIGHTCYAN_EX,"""                      
                            █▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ ▀█▀ █▀█ █▀█
                            █▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄""")
        print(Fore.WHITE,  "="* 35 + "Calculator Program - OOP way" + "="* 35 ,"\n\n")

    #Program Footer
    def program_footer(self):
        print(Fore.RED, """

                            ▀█▀ █░█ ▄▀█ █▄░█ █▄▀   █▄█ █▀█ █░█ █
                            ░█░ █▀█ █▀█ █░▀█ █░█   ░█░ █▄█ █▄█ ▄""" + Fore.WHITE, """
                                    -🅗🅐🅥🅔 🅐 🅖🅡🅔🅐🅣 🅓🅐🅨-""")

    #Operator design    
    def operators(self):
        print(Fore.LIGHTCYAN_EX, """

                            ░░░░░░░  ░░░░░░  ██╗░░██╗  ░░░░██╗
                            ░░██╗░░  ░░░░░░  ╚██╗██╔╝  ░░░██╔╝
                            ██████╗  █████╗  ░╚███╔╝░  ░░██╔╝░
                            ╚═██╔═╝  ╚════╝  ░██╔██╗░  ░██╔╝░░
                            ░░╚═╝░░  ░░░░░░  ██╔╝╚██╗  ██╔╝░░░
                            ░░░░░░░  ░░░░░░  ╚═╝░░╚═╝  ╚═╝░░░░
  """)
        print(Fore.LIGHTWHITE_EX, "="* 35 + "CHOOSE YOUR OPERATOR" + "="* 35 ,"\n" + Fore.RESET)

    #Numbers design
    def numbers(self):
        print (Fore.LIGHTWHITE_EX, "="* 35 + "CHOOSE YOUR NUMBERS" + "="* 35 , Fore.LIGHTMAGENTA_EX,"""

           █▀▀█ 　 ▄█─ 　 █▀█ 　 █▀▀█ 　 ─█▀█─ 　 █▀▀ 　 ▄▀▀▄ 　 ▀▀▀█ 　 ▄▀▀▄ 　 ▄▀▀▄ 
           █▄▀█ 　 ─█─ 　 ─▄▀ 　 ──▀▄ 　 █▄▄█▄ 　 ▀▀▄ 　 █▄▄─ 　 ──█─ 　 ▄▀▀▄ 　 ▀▄▄█ 
           █▄▄█ 　 ▄█▄ 　 █▄▄ 　 █▄▄█ 　 ───█─ 　 ▄▄▀ 　 ▀▄▄▀ 　 ─▐▌─ 　 ▀▄▄▀ 　 ─▄▄▀""", "\n" +Fore.RESET)

    def loading_bar(self):
        from tqdm import tqdm
        from time import sleep
        print("LOADING CALCULATOR")
        for i in tqdm(range(50)):
            sleep(0.1)