# Linda Phung
def encode(password):
    encoded = ""
    for i in password:
        digit = int(i) + 3
        encoded += str(digit)
    return encoded


def decode(password):
    # rachel edited this
    decoded = ""
    for i in password:
        digit = int(i) - 3
        decoded += str(digit)
    return decoded


def main():

    encoded = None

    while True:
        print()
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        menu_selection = int(input("Please enter an option: "))
        if menu_selection == 1:
            password = input("Please enter your password to encode: ")
            encoded = encode(password)

            print("Your password has ben encoded and stored!")

        elif menu_selection == 2:
            decoded = decode(encoded)
            print("The encoded password is " + encoded + " and the original password is " + decoded + ".")

        elif menu_selection == 3:
            break

if __name__ == "__main__":
    main()
