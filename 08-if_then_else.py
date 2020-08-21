
a = int(input("length of side a = "))
b = int(input("length of side b = "))
c = int(input("length of side c = "))
d = int(input("length of side d = "))
if a == c and b == d and a !=b:
    print ("this is a rectangle")
elif a == c and b == d and a == b:
    print ("this is a square")

if a == 0 or b == 0 or c == 0 or d == 0:
    print ("this is a triangle")
else:
    print ("this is a quadrilateral")
    