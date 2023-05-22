#Kate Eurisse Martinez_BSCPE 1-5_Simple App Calculator - OOP Version

#This program will create a Simple App Calculator; where the user will input the operation as well as the two numbers that they want to calculate.
#The program will use exception handling (try-catch method) to handle user input errors.
#The program will be executed in an Object oriented programming way 

#import tkinter as tk
#Import class files
from user_interface import UserInterface
from calculator import Calculator
from loop_condition import LoopCondition
from exception_file import Exceptions
from prog_gui import TkMethods

#Initialize variables(modules)
ui = UserInterface()
calc = Calculator()
loop = LoopCondition()
exception = Exceptions()
gui = TkMethods ()
#gui = TkMethods()
class MainCalculator:
    def main_calculator(self):
        #Show operation instructions
        ui.show_instructions()
        #Initialize retrying variable
        #retry = 'y'
        #while loop.retry_prog(retry): 
            #Try function to test the block of codes
        try: 
            #Ask the user to choose one of the four math operations
            self.operation = ui.operation_input().get() 
            exception.raise_error(self.operation)
                
            #Ask the user for two numbersa
            self.num1 = ui.num_input1()
            self.num2 = ui.num_input2()

            #Perform the operation chosen with the two numbers
            result = calc.calculations(self.operation, self.num1, self.num2)

            #Display the result
            self.result = ui.display_result(result)
            self.gui.label_result.config(text="RESULTING VALUE: " + str(result))
        #Except function to handle errors
        except Exception as errors:
            exception.except_condition(errors)

                #Ask if the user wants to try again or not.
    #retry = loop.retry_prog()
                #If yes, repeat Step 1.
                #If no, Display “Thank you!” and the program will exit 
loop.retry_prog()
#Window
gui.tk_window()

#Labels
gui.labels()

#Input Fields
gui.input_fields()

#Buttons
gui.buttons()
