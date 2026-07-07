#-------------- Simple Calculator ------------------

def calculator(a,b):
    print(" Multi of a and b is :- ",a*b)
    print(" Multi of a and b is :- ",a+b)
    print(" Multi of a and b is :- ",a-b)
    print(" Multi of a and b is :- ",a/b)
    print(" Multi of a and b is :- ",a%b)
calculator(12,2)


# -------------------------------------------------
num1 = int(input("Enter your first nnumber for calculation :- "))
num2 = int(input("Enter your Second nnumber for calculation :- "))
opt  = input("Select the operator you want to use :-    " )

if num1 <= 0:
    print("calculation with 0 not possible :-")
elif opt == "+":
    print(" Sum of a and b is :-",num1+num2)  
# --------------------------------------------------------



def calculator():
    while True:
        try:
            a = float(input("Enter your first nnumber for calculation :- "))
            b  = float(input("Enter your Second nnumber for calculation :- "))
            opt  = input("Select the operator (+, -, *, /, %) or type 'exit' to leave: :-    " ).strip()
        except ValueError :
            print("Error: Please enter valid numbers")
            continue
        # exit = input(" Type exit to leave :- ").lower.strip()
        
        if opt == "exit":
            print(" Exiting calculator . Goodbye!")
            break
        try:
            if opt == "*":
                print(f"Multi of a and b is :- {a*b}")
                
            elif opt == "+":
                print(" Sum of a and b is :-         ",a+b)
                
            elif opt == "-":
                print(" Subtraction of a and b is :- ",a-b)
                
            elif opt == "/":
                
                try:
                    print(" Divison of a and b is :-     ",a/b)
                except ZeroDivisionError:
                    print(" Error: Divison by zero is not allowed ")
            elif opt == "%":
                print(" Modulos of a and b is :-     ",a%b)
                
            else:
                print(" Choose correct opt ")
        except ValueError:
            print("Error: Please enter valid numbers.")

calculator()



