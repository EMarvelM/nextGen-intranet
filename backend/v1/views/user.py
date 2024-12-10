from random import randint

def generate_username(firstname):
    return f'{firstname}{randint(1111, 9999)}'
