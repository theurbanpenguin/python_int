class Car:
    def __init__(self, make, model):
        self.__make = make
        self._model = model

    def __del__(self):
        print("Goodbye Cruel World")


    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make


    make = property(get_make, set_make)


car1 = Car('ora', 'cat')
print(car1.make)
car1.make = "MG"
print(car1.make)
print(car1._Car__make)
print(car1._model)