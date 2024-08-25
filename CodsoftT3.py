from random import choice, shuffle,randint

def generate_pass(max_length, a, a2, b, b2, c, c2):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    min_letters = a
    min_symbols = b
    min_numbers = c

    num_letters = randint(min_letters, min(min_letters + (max_length - (min_symbols + min_numbers)), a2))
    num_symbols = randint(min_symbols, min(min_symbols + (max_length - (num_letters + min_numbers)), b2))
    num_numbers = max_length - (num_letters + num_symbols)

    while num_letters + num_symbols + num_numbers > max_length:
        if num_letters > min_letters:
            num_letters -= 1
        elif num_symbols > min_symbols:
            num_symbols -= 1
        elif num_numbers > min_numbers:
            num_numbers -= 1

    while num_letters + num_symbols + num_numbers < max_length:
        if num_letters < a2:
            num_letters += 1
        elif num_symbols < b2:
            num_symbols += 1
        elif num_numbers < c2:
            num_numbers += 1

    password_letter = [choice(letters) for _ in range(num_letters)]
    password_symbol = [choice(symbols) for _ in range(num_symbols)]
    password_num = [choice(numbers) for _ in range(num_numbers)]

    password_list = password_letter + password_symbol + password_num
    shuffle(password_list)
    password = "".join(password_list)
    return password

max_length = int(input("Enter the maximum length of the password: "))
a = int(input("Enter the minimum number of alphabets you need in the password: "))
a2 = int(input("Enter the maximum number of alphabets you need in the password: "))
b = int(input("Enter the minimum number of symbols you need in the password: "))
b2 = int(input("Enter the maximum number of symbols you need in the password: "))
c = int(input("Enter the minimum number of digits you need in the password: "))
c2 = int(input("Enter the maximum number of digits you need in the password: "))

print("The newly generated password is:", generate_pass(max_length, a, a2, b, b2, c, c2))

