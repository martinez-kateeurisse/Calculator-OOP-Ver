#Import File to be inherited
from calculation_file import Calculator

#Create class 
class CalcModified(Calculator):   
#Add methods
    def calculations (self, operation, num1, num2):
        #Power operation
        if operation == "^":
        #Perform operation
            result = num1**num2
        #Return result
            return result
        
        #Determining numbers are greater, lesser or equal
        if operation == "=":
            #If num 1 is greater
            if num1 > num2:
                result = str(num1) + "is greater than" + str(num2)
                return result
            #If num 2 is greater
            elif num1 < num2:
                result = str(num1) + "is less than" + str(num2)
                return result
            #If equal
            else:
                result = "The numbers you've entered are equal"
                return result