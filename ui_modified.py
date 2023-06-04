#This file is a inheritance file of the user_interface file

#Import modules
import pyfiglet 
from colorama import Back, Fore, Style 

#Import File to be inherited
from user_interface import UserInterface

#Create class
class UiModified(UserInterface):    
#Add methods
    def __init__(self):
        self.intro = f"{Fore.LIGHTRED_EX}\n Enter + if Addition \n Enter - if Subtraction \n Enter * if Multiplication \n Enter / if Division \n Enter ^ for Power Operator" + Fore.RESET
    def show_instructions(self):
        #Printing the operation instructions
        print(self.intro)  

    def display_result(self, result):
        #Print result
        print (f"{Fore.LIGHTYELLOW_EX}RESULTING VALUE: \n" + Fore.RESET)
        print (Fore.MAGENTA,Style.BRIGHT,pyfiglet.figlet_format(str(result), font = "block"))

    #Output border
    def output_border(self, result):
        for i in range(len(str(result))):
            if i <= 5:
                print(Fore.LIGHTCYAN_EX,"""██████████""", end ="""░░""")
            else:
                pass
        print("\n")