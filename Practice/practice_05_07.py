# Check Spam or not 

massage = input(" Enter your massage to check Spam or not :- ").lower().strip()
keywords = ["free","win","price","free money","won","click to grabe","giveaway","loan","big profit",]
if any (keyword in massage for keyword in keywords):
    print(" Message is Spam 💀")
else:
    print("Normal Message ")
    
    
#--------------------------------------------------
# Check message spam or not using count if keyword have 2 value in message it declare Spam

message = input("Enter your message to check Spam or not :- ").lower().strip()

keywords = ["free", "win", "price", "free money", "won", "click to grabe", "giveaway", "loan", "big profit"]

# Count how many keywords are present in the message
count = sum(1 for keyword in keywords if keyword in message)

if count >= 2:
    print("Message is Spam 💀")
else:
    print("Normal Message 🙂")

#---------------------------------------------------

# Simple List of Dictionaries 
data = [
    {"name":"deep","age":23,"id":765},
    {"name":"aman","age":24,"id":766},
    {"name":"rahul","age":22,"id":767},
    {"name":"harry","age":21,"id":768},
    {"name":"hardeep","age":23,"id":769},
    {"name":"rohit","age":25,"id":770},
]
for s in data:
    print("Student Name :-",s["name"],
    "| Age :-",s["age"],
    "| ID :-",s["id"])
    
#------------------------------------------------------------

# PRINT Avg Highest 
   
students =[   # students is a variable and we store dictionaries in list 
    {"name":"Deepak","marks":89},  # Their are no extra spaces in key 
    {"name":"Rahul","marks":65},
    {"name":"simran","marks":80},
    {"name":"Harry","marks":45},
]
total = 0       # initilize total = 0
highest = 0
highest_student = ""   # for now their is no value in this 
for data in students:   # data = students
    print("Student name",data["name"])  
    print("Student Marks",data["marks"])
    total = total + data["marks"]
    if data["marks"]> highest:
        highest = data["marks"]
        highest_student = data["name"]
    if data["marks"] >= 60:
        print("PASS")
    else:
        print("FAIL")
        
avg = total/len(students)
print("Average Marks :- ",avg)
print("Highest Marks :-",highest_student,highest)
    
