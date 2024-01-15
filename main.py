from random import randint
from random import choice


def get_randint_50_6() -> list:
    return [randint(1, 50) for _ in range(6)]

def get_choice_50_6() -> list:
    return [choice(range(1, 50+1)) for _ in range(6) ]

def get_randint_45_7() -> list:
    return [randint(1, 45) for _ in range(7)]

def get_choice_45_7() -> list:
    return [choice(range(1, 45+1)) for _ in range(7) ]

fruits = [
        'apple', 
        'banana',
        'kiwi'
]

foods = [
        'pasta',
        'pizza',
        'stwe',
]

if __name__=='__main__':
    print(get_randint_50_6())
    print(get_choice_50_6())
    print(get_randint_45_7())
    print(get_choice_45_7())

