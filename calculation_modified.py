#Import File to be inherited
from calculation_file import Calculator

#Create class 
class CalcModified(Calculator):   
#Add methods
    def calculations (self, operation, num1, num2):
        #Power
        if operation == "^":
        #Perform operation
            result = num1**num2
        #Return result
            return result