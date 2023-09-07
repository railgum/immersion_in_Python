

# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга,
# а значение — кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того,
#   у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться
#   на любое большее количество друзей.

hike = {
    'misha': ('tent', 'pot', 'matches', 'axe', 'rope', 'canned food', 'knife'),
    'roma': ('knife', 'salt', 'rope', 'sweater', 'canned food'),
    'sasha': ('noodles', 'matches', 'salt', 'tent', 'axe'),
}

things = set()
for key, values in hike.items():
    for i in values:
        things.add(i)
print(f'Взяли следующие вещи: {things}')

all_things = list(hike.values())
uniq_things = set()
for i in all_things:
    uniq_things = set(i).symmetric_difference(uniq_things)
print(f'Уникальные вещи: {uniq_things}')

friend_not_thing = {}
for key, value in hike.items():
    friend_not_thing[key] = uniq_things.difference(set(value))

for key, value in friend_not_thing.items():
    print(f'У {key} нет {value}')

