groceries = set()
groceries.add("bread")
groceries.add("cheese")
groceries.add("apples")
groceries.add("milk")
groceries.add("beer")


print (len(groceries))

groceries.remove ("apples")
print (len(groceries))

dairy = set(["cheese", "milk"])
yeast = set(["bread", "beer"])
drink = set(["milk", "beer"])
food = set (["bread", "cheese", "apples"])

print (dairy.intersection (food))
print (yeast.union (drink))


