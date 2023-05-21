#Kate Eurisse Martinez_BSCPE 1-5_Simple App Calculator - OOP Version

#This program will create a Simple App Calculator; where the user will input the operation as well as the two numbers that they want to calculate.
#The program will use exception handling (try-catch method) to handle user input errors.
#The program will be executed in an Object oriented programming way 

#Import class files
from user_interface import UserInterface
from calculator import Calculator
from loop_condition import LoopCondition
from exception_file import Exceptions

#Initialize variables
ui = UserInterface()
calc = Calculator()
loop = LoopCondition()
exception = Exceptions()

#Initialize 
#retry = 'y'
while loop.retry_prog(): 
    try: 
        ui.show_instructions()
        #Ask the user to choose one of the four math operations (Addition, Subtraction, Multiplication and Division)
        operation = ui.operation_input() 
        exception.raise_error(operation)
        
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
#Use Python Function and appropriate Exceptions to capture errors during runtime.
    except Exception as errors:
        exception.except_condition(errors)