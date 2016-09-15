from random import randint
komp = randint (1,5)
print "kompp zagadal chislo, vvedi svoe chislo chtoby sravnit :"
user = int(input("> "))
print "skolko ballov? (0) "
bally = int(input("> "))
point = abs(komp - user)
if point == 1:
    print (bally + 5)
if point == 2:
    (bally + 4)
if point == 3:
    (bally + 3)
if point == 4:
    (bally + 2)
if point == 5:
    (bally + 1)
print "----------------------"
print point
print bally


