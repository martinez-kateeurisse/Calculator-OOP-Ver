#This class file will include the codes that require a user interface.
from colorama import Back, Fore, Style 
#Create class
class UserInterface:    
    #Create objects

    #Operation Instructions
    def __init__(self):
        self.intro = f"{Fore.LIGHTRED_EX} Enter + if Addition \n Enter - if Subtraction \n Enter * if Multiplication \n Enter / if Division \n" + Fore.RESET
    def show_instructions(self):
        #Printing the operation instructions
        print(self.intro)   

    #Operation 
    def operation_input(self):
        #Create instance variables
        #Ask user for Operation
        operation = input(f"{Fore.LIGHTCYAN_EX}Please enter the operation: "+Fore.RESET)
        #Return the value
        return operation
    
    #Numbers
    def num_input(self):
        #Ask user for numbers
        num = float(input(f"{Fore.LIGHTGREEN_EX}Please input a number: "+Fore.RESET))
        #Return the value
        return num
    
    #Display Results
    def display_result(self, result):
        print(f"{Fore.LIGHTYELLOW_EX}RESULTING VALUE: " + str(result) + Fore.RESET)
    
    #Retry
    def retry_option(self):
        #Ask users if they want to try again
        retry = input(f"{Fore.LIGHTMAGENTA_EX}Do you want to try again?(Enter 'y' if yes and any key if no): "+ Fore.RESET)
        #Return the value
        return retry