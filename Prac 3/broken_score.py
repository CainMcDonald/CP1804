score = float(input("Enter Score: "))
result = return_result
print(result)


def return_result(final_score):
    if final_score < 50:
        return "Bad"
    elif final_score < 90:
        return "Passable"
    else:
        return "Excellent"

# if 50 <= score < 90:
#         print("Passable")
#     elif score >= 90:
#         print("Excellent")
#     else:
#         print("Bad")
#     score = float(input("Enter Score: "))
# print("Invalid Score")
