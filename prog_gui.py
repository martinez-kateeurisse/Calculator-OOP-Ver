#This python file will have the methods relating to program's tkinter execution.
import tkinter as tk 
from loop_condition import LoopCondition
loop = LoopCondition
from calc_main import MainCalculator
calc = MainCalculator
#Create class
class TkMethods:
#Creeate Window
    def tk_window(self):
        self.calc_window = tk.Tk()
        self.calc_window.title("Simple App Calculator") #Window Title
        self.calc_window.geometry("400x300") #Window Size
        self.calc_window.configure(bg="light cyan") #Window background#Create Labels
    #Ask the user to enter the operation
        self.label_operator = tk.Label(self.calc_window, text="Operations (+, -, *, /):")
        self.label_operator.grid(row=1, column=0, padx=10, pady=10)
        #Ask the user to input the first number
        self.label_num1 = tk.Label(self.calc_window, text="Please input the first number:")
        self.label_num1.grid(row=2, column=0, padx=10, pady=10)
        #Ask the user to input the second number
        self.label_num2 = tk.Label(self.calc_window, text="Please input the second number:")
        self.label_num2.grid(row=3, column=0, padx=10, pady=10)
        #Ask the user if they want to try again
        self.label_retry = tk.Label(self.calc_window, text="Do you want to try again?")
        self.label_retry.grid(row = 6, column = 0, padx=10, pady=10)
        #Displaying the result
        self.label_result = tk.Label(self.calc_window, text="The answer is: ")
        self.label_result.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
    #Create Input Fields
        #Input for the operation
        self.input_operation = tk.Entry(self.calc_window)
        self.input_operation.grid(row=1, column=1, padx=10, pady=10)
        #Input for the first number
        self.input_num1 = tk.Entry(self.calc_window)
        self.input_num1.grid(row=2, column=1, padx=10, pady=10)
        #Input for the second number
        self.input_num2 = tk.Entry(self.calc_window)
        self.input_num2.grid(row=3, column=1, padx=10, pady=10)
    #Create Buttons
        #Button for calculating the result
        self.button_calculate = tk.Button(self.calc_window, text="Calculate the Result", command=calc.main_calculator)
        self.button_calculate.grid(row=4, column=1, padx=10, pady=10)
        #Yes button - If yes, the program will repeat step 1
        self.button_yes = tk.Button(self.calc_window, text="Yes", command=loop.retry)
        self.button_yes.grid(row=4, column=1, padx=10, pady=10)
        #No button - If no, the calculator program will exit
        self.button_no = tk.Button(self.calc_window, text="No", command=loop.quit_calculator)
        self.button_no.grid(row=4, column=2, padx=10, pady=10)
    #Organize the buttons
        self.button_calculate.grid(row=4, column=0, pady=10)
        self.button_yes.grid(row=6, column=1, pady=10)
        self.button_no.grid(row=6, column=2, pady=10)