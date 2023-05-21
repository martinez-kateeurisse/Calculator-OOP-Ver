#This class file will include the codes that require a user interface.

#Create class
class UserInterface:    
#Create objects
    #Operation 
    def operation_input(self):
        #Create instance variables
        #Ask user for Operation
        operation = input("Please enter the operation: ")
        #Return the value
        return operation
    #Numbers
    def num_input(self):
        #Ask user for numbers
        num = float(input("Please input a number: "))
        #Return the value
        return num
    
    #Display Results
    def display_result(self, result):
        print("RESULTING VALUE: " + str(result))
    
    #Retry
    def retry_option(self):
        #Ask users if they want to try again
        retry = input("Do you want to try again?(Enter 'y' if yes and any key if no): ")
        #Return the value
        return retry