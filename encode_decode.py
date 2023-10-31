#functions

def menu():
    print("Menu")
    print("-------------")
    print("1. Encode\n2. Decode\n3. Quit")

def encode(password):
    global orig_pass
    global encoded_password
    if len(password) != 8 and not password.isdigit():
        print("Password must be 8-digits and only consist of numbers")

    else:
        orig_pass = password
        encoded_password = ''.join(str((int(digit) + 3) % 10) for digit in password)
        print('Your password has been encoded and stored')
    
if __name__ == "__main__":
    while True:
        menu()
        choice = input("Please enter an option: ")

        if choice == "1":
            password = input("Please enter a password to be encoded that is 8 chars long and only digits: ")
            encode(password)
        elif choice == "2":
            print("The encoded password is " + encoded_password + ", and the original password is " + orig_pass)
        elif choice == "3":
            print("Thank you for using this password encoder/decoder. Have a nice day!")
            break
        else:
            print("Please enter a value 1-3")
