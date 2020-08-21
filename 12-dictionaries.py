crunchips = {"fat":34, "carbohydrates":52, "fibre":3.5, "protein":5.5, "salt":1.6}
print (crunchips)
print (crunchips ['fat'])

# do chips contain vitamins
if 'vitamins' in crunchips:
    print(crunchips["vitamins"])
else:
    print("crunchips have no vitamins")

try:
    print(crunchips['sugar'])
except KeyError:
    print("no sugar content")
