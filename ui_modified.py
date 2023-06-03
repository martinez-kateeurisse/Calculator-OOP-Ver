#Import modules
import pyfiglet 
from colorama import Back, Fore, Style 

#Import File to be inherited
from user_interface import UserInterface

#Create class
class UiModified(UserInterface):    
#Add methods
    def display_result(self, result):
        #Print result
        print(f"{Fore.LIGHTYELLOW_EX}RESULTING VALUE: \n" + Fore.RESET)
        print(Fore.MAGENTA,Style.BRIGHT,pyfiglet.figlet_format(result, font = "block"))



