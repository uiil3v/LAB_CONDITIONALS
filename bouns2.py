name = input("Enter Your Name: ")
email = input("Enter Your Email: ")

if len(name) > 2 and email.endswith("@gmail.com"):
    print(f"welcome {name}, you registered with the email {email} !")
else:
    if len(name) <=2 and not email.endswith("@gmail.com"):
        print("Both are wrong")
    elif len(name) <=2:
        print("the name length must be more than 2 characters, please provide a valid name.")
    elif not email.endswith("@gmail.com"):
        print("the email is not valid , please provide a valid email.")
