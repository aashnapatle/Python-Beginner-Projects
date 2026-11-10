try:
     
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    c=input("enter what operation you would like to perform \n press + for addition \n press - for subtraction \n press * for multiplication \n press / for division ")
    match c:
        case "+" :
                    print(f"the result is :{a+b}")
        case "-" :
                    print(f"the result is :{a-b}")
        case "*" :
                    print(f"the result is :{a*b}")
        case "/" :
                    print(f"the result is :{a/b}")
        case _:
                    print("there was an error")                                    
except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Please enter valid numbers!")

except Exception as e:
    print("An error occurred:", e)
       