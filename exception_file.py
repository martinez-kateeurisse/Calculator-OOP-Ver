#This class file will include the exception handling codes.

#Create Class
class Exceptions:
#Create Object
    def except_condition(exception):
#Create instance variables
        if isinstance(exception, ZeroDivisionError):
            print("Sorry! You are dividing by zero. Try changing the second number.")
        elif isinstance(exception, ValueError):
            print("Invalid input: Please input numbers only")
        elif isinstance(exception):
            print("Sorry, input should only be +, -, *, or /d")             