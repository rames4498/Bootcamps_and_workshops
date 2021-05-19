
# username and password verification
# rules for username validation
  # @ and . followed by it
  # mail should not start with special characters , like #ser@gmail.com
# rules for password validation
  # length 6 to 15
  # atleast one lowercase
  # atleast one uppercase
  # atleast one special character
  # alteast one digit

# shall we....

speChar = "!@#$%&(){}[]_"
speChar =  list(speChar)

def Login():
    mail =  input("Enter your username to login " )
    passwd = input("Enter your password to login " )
    for line in open("kgisl_database.txt", "r").readlines():
        flag  =  True
        data  = line.split()  # result an array (here list)
        if mail == data[0] and passwd == data[1]:
            print("you are successfully logged into your account")
        else:
            flag = False
    if flag  == False:
        print("your login credentials are wrong, please try to register if you are new user")

    

def Registration():
    def password(passwd):

        k,c,d,j = 0,0,0,0

        for b in passwd:
            if b.isupper():  # will return boolean TRUE if the character is uppercase
                k = k+1
            if b.islower():  # will return boolean TRUE if the character is lowercase
                c = c + 1
            if b.isdigit():
                d  = d + 1
            if (k and c and d)>0:
                break
        for s in speChar:
            if s in passwd:
                j = j + 1
        if (5<len(passwd)<16) and ((k and c and d and j)>0):
            print("valid password")
            myfile  = open("kgisl_database.txt","a")
            myfile.write(mail)
            myfile.write(" ")
            myfile.write(passwd)
            myfile.write("\n")
            myfile.close()
            
        else:
            print("Invalid password")
                

    def username(mail):
        for h in mail:
            if h == "@":
                r  = mail.index(h)     # index value of @
                for l in range(r, len(mail)):
                    flag  =  True 
                    if mail[l] == ".":
                        print("valid email id")
                        password(passwd) # can call the password function only if my username is valid
                        break
                    else:
                        flag  = False
                if flag == False:
                    print("Invalid email id ")
                        
    
    mail =  input("please enter your valid email id ") # email id  . eg: ganesh@gmail.com
    passwd =  input("please enter your valid password ") # password eg: Idontknow@123
    username(mail)

print("Welcome to Facebook")
print("choose any option which suits you")
print("Enter 1 to Register, if you are a new user")
print("Enter 2 to Login, if you are an existing user")

userInput = input("Enter your choice : ")

if userInput == "1":
    Registration()
else:
    Login()






    
