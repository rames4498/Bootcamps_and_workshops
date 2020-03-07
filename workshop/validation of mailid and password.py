
a = 0
spec =  "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
spec = list(spec)
#print(spec)
def password(m):
    k,c,d,j = 0,0,0,0
    for b in n:
        if b.isupper():
            k = k+1
        if b.islower():
            c = c+1
        if b.isdigit():
            d = d+1
        if (k and c and d)>0:
            break
    for s in spec:
        if s in n:
            j = j+1
    if (5<len(n)<15) and ((k and c and d and j) > 0):
        print("Valid password")
    else:
        print("Invalid password")

def username(n):
     
     for h in m:
          if h == "@":
               r = m.index(h)
               for l in range(r,len(m)):
                    if m[l] == ".":
                         print("Valid emailid")
                         password(m)
                         break
                    else:
                         global a
                         a = a+1
                         if a == (len(m)-r):
                              print("Invalid emailid")
m = input("please provide valid mailpwd: ")
n = input("please provide valid mailid: ")
username(n)
     

                
    

                        
