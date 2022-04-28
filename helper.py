print("Note + = Addition - = Subtraction % = remainder * = multiplication / = division // = floor division ** exponent")

Operation = (input("What type of operation would you like to do?: "))
if (Operation == "+"):
    Num1 = float(input("Pick a number: "))
    Num2 = float(input('Pick another number to add: '))
    Result = Num1 + Num2
    print(Result)
elif (Operation == "-"):
    Num1 = float(input("Pick a number: "))
    Num2 = float(input("Pick another number to subtract: "))
    Result = Num1 - Num2
    print(Result)
elif (Operation == "%"):
    (Num1) = float(input("Pick a number: "))
    (Num2) = float(input("Pick another number to find the reminder: "))
    Result = Num1 % Num2
    print(Result)
elif (Operation == "*"):
    Num1 = float(input("Pick a number: "))
    Num2 = float(input("Pick another number to multiply: "))
    Result = Num1 * Num2
    print(Result)
elif (Operation == "/"):
    Num1 = float(input("Pick a number: "))
    Num2 = float(input("Pick another number to divide: "))
    Result = Num1 / Num2
    print(Result)
elif (Operation == "//"):
    Num1 = float(input("Pick a number: "))
    Num2 = float(input("Pick another number to floor division: "))
    Result = Num1 // Num2
    print(Result)
elif (Operation == "**"):
    Num1 = float(input("Pick a number: "))
    Num2 = float(input("Pick another number to be the exponent: "))
    Result = Num1 ** Num2
    print(Result)
else:
    print ("Not a valid Operator")
