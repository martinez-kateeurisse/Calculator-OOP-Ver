#This class file will include the exception handling codes.

from user_interface import UserInterface
ui = UserInterface

#Create Class
class Exceptions:
#Create Objects
    def except_condition(self, exception):
    #Create instances
        #Exception errors
        if isinstance(exception, ZeroDivisionError):
            self.label_result.config(text="Sorry! You are dividing by zero. Try changing the second number.")
        elif isinstance(exception, ValueError):
            self.label_result.config(text="Invalid input: Please input numbers only")
        else:
            self.label_result.config(text = "Invalid input: Please enter a valid input")
    #Raise Value Error
    def raise_error(self, operation):
        #Initializing operator symbols
        operators = ["+", "-", "*", "/"]
        #If statement
        if  operation not in operators:
            #Error Message
            self.label_result.config(text="Sorry, operation should only be +, -, *, or /")