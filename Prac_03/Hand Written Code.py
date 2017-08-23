def main():
    name = get_name()
    print_name(name, 3)


def print_name(name, step=3):
    print(name[::step])


def get_name():
    name = input("Please Enter Your Name:")
    if len(name) <= 0:
        print("Invalid Name")
        name = input("Please Enter Your Name:")
    return name


main()