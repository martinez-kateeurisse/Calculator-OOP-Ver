#This python file will serve as the execution file of the program version executed through tkinter.

#Import modules
import tkinter as tk

#Import class files
from calc_main import MainCalculator
from prog_gui import TkMethods
from loop_condition import LoopCondition


#Initialize classes
main_calc = MainCalculator()
gui = TkMethods ()
loop = LoopCondition()

main_calc.main_calculator()

loop.retry_prog()
#Window
gui.tk_window()

#Labels
gui.labels()

#Input Fields
gui.input_fields()

#Buttons
gui.buttons()

#Organize buttons
gui.organize_buttons()

#Start Mainloop
gui.main_loop()