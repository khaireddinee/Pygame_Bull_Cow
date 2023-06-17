import random

Number = []


def generate_number():

    for _ in range(0, 4):
        x = random.randrange(0, 9)
        Number.append(x)
        if len(Number) > len(set(Number)):
            Number.clear()
            generate_number()
