def main():
    name = get_name()
    print_name(name)


def print_name(name):
    for char in name[::2]:
        print("{}".format(char))


def get_name():
    name = input("Please Enter Your Name:")
    if len(name) <= 0:
        print("Invalid Name")
        name = input("Please Enter Your Name:")
    return name


main()