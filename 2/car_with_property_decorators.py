class Car:
    def __init__(self, make, model):
        self.__make = make
        self._model = model

    def __del__(self):
        print("Goodbye Cruel World")

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, make):
        self.__make = make



car1 = Car('ora', 'cat')
print(car1.make)
car1.make = "MG"
print(car1.make)
print(car1._Car__make)
print(car1._model)