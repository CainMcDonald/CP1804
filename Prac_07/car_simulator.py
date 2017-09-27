from Prac_07.car import Car

MENU = 'Menu:\nd) drive\nr) refuel\nq) quit'


def main():
    print('Lets Drive')
    name = input("Enter your car name: ")
    car = Car(name, 100)
    print(car)
    print(MENU)
    choice = input("Enter your choice: ").lower()
    while choice != 'q':
        if choice == 'd':
            distance_to_drive = int(input("How many km do you wish to drive? "))
            while distance_to_drive < 0:
                print("Distance must be over 0 km")
                distance_to_drive = int(input("How many km do you wish to drive? "))
            distance_driven = car.drive(distance_to_drive)
            print("The car drove {}km".format(distance_driven))
            if car.fuel == 0:
                print(" and ran out of fuel")
            print(".")
        elif choice == 'r':
            fuel_to_add = int(input("How much fuel do you wish to add to the car? "))
            while fuel_to_add < 0:
                print("Fuel amount must be more than 0")
                fuel_to_add = int(input("How much fuel do you wish to add to the car? "))
            car.add_fuel(fuel_to_add)
            print("Added {} units of fuel to the car".format(fuel_to_add))
        else:
            print("Invalid Choice")
        print(car)
        print(MENU)
        choice = input("Enter your choice: ").lower()
    print("\nGoodBye {}'s driver".format(car.name))


main()
