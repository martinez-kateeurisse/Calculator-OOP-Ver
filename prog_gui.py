#This python file will have the methods relating to program's tkinter execution.
import tkinter as tk 
#Create class
class TkMethods:
#Creeate Window
    def tk_window():
        calc_window = tk.Tk()
        calc_window.title("Simple App Calculator") #Window Title
        calc_window.geometry("400x300") #Window Size
        calc_window.configure(bg="light cyan") #Window background#Create Labels
    #Ask the user to enter the operation
        label_operator = tk.Label(calc_window, text="Operations (+, -, *, /):")
        label_operator.grid(row=1, column=0, padx=10, pady=10)
        #Ask the user to input the first number
        label_num1 = tk.Label(calc_window, text="Please input the first number:")
        label_num1.grid(row=2, column=0, padx=10, pady=10)
        #Ask the user to input the second number
        label_num2 = tk.Label(calc_window, text="Please input the second number:")
        label_num2.grid(row=3, column=0, padx=10, pady=10)
        #Ask the user if they want to try again
        label_retry = tk.Label(calc_window, text="Do you want to try again?")
        label_retry.grid(row = 6, column = 0, padx=10, pady=10)
        #Displaying the result
        label_result = tk.Label(calc_window, text="The answer is: ")
        label_result.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
    #Create Input Fields
        #Input for the operation
        input_operation = tk.Entry(calc_window)
        input_operation.grid(row=1, column=1, padx=10, pady=10)
        #Input for the first number
        input_num1 = tk.Entry(calc_window)
        input_num1.grid(row=2, column=1, padx=10, pady=10)
        #Input for the second number
        input_num2 = tk.Entry(calc_window)
        input_num2.grid(row=3, column=1, padx=10, pady=10)
    #Create Buttons
        #Button for calculating the result
        button_calculate = tk.Button(calc_window, text="Calculate the Result", command=calculator)
        button_calculate.grid(row=4, column=1, padx=10, pady=10)
        #Yes button - If yes, the program will repeat step 1
        button_yes = tk.Button(calc_window, text="Yes", command=retry)
        button_yes.grid(row=4, column=1, padx=10, pady=10)
        #No button - If no, the calculator program will exit
        button_no = tk.Button(calc_window, text="No", command=quit_calculator)
        button_no.grid(row=4, column=2, padx=10, pady=10)
    #Organize the buttons
        button_calculate.grid(row=4, column=0, pady=10)
        button_yes.grid(row=6, column=1, pady=10)
        button_no.grid(row=6, column=2, pady=10)