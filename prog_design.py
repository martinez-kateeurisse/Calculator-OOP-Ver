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