students_data = [] #list storing all data
FIELDS = ["Username", "Password", "Full Name", "Email",
          "Phone Num","DOB", "Address",
          "Course", "Enrollment Year", "Student ID"]

logged_user = '' #global variable
logged = False #global variable

def register() :
    print("\nNew Student Registration\n")
    new_student = {} #studnet data dictionary

    for field in FIELDS :
        value = input(f"Enter {field} : ")
        new_student[field] = value

    for student in students_data: #if username already present
        if student["Username"] == new_student["Username"]:
            print("\nUsername not available")
            return

    students_data.append(new_student)
    print("\nRegistration successful")

def login():
    global logged, logged_user #global needed to modify values
    
    print("\nStudent Login\n")
    username = input("Enter username : ")
    password = input("Enter password : ")

    for student in students_data:
        if student["Username"] == username and student["Password"] == password:
            logged = True
            logged_user = username
            print(f"\nLogin successful, Welcome {username}")
            return

    print("\nError: Invalid username or password\n")

def show_profile():
    if logged == False : #no need for global for accessing values
        print("\nPlease log in")
        return
        
    print(f"\nProfile details of {logged_user}\n")
    for student in students_data:
        if student["Username"] == logged_user:
            for key, value in student.items():
                if key == "Password" : #hide pass
                    print("Password : ********")
                else :
                    print(f"{key}: {value}")
            return

def update_profile():
    if logged == False :
        print("\nPlease log in")
        return
        
    print("\nUpdate Your Profile\n")
    for student in students_data:
        if student["Username"] == logged_user:
            field_update = input("Enter Field to update : ")
            
            if field_update in student:
                new_value = input(f"Enter new value for {field_update} : ")
                student[field_update] = new_value
                print("\nProfile updated\n")
            else:
                print("\nInvalid field\n")
            return

def logout():
    global logged, logged_user
    if logged == True :
        print(f"{logged_user} is logged out")
        logged = False
        logged_user = ''
    else:
        print("You are not logged in")

def terminate():
    """Exits the program."""
    print("Exiting program.")
    exit()

def main(): 
    while True: #program loop
        print("\nWELCOME TO LNCT\n")
        if logged == True :
            print(f"(Logged in as: {logged_user})")
        
        response = input(
            "OPTIONS\n\n"
            "1 - Register\n"
            "2 - Login\n"
            "3 - Show Profile\n"
            "4 - Update Profile\n"
            "5 - Logout\n"
            "6 - Exit\n"
            "\nChoose option number: ")
        
        if   response == '1': register()
        elif response == '2': login()
        elif response == '3': show_profile()
        elif response == '4': update_profile()
        elif response == '5': logout()
        elif response == '6': terminate()
        else:
            print("Invalid Choice, please try again.")

main()
