#f  = lambda x,i:x**i
myli = [lambda x,i=i:x**i for i in range(4)]
print(myli[3](5))
