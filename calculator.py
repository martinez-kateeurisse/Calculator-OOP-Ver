#This class file will include codes that require performing calculations.

#Create class file
class Calculator():
    #Create objects
    #Create variable instances
    def calculations (self, operation, num1, num2):
    #If addition
        if operation == "+":
        #Perform operation
            result = num1 + num2
        #Return result
            return result
    #If subtraction
        elif operation == "-":
        #Perform operation
            result = num1 - num2
        #Return result
            return result    
    #If multiplication
        elif operation == "*":
        #Perform operation
            result = num1 * num2
        #Return result
            return result  
    #If division
        elif operation == "/":
        #Perform operation
            result = num1 / num2
        #Return result
            return result
