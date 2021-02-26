import json
user=input("You wants to 1.signup or 2.login:-")
if user=="1":
    user_name=input("Enter Your Username:-")
    mydata=open("data.json","r")
    read_data=mydata.read()
    if user_name in read_data:
        print("user_name already exists")
    else:
        password_1=input("Enter Your first Password:-")
        if "#" in password_1 or "@" in password_1 :
            password_2=input("Re-write the password:-")
            if password_1==password_2:
                print("Congrats", user_name, "you are signed up success fully")
                Discription=input("Enter Your Discription:- ")
                DOB=input("Enter Your Date of Birth :- ")
                Hobbie=input("Enter Your Hobbie :-")
                Gender=input("Enter Your Gender Male/Female/Other:-")
                user_details={"User" : {"username":  user_name, "Password": password_1, "Profile" : {"Discription" : Discription , "DOB":DOB, "Hobbie": Hobbie , "Gender": Gender}}}
                myfile=open("data.json", "a")
                mydata=json.dumps(user_details)
                myfile.write(mydata)
                print()
                print(mydata)
            else:
                print("wrong password Please check once")
        else:
            print("Atleast Password should contain one special character and one number")
            print("Write answer properly")
elif user=="2":
    user_name=input("Enter Your Username:-")
    password=input("Enter Your password:-")
    open_file=open("data.json","r")
    read_data1=open_file.read()
    if user_name in read_data1:
        if password in read_data1:
            print("login successfully")
            with open("data.json") as data_file:    
                data = json.load(data_file)
                users = data['User']
                for user in users:
                    count=0
                    print ("users full name and password is ", users["username"] , users["Password"])
                while count<1:
                    print("profile")
                    print("Discription : ", users["Profile"]["Discription"])
                    print("DOB : ", users["Profile"]["DOB"])
                    print("Hobbie : ", users["Profile"]["Hobbie"])
                    print("Gender : ", users["Profile"]["Gender"])
                    count+=1
        else:
            print("password is incorrect")
    else:
        print("invalid User_Name")


