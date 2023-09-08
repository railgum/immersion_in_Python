import random

# Создайте словарь со списком вещей для похода в качестве ключа и их массой в
# качестве значения. Определите какие вещи влезут в рюкзак, передав его
# максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.


MAX_TONNAGE = 30
MIN_TONNAGE = 25
things_for_hike = {
    'marquee': 15,
    'pot': 1,
    'axe': 3,
    'rope': 0.5,
    'food': 5,
    'sleeping bag': 3,
    'dishes': 2,
    'knife': 0.3,
    'clothes': 10,
    'kit': 0.5,
    'lamp': 1.5,
    'telephone': 0.4,
    'battery': 0.5,
}

possible_dict = {}
while True:
    rnd_key = random.choice(list(things_for_hike))
    possible_dict.setdefault(rnd_key, things_for_hike[rnd_key])
    if sum(possible_dict.values()) > MAX_TONNAGE:
        del possible_dict[rnd_key]
    if MAX_TONNAGE > sum(possible_dict.values()) > MIN_TONNAGE:
        break


print('Возможный вариант:')
for key in possible_dict.keys():
    print(key)
print(f'Общий вес: {sum(possible_dict.values())}')


