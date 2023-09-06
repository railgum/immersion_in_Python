# Создайте словарь со списком вещей для похода в качестве ключа и их массой в
# качестве значения. Определите какие вещи влезут в рюкзак, передав его
# максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

MAX_TONNAGE = 30
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

possible_set = []

for key, value in things_for_hike.items():
    while sum(possible_set(key)) < MAX_TONNAGE:


