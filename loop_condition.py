#This class file will include the codes for loop conditions.

import tkinter as tk
#Create class
class LoopCondition:   
    def retry_prog(self, input_num1, input_num2, input_operation,label_result):
        input_num1.delete(0, tk.END)
        input_num2.delete(0, tk.END)
        input_operation.delete(0, tk.END)
        label_result.config(text="RESULTING VALUE: ")

    #Define a  variable to quit the calculator window
    def quit_calculator(self, calc_window):
        calc_window.destroy()
