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
            print("Sorry! You are dividing by zero. Try changing the second number.")
        elif isinstance(exception, ValueError):
            print("Invalid input: Please input numbers only")
        else:
            print("Please enter a valid input")
    
    #Raise Value Error
    def raise_error(self, operation):
        #Initializing operator symbols
        operators = ["+", "-", "*", "/"]
        #If statement
        if  operation not in operators:
            #Error Message
            print("Sorry, operation should only be +, -, *, or /")
            #Retrying program
            retry = ui.retry_option()
            return retry
    