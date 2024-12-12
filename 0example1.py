import random


print("The method random.random() generates a number from 0 to 1")
for i in range(5):
    x = random.random()
    print("  " , x)

print("\nThe method random.randint(a,b) returns a random integer")
print("starting with a and ending with b, inclusive")
print("random.randint(1,10) creates a random number from 1 to 10")

for i in range(5):
    x = random.randint(1,10)
    print("  ",x)