while True:
    correct_password = "password123"
    correct_username = "Deepak@123"
    choice = input("Login or Signup? (login/signup/exit): ").strip().lower()

    if choice == "login":
        username = input("Enter username:- ")
        password = input(" Enter your password :-")
        if username == correct_username and password == correct_password:
            print("login Successful ") 
            
        else:
            print(" X Login Failed")
            if username != correct_username:
                print(" Invalid Username ")
            if password != correct_password:
                print( " Invalid Password ")
            
        # Add your login password code here

    elif choice == "signup":
        username = input("Enter username: ")
        password = input("Enter password: ")
        print("Signup successful!")
        break
    elif choice == "exit":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please type login, signup, or exit.")




#------------------- FIND SUM --------------------------

sum = 0       # initialize and declare sum value = 0 
num = int(input("Enter the Number which you want to find the Sum :- "))
for i in range (1,num+1):  # start from 1 go to num value like 10 sum hoga first 10 number kaa 1 to 10
    sum += i               # it will increase the  value of sum till than n 
    # 1
    # 1+2 = 3
    # 3+3 = 6
    # 6+4 = 10 and so on 
print(sum)               # agar print to for kae nadar likh do to har ik number add hone par show hoga but now 
                        # print for kae andar nahi hai to total sum print karega 
                        


#------------------- Print Table -------------------------
num = int(input(" Enter the number you want a Table :- "))
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")
    
# ---------------------- Print Multiple Table ----------------------
num1 = int(input("Enter the first number to start tables: "))
num2 = int(input("Enter the last number to end tables: "))
for i in range (num1,num2+1):
    for j in range (1,11):
        print(f"{i} X {j} = {i*j}")
    print()
