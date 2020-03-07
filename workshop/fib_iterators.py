
'''
li = [lambda x, i=i : x**i for i in range(4)]
print(li[3](2))


mylist = [x*x for x in range(3)]
for i in mylist:
    print(i)
'''
mylist = range(3)
print(mylist[2])
'''
def createGenerator():
    mylist = range(3)
    print(mylist)
    for i in mylist:
        yield i*i
'''       

       
#print(createGenerator())

'''
mygenerator = createGenerator()

for i in mygenerator:
    print(i)
'''

class fib_iterator:
    """An iterator over part of the Fibonacci sequence."""

    def __init__(self, limit, seed1=1, seed2=1):
        self.limit = limit
        self.previous = seed1
        self.current = seed2

    def __iter__(self):
        return self

    def __next__(self):
        (self.previous, self.current) = (self.current, self.previous + self.current)
        self.limit -= 1
        if self.limit < 0:
            raise StopIteration()
        return self.current


for x in fib_iterator(5):
    print(x)




