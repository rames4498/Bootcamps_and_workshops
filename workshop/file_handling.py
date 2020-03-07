fl = open("ramesh_data.txt","r+")
fl.write("name ramesh nagur\n")
fl.write("dept ece c\n")
fl.write("address renigunta andhra\n")

d = {}
for values in fl:
    print(values)
    a,b,c = values.split()
    d[a]=[b,c]
    fl.write(d)
print(d)
fl.close()

