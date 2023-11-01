#functions

#this was coded by yona
#some of the text was edited by sky (dylan) boes
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode\n2. Decode\n3. Quit\n")

def encode(password):
    global encoded_password
    if len(password) != 8 and not password.isdigit():
        print("Password must be 8-digits and only consist of numbers")

    else:
        encoded_password = ''.join(str((int(digit) + 3) % 10) for digit in password)
        print('Your password has been encoded and stored!')

#this was coded by sky (dylan) boes
def decode(password):
  decoded_password = ''.join(str((int(digit) - 3) % 10) for digit in password)
  return decoded_password

#this was coded by yona
#sky (dylan) boes edited some of the text, initialized encoded_password, and made the code work with the decode() function

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Please enter an option: ")
        encoded_password = ""

        if choice == "1":
            password = input("Please enter your password to encode: ")
            encode(password)
        elif choice == "2":
            print("The encoded password is " + encoded_password + ", and the original password is " + decode(encoded_password) + ".\n")
        elif choice == "3":
            break
        else:
            print("Please enter a value 1-3")
