#Kate Eurisse Martinez_BSCPE 1-5_Simple App Calculator - OOP Version

#This program will create a Simple App Calculator; where the user will input the operation as well as the two numbers that they want to calculate.
#The program will use exception handling (try-catch method) to handle user input errors.
#The program will be executed in an Object oriented programming way 

#====================================Under Maintenance(hshs)=======================================
import tkinter as tk
from PIL import Image, ImageTk

#Import class files
from user_interface import UserInterface
from calculation_file import Calculator
from exception_file import Exceptions
from tk_methods import TkMethods

#Initialize variables(modules)
ui = UserInterface()
calc = Calculator()
exception = Exceptions()
gui = TkMethods()

#Calculator window
def calculator_window():
    def calculator():
        #Try function to test the block of codes
        try: 
            #Ask the user to choose one of the four math operations
            operation = ui.operation_input() 
            exception.raise_error(operation)
            
            #Ask the user for two numbersa
            num1 = ui.num_input()
            num2 = ui.num_input()

            #Perform the operation chosen with the two numbers
            result = calc.calculations(operation, num1, num2)

            #Display the result
            ui.display_result(result)

        #Except function to handle errors
        except Exception as errors:
            exception.except_condition(errors)
    
    #Retrying option
    def retry_calc():
        ui.retry_option()
    #Quit the calculator window
    def quit_calc():
        ui.quit_calculator()

    #Call calculator window
    gui.calculator_window()

#Ending window
def ending_window():
    gui.create_ending_window()

#Calling introduction window
gui.introduction_window()
