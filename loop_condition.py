#This class file will include the codes for loop conditions.

import tkinter as tk
#Create class
class LoopCondition:
#Create Object
    def retry_prog(self, retry):
    #Create variable instances(if-else condition)
        if retry == 'y':        
    #Return value
            return retry
        else:
            print("Thank you!")
    
    def retry(input_num1, input_num2, input_operation,label_result):
        input_num1.delete(0, tk.END)
        input_num2.delete(0, tk.END)
        input_operation.delete(0, tk.END)
        label_result.config(text="The answer is: ")

    #Define a  variable to quit the calculator window
    def quit_calculator(calc_window):
        calc_window.quit()
