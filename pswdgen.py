# pswdgen.py - generates password and prompts user for strength

# Modules used

import string, random

# different strength levels based on string module's
# methods. .ascii letters are chars Aa - Zz, .punctuation
# are chars considered punctuation, and .digits is the
# string '0123456789'

weak = string.ascii_letters
med = string.ascii_letters + string.digits
strong = string.ascii_letters + string.digits + string.punctuation

# function that generates password. Takes arguments for strength,
# which is user input, and size, which is decided based on
# user's choice.


def pswd_gen(strength, size):
    return ''.join(random.choice(strength) for x in range(size))


# while loop with statements to ensure that the program
# runs until the user enters the right input

while True:

    # .casefold() used to take all cases of letters. Size depends
    # on user's strength choice.

    strength = input('How strong do you want your password? ').casefold()
    if strength == 'weak':
        size = random.randint(6, 8)
        print(pswd_gen(weak, size))
        break

    elif strength == 'medium':
        size = random.randint(8, 10)
        print(pswd_gen(med, size))
        break

    elif strength == 'strong':
        size = random.randint(10, 12)
        print(pswd_gen(strong, size))
        break

    else:
        print('Please enter weak, medium, or strong: ')
        continue

# credit to the numerous python resources on the internet that
# helped me make my own password generator.
