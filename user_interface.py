#This class file will include the codes that require a user interface.

import tkinter as tk
from tk_methods import TkMethods

gui = TkMethods
#Create class
class UserInterface:    
    #Create objects
    
    def show_instructions(self):
        #Printing the operation instructions
        print(self.intro)   

    #Operation 
    def operation_input(self):
        #Create instance variables
        #Ask user for Operation
        operation = self.input_operation.get()
        #Return the value
        return operation
    
    #Numbers
    def num_input(self):
        #Ask user for numbers
        num1 = float(self.input_num1.get())
        num2 = float(self.input_num2.get())
        #Return the value
        return num1, num2

    #Display Results
    def display_result(self, result):
        self.label_result.config(text="RESULTING VALUE: " + str(result))
    
    #Retry
    def retry_option(self):
        self.input_num1.delete(0, tk.END)
        self.input_num2.delete(0, tk.END)
        self.input_operation.delete(0, tk.END)
        self.label_result.config(text="RESULTING VALUE: ")
    
    #Quit
    def quit_calculator(self):
        self.calc_window.destroy()  # Close the calculator window
        self.create_ending_window()
    
    #Opening calculator
    def open_calculator(self):
        self.introduction_window.destroy()  # Close the introduction window
        self.calculator_window()