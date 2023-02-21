"""
Тестовое задание На бесконечной координатной сетке находится муравей. \
Муравей может перемещатся на 1 клетку вверх (x,y+1), вниз (x,y-1), влево (x-1,y), вправо (x+1,y), по одной клетке за шаг. \
Клетки, в которых сумма цифр в координате X плюс сумма цифр в координате Y больше чем 25 недоступны муравью. \
Например, клетка с координатами (59, 79) недоступна, т.к. 5+9+7+9=30, что больше 25. \
Сколько cклеток может посетить муравей если его начальная позиция (1000,1000), (включая начальную клетку). \
Прислать ответ и решение в виде числа клеток и исходного текста программы на языке Python решающей задачу

"""

COUNT = 1

class Ant:
    def __init__(self, x, y):
        self.GEN_LIST = [(x, y)]
        self.PAST_PLACE = [(x, y)]

    def counter_plus(self):
        global COUNT
        COUNT += 1

    def append_place(self, x, y):
        self.GEN_LIST.append((x, y))

    def remove_place(self, place: tuple):
        self.GEN_LIST.remove(place)

    def append_past_place(self, place: tuple):
        self.PAST_PLACE.append(place)

class Moving(Ant):
    def __init__(self, x, y):
        super().__init__(x, y)

    def down(self, x, y):
        if Checker.Check(x, y - 1) and (x, y - 1) not in self.PAST_PLACE:
            self.append_past_place((x, y - 1))
            self.append_place(x, y - 1)
            self.counter_plus()

    def up(self, x, y):
        if Checker.Check(x, y + 1) and (x, y + 1) not in self.PAST_PLACE:
            self.append_past_place((x, y + 1))
            self.append_place(x, y + 1)
            self.counter_plus()

    def left(self, x, y):
        if Checker.Check(x - 1, y) and (x - 1, y) not in self.PAST_PLACE:
            self.append_past_place((x - 1, y))
            self.append_place(x - 1, y)
            self.counter_plus()

    def right(self, x, y):
        if Checker.Check(x + 1, y) and (x + 1, y) not in self.PAST_PLACE:
            self.append_past_place((x + 1, y))
            self.append_place(x + 1, y)
            self.counter_plus()

    def main(self):
        while len(self.GEN_LIST) > 0:
            self.up(self.GEN_LIST[0][0], self.GEN_LIST[0][1])
            self.down(self.GEN_LIST[0][0], self.GEN_LIST[0][1])
            self.right(self.GEN_LIST[0][0], self.GEN_LIST[0][1])
            self.left(self.GEN_LIST[0][0], self.GEN_LIST[0][1])
            self.remove_place(self.GEN_LIST[0])

class Checker:
    @staticmethod
    def Check(x: int, y: int) -> bool:
        sum_x = sum([int(i) for i in str(x)])
        sum_y = sum([int(i) for i in str(y)])
        count = sum_x + sum_y
        if count > 25:
            return False
        return True

from matplotlib.pylab import *
class Coordinate:
    def __init__(self, _list: list):
        self._list_of_tuples = _list
        self.list_x = [int(i[0]) for i in self._list_of_tuples]
        self.list_y = [int(i[1]) for i in self._list_of_tuples]

    def show(self):
        scatter(self.list_x, self.list_y)
        grid()
        show()


if __name__ == '__main__':
    import time
    r = Moving(2500, 2500)
    start = time.monotonic()
    r.main()
    print('Ходов всего - {}'.format(COUNT))
    print('Время работы - {}'.format(time.monotonic() - start))

    pl = Coordinate(r.PAST_PLACE)
    pl.show()


