my = "I am from chennai"
'''
for i in my:
    if i == "f":
        print(" found")
        break
    else:
        print("not found")
'''
for i in range(len(my)):
    if my[i]=='f':
        print(i,'is the index of f')
        print('found')
