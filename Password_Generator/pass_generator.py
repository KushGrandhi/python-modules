#uses python module random to generate random password of length 8

import random
import string

def random_password():
    random_source = string.ascii_letters  + string.digits + string.punctuation
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    for i in range(4):
        password += random.choice(random_source)

    initial_pass = list(password)
    random.SystemRandom().shuffle(initial_pass)
    password = ''.join(initial_pass)
    return password

print("Random Password is ",  random_password())

#sample output:
#Random Password is  01Vi}13b
