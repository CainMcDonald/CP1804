def main():
    name = get_name()
    print_name(name)


def print_name(name):
    print(name[::3])


def get_name():
    name = input("Please Enter Your Name:")
    if len(name) <= 0:
        print("Invalid Name")
        name = input("Please Enter Your Name:")
    return name


main()