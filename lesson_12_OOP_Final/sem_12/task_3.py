# 📌 Создайте класс-генератор.
# 📌 Экземпляр класса должен генерировать факториал числа в
#    диапазоне от start до stop с шагом step.
# 📌 Если переданы два параметра, считаем step=1.
# 📌 Если передан один параметр, также считаем start=1.

class FactorStep:
    def __init__(self, *args):
        self.start, self.stop, self.step = 1,1,1
        if args:
            args = list(map(int, args))
            match len(args):
                case 1:
                    self.stop = args[0]
                case 2:
                    self.start, self.stop = args
                case 3:
                    self.start, self.stop, self.step = args
        self._value = self._fact()

    def _fact(self):
        factorial = []
        number = 1
        for i in range(self.start, self.stop, self.step):
            number *= i
            factorial.append(number)
        return factorial

    def __iter__(self):
        return self

    def __next__(self):
        while self._value:
            return self._value.pop(0)
        raise StopIteration

a = FactorStep(3,10,2)
print(*a)