#This class file will include the exception handling codes.

from colorama import Back, Fore, Style 
from user_interface import UserInterface
ui = UserInterface

#Create Class
class Exceptions:
#Create Objects
    def except_condition(self, exception):
    #Create instances
        #Exception errors
        if isinstance(exception, ZeroDivisionError):
            print(f"{Fore.RED}Sorry! You are dividing by zero. Try changing the second number." + Fore.RESET)
        elif isinstance(exception, ValueError):
            print(f"{Fore.RED}Invalid input: Please input numbers only" + Fore.RESET)
        else:
            print(f"{Fore.RED}Please enter a valid input" + Fore.RESET)
    
    #Raise Value Error
    def raise_error(self, operation):
        #Initializing operator symbols
        operators = ["+", "-", "*", "/", "^", "="]
        #If statement
        if  operation not in operators:
            #Error Message
            print(f"{Fore.RED}Sorry, operation should only be +, -, *, or /" + Fore.RESET)
            #Retrying program
            retry = ui.retry_option()
            return retry
    