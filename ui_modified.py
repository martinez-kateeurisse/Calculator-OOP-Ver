#Import modules
import pyfiglet 
from colorama import Back, Fore, Style 

#Import File to be inherited
from user_interface import UserInterface

#Create class
class UiModified(UserInterface):    
#Add methods
    def display_result(self, result):
        print(f"{Fore.LIGHTYELLOW_EX}RESULTING VALUE: " + str(result) + Fore.RESET)
#Return results


