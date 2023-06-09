#Procedural Version

#Initialize retrying variable
retry = "y"
#Loop condition
while retry == "y":
    #Use Python Function and appropriate Exceptions to capture errors during runtime.
    while True:
        #Try function to test the block of codes
        try:
            #Display instructions regarding the operations
            print (" Enter + if Addition \n Enter - if Subtraction \n Enter * if Multiplication \n Enter / if Division")
            #Ask the user to enter their chosen operation
            operation = input("Please enter the corresponding symbol for your chosen operator: ")
            operators = ['+', '-', '*', '/']
            if  operation not in operators:
                raise Exception("Sorry, operation should only be +, -, *, or /:") 
            #Ask the user for two numbers
            num1 = float(input("Please input the first number: "))            
            num2 = float(input("Please input the second number: "))
            #Perform the operation chosen with the two numbers
            #If operation is addition
            if operation == "+":
                result = num1 + num2     
            #If operation is subtraction
            elif operation == "-":
                result = num1 - num2
            #If operation is multiplication
            elif operation == "*":
                result = num1 * num2
            #If operation is division
            elif operation == "/":
                result = num1/num2
            #Display the result
            print(result)
        #Except function to handle errors
        except ZeroDivisionError:
            print("Sorry! You are dividing by zero. Try changing the second number.")
        except ValueError:
            print("Invalid input: Please input numbers only")
        except Exception:
            print("Sorry, input should only be +, -, *, or /d")             
        break
        #Ask if the users if they want to try again or not.
    retry = input("Do you want to try again?(Enter 'y' if yes and any key if no) ")
    #If yes, the program will repeat Step 1.
#If no, the program will display “Thank you!” and the program will exit
print("Thank you!")