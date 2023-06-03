#Kate Eurisse Martinez_BSCPE 1-5_Simple App Calculator - OOP Version

#This program will create a Simple App Calculator; where the user will input the operation as well as the two numbers that they want to calculate.
#The program will use exception handling (try-catch method) to handle user input errors.
#The program will be executed in an Object oriented programming way 

#Import color modules
import colorama
from colorama import Back, Fore, Style 
#colorama.init(autoreset = True)

#Import class files
from user_interface import UserInterface
from calculation_file import Calculator
from loop_condition import LoopCondition
from exception_file import Exceptions
from prog_design import ProgramDesign
from ui_modified import UiModified

#Initialize variables(modules)
ui = UserInterface()
calc = Calculator()
loop = LoopCondition()
exception = Exceptions()
prog_design = ProgramDesign()
ui_mod = UiModified()

#Program header
prog_design.program_header()

#Displaying greetings and instructions
ui.user_greeting()

#Loading bar
prog_design.loading_bar()

#Show operation instructions
ui.show_instructions()
#Initialize retrying variable
retry = 'y'
while loop.retry_prog(retry): 
    #Try function to test the block of codes
    try:
        #Displaying operator art
        prog_design.operators() 

        #Ask the user to choose one of the four math operations
        operation = ui.operation_input() 
        #Raising Exception
        exception.raise_error(operation)
        
        #Displaying Numbers art
        prog_design.numbers()
        #Ask the user for two numbersa
        num1 = ui.num_input()
        num2 = ui.num_input()

        #Perform the operation chosen with the two numbers
        result = calc.calculations(operation, num1, num2)

        #Display the result
        ui.display_result(result)
        
        #Ask if the user wants to try again or not.
        retry = ui.retry_option()
        #If yes, repeat Step 1.
        #If no, Display “Thank you!” and the program will exit 

    #Except function to handle errors
    except Exception as errors:
        exception.except_condition(errors)