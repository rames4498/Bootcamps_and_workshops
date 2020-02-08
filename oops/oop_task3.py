class Square:
   def __init__(self, length, unit_cost=0):
       self.length = length
       #self.breadth = breadth
       self.unit_cost = unit_cost
   
   def get_perimeter(self):
       return 4 * (self.length)
   
   def get_area(self):
       return self.length * self.length
   
   def calculate_cost(self):
       area = self.get_area()
       return area * self.unit_cost
# breadth = 120 cm, length = 160 cm, 1 cm^2 = Rs 2000
s = Square(160, 2000)

print("Area of Square: %s cm^2" % (s.get_area()))
print("Cost of square field: Rs. %s " %(s.calculate_cost()))
