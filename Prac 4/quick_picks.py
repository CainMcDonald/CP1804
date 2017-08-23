import random
NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45

quick_picks = int(input("How many Quick Picks would you like: "))
for i in range(quick_picks):
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MINIMUM, MAXIMUM)
        print("{:2}".format(number))
    print()