bakery_cache = {}
def carrotcake(n):
    if n in bakery_cache:
        return bakery_cache[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = carrotcake(n-1) + carrotcake(n-2)

    bakery_cache[n]=value
    return value

for n in range(1,101):
    print(n,":", carrotcake(n))


    