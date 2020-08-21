def areasq(x):
    """ calculate area of a square """
    return x**2
    


print(areasq(2))

print(areasq(3))

def circcirc(r):
    """ calculate the circumference of a circle """
    return 2 * 3.14159 * r

print(circcirc(1))

def bananaorder(quantity, perunitcost = 2, shipping = 10):
    return quantity + perunitcost*quantity + shipping

print(bananaorder(3))
print(bananaorder(3,perunitcost=0.5))
#bananas are on offer
print(bananaorder(30, perunitcost=0.5, shipping=3))
#reduced price shipping
