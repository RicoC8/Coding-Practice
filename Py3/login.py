user_data = {
    'Admin' : {'Phone': '+62817', 'Safety Word': 'dog', 'Password': 'admin'}
}

def login():
    username = (input("Enter Username: "))
    pw = input("Enter Password: ")
    safety = input("Enter Safety Word: ")
    user_info = user_data.get(username, False)
    if user_info == False:
        print("User does not exist!")
        return
    else:
        if pw == user_info.get('Password') and safety == user_info.get('Safety Word'):
            print("Login Success!")
        else: 
            print("Login FAILED! Please try again")
            
login()