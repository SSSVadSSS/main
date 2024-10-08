class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if self.number_of_floors >= new_floor > 0:
            for i in range(new_floor):
                print(i + 1)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return str(f'Название: {self.name}, Количество этажей: {self.number_of_floors}')

    def __eq__(self, other):
        if isinstance(other, House):
            if isinstance(other.number_of_floors, int) and isinstance(self.number_of_floors, int):                                                                                               int):
                return self.number_of_floors == other.number_of_floors
        else:
            return print("Неверный параметр")

    def __add__(self, value):
        if isinstance(self.number_of_floors, int) and isinstance(value, int):
            self.number_of_floors += value
        else:
            print("Значение аргумента не соответствует типу")
            return self

    def __lt__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors < other.number_of_floors
        else:
            print("Значение аргумента не соответствует типу")

    def __le__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors <= other.number_of_floors
        else:
            print("Значение аргумента не соответствует типу")

    def __gt__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors > other.number_of_floors
        else:
            print("Значение аргумента не соответствует типу")

    def __ge__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors >= other.number_of_floors
        else:
            print("Значение аргумента не соответствует типу")

    def __ne__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors != other.number_of_floors
        else:
            print("Значение аргумента не соответствует типу")

    def __radd__(self, value):
        if isinstance(value, int) and isinstance(self.number_of_floors, int):
            return self.__add__(value)
        else:
            print("Значение аргумента не соответствует типу")

    def __iadd__(self, value):
        if isinstance(value, int) and isinstance(self.number_of_floors, int):
            return self.__add__(value)
        else:
            print("Значение аргумента не соответствует типу")


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
