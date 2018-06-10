def p(x):
    print(x)

#1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

def seven_and_five():
    for number in range(1500,2701):
        if number % 7 == 0 and number % 5 == 0:
            print(str(number) + " is divisible by 7 and multiplicable by 5.")
        else:
            p(str(number)  + " is rejected.")

#3. Write a Python program to guess a number between 1 to 9. Go to the editor
#Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

def attempt_to_guess():
    from scripts import test_crap
    random_number = test_crap.randint(1, 3)
    user_guess = int(input("choose a number..."))

    if random_number == user_guess:
        print("its the same.")
    else:
        print("its different.")

    print("the random number was " + str(random_number))
    print("the guessed number was " + str(user_guess))

#7. Write a Python program that prints each item and its corresponding type from the following list.

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

def types_in_list(anylist):
    for item in anylist:
        p(type(item))

#14. Write a Python program that accepts a string and calculate the number of digits and letters.

# def count_letter_and_digit(any_string):
#     digits = 0
#     chars = 0

a = "1"
b = "d"

p(int(b))


# 15. Write a Python program to check the validity of password input by users. Go to the editor
# Validation :
#
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
