def createGenerator():
    
    mylist = range(3)
    for i in mylist:
        yield i*i
        
mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!

#<generator object createGenerator at 0xb7555c34>

for i in mygenerator:
    print(i)

