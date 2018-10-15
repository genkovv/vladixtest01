import pdb
import random


print("Provide 6 numbers from 1 to 49")
num1 = input("First number:")
num2 = input("Second number:")
num3 = input("Third number:")
num4 = input("Forth number:")
num5 = input("Fifth number:")
num6 = input("Sixth number:")

lot1 = random.randint(1,49)
lot6 = lot5 = lot4 = lot3 = lot2 = lot1

while lot1 == lot2:

    lot2 = random.randint(1,49)
    print ("lot2:",lot2)

while lot3 == lot2 or lot3 == lot1:

    lot3 = random.randint(1,49)
    print ("lot3",lot3)

lot3 = random.randint(1,49)
lot4 = random.randint(1,49)
lot5 = random.randint(1,49)
lot6 = random.randint(1,49)

print ("lot1:", lot1)
print ("lot2:", lot2)
print ("lot3:", lot3)
print ("lot4:", lot4)
print ("lot5:", lot5)
print ("lot6:", lot6)
