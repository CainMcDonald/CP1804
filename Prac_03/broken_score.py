def main():
    score = float(input("Enter Score: "))
    print(calculate_result(score))


def calculate_result(score):
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
