#This python file will serve as the execution file of the program version executed through tkinter.

#Import class files
from calc_main import MainCalculator
from prog_gui import TkMethods
#Import modules
import tkinter as tk

#Initialize classes
main_calc = MainCalculator
tk = TkMethods

#Call main calculator
main_calc.main_calculator()

