#This class file will include the exception handling codes.

#Create Class
class Exceptions:
#Create Object
    def except_condition(self, exception):
#Create instance variables
        if isinstance(exception, ZeroDivisionError):
            print("Sorry! You are dividing by zero. Try changing the second number.")
        elif isinstance(exception, ValueError):
            print("Invalid input: Please input numbers only")
        else:
            print("Please enter a valid input")
    def raise_error(self, operation):
        operators = ["addition", "subtraction", "multiplication", "division"]
        if  operation not in operators:
            print("Sorry, operation should only be addition, subtraction, multiplication, or division")
            
    