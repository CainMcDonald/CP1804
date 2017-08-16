# Part 1
# output_file = open('name.txt', 'w')
# username = input("Enter your name: ")
# print(username, file=output_file)
# output_file.close()

# Part 2
# input_file = open('name.txt', 'r')
# name = input_file.read().strip()
# print('Your name is {}'.format(name))
# input_file.close()

# Part 3
# in_file = open('numbers.txt', 'r')
# first_number = int(in_file.readline())
# second_number = int(in_file.readline())
# print(first_number + second_number)
# in_file.close()

in_file = open('numbers.txt', 'r')
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)
in_file.close()
