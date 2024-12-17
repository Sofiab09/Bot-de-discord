import random as r, string as s

def gen_pass(largo):
    elements = s.ascii_letters + s.digits + s.punctuation +s.ascii_lowercase +s.ascii_uppercase
    password =""

    for i in range(largo):
        password += r.choice(elements)

    return password

def flip_coin():
    flip = r.randint(0, 2)
    if flip == 0:
        return "HEADS"
    else:
        return "TAILS"