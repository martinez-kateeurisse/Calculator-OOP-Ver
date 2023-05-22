#This file will include the program design such as the program header.

from colorama import Back, Fore, Style 

class ProgramDesign:
    def program_header (self):
        print(Fore.LIGHTYELLOW_EX, """
                                    ──────▄▀▄─────▄▀▄
                                    ─────▄█░░▀▀▀▀▀░░█▄ 
                                    ─▄▄──█░░░░░░░░░░░█──▄▄
                                    █▄▄█─█░░▀░░┬░░▀░░█─█▄▄█"""+ Fore.LIGHTCYAN_EX,"""                      
                            █▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ ▀█▀ █▀█ █▀█
                            █▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄""")
        print(Fore.WHITE,  "="* 35 + "Calculator Program - OOP way" + "="* 35 ,"\n")

    def program_footer(self):
        print(Fore.RED, """

                            ▀█▀ █░█ ▄▀█ █▄░█ █▄▀   █▄█ █▀█ █░█ █
                            ░█░ █▀█ █▀█ █░▀█ █░█   ░█░ █▄█ █▄█ ▄""" + Fore.WHITE, """
                                    -🅗🅐🅥🅔 🅐 🅖🅡🅔🅐🅣 🅓🅐🅨-""")
        
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

    def numbers(self):
        print (Fore.LIGHTWHITE_EX, "="* 35 + "CHOOSE YOUR NUMBERS" + "="* 35 , Fore.LIGHTMAGENTA_EX,"""

           █▀▀█ 　 ▄█─ 　 █▀█ 　 █▀▀█ 　 ─█▀█─ 　 █▀▀ 　 ▄▀▀▄ 　 ▀▀▀█ 　 ▄▀▀▄ 　 ▄▀▀▄ 
           █▄▀█ 　 ─█─ 　 ─▄▀ 　 ──▀▄ 　 █▄▄█▄ 　 ▀▀▄ 　 █▄▄─ 　 ──█─ 　 ▄▀▀▄ 　 ▀▄▄█ 
           █▄▄█ 　 ▄█▄ 　 █▄▄ 　 █▄▄█ 　 ───█─ 　 ▄▄▀ 　 ▀▄▄▀ 　 ─▐▌─ 　 ▀▄▄▀ 　 ─▄▄▀"""+Fore.RESET)
