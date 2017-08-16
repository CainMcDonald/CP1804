score = float(input("Enter Score: "))
while 0 < score <= 100:
    if 50 <= score < 90:
        print("Passable")
    elif score >= 90:
        print("Excellent")
    else:
        print("Bad")
    score = float(input("Enter Score: "))
print("Invalid Score")
