# для создания имен по слогам
import random
from string import ascii_lowercase

vowels = set('aeiouy')
consonants = set(ascii_lowercase).difference(vowels)


def random_name():
    len_name = random.randint(4, 7)
    name = ''
    for i in range(len_name):
        name += random.choice(list(vowels)) if i % 2 else random.choice(list(consonants))
    return name.title()


for i in range(10):
    print(random_name())