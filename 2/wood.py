class Wood:

    def __init__(self, product, type, price, inventory):
        self.__product = product
        self.__type = type
        self.__price = price
        self.__inventory = inventory

    def get_product(self):
        return self.__product

    def set_product(self, product):
        self.__product = product

    def get_type(self):
        return self.__type

    def set_type(self, type):
        self.__type = type

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_inventory(self):
        return self.__inventory

    def set_inventory(self, inventory):
        self.__inventory = inventory

    product = property(get_product, set_product)
    type = property(get_type, set_type)
    price = property(get_price, set_price)
    inventory = property(get_inventory, set_inventory)

    def display(self):
        print(f'{self.product} {self.type} - price: {self.price:.2f}, inventory:{self.inventory:d}')

        def sellWood(self, quantity):
            self.__inventory = self.__inventory - quantity
            print(f'\nSold {quantity} pieces of {self.product}\n')


class Plywood(Wood):

    def __init__(self, product, type, price, inventory, width, length):
        super().__init__(product, type, price, inventory)
        self.__width = width
        self.__length = length

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    width = property(get_width, set_width)
    length = property(get_length, set_length)

    def display(self):
        print(f'This Plywood is {self.width} inches wide and {self.length} inches long')