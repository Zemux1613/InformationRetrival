import crashkurs.variables
import crashkurs.functions
import crashkurs.generators
import crashkurs.controlls

if __name__ == '__main__':
    print("Variables:")
    print(crashkurs.variables.check_isbn())

    print("Functions:")
    number = "11"  # input("Von welcher Zahl willst du die Quersumme?: ")
    print(crashkurs.functions.digit_sum(number))
    print(crashkurs.functions.info(1, 12, 3, 4))

    print("Generators:")
    generators_even = crashkurs.generators.even(256)
    list = []
    for elements in generators_even:
        for element in elements:
            list.append(element)
    print(list)
    print("Controlls:")
    print(crashkurs.controlls.sort(2, 4, 1))
    print("\n")
    print("11 -> 31")
    print(crashkurs.controlls.price(11, 31))
    print("21 -> 31")
    print(crashkurs.controlls.price(21, 31))
    print("13 -> 31")
    print(crashkurs.controlls.price(13, 31))
    print("31 -> 13")
    print(crashkurs.controlls.price(31, 13))
