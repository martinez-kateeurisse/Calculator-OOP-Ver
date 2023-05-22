#This class file will include the codes that require a user interface.

#Create class
class UserInterface:    
    #Create objects

    #Operation Instructions
    def __init__(self):
        self.intro = " Enter + if Addition \n Enter - if Subtraction \n Enter * if Multiplication \n Enter / if Division"
    def show_instructions(self):
        #Printing the operation instructions
        print(self.intro)   

    #Operation 
    def operation_input(self, input_operation):
        #Create instance variables
        #Ask user for Operation
        operation = input_operation.get()
        #Return the value
        return operation
    
    #Numbers
    def num_input1(self, input_num1):
        #Ask user for numbers
        num1 = float(input_num1.get())
        #Return the value
        return num1 
    def num_input2(self, input_num2):
        #Ask user for numbers
        num2 = float(input_num2.get())
        #Return the value
        return num2
        
    #Display Results
    def display_result(self, result):
        return (result)
    
    #Retry
    #def retry_option(self):
        #Ask users if they want to try again
        #retry = input("Do you want to try again?(Enter 'y' if yes and any key if no): ")
        #Return the value
        #return retry