#3.compute and return the area and circumference of a circle.

def area(r):
    area=3.14*r*r
    return area

def circumference(r):
    c=2*3.14*r
    return c

r=float(input("enter the radius"))
a=area(r)
print("area is: ",a)
cf=circumference(r)
print("Circumference is: ",cf)
