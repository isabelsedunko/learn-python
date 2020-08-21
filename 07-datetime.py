import datetime
born = datetime.date(1972, 11, 12)
print(born)
education = datetime.timedelta(25, 1, 1)
graduation = born + education
print(graduation)#
congratulations = "you graduated on {:%A, %B %d, %Y}"
print(congratulations.format(graduation))

