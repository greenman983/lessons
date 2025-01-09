class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

    def __add__(self, other):
        return Product (self.name, self.weight + other.weight, self.category)


class Shop():
    __file_name = 'products.txt'
    file = open(__file_name, 'w')
    file.close()

    def get_products(self):
        file = open(self.__file_name, 'r')
        products_ = file.read()
        file.close()
        return products_

    def add(self, *products):
        for product in products:
            prod_ = self.get_products()
            if product.name not in prod_:
                _file = open(self.__file_name, 'a')
                _file.write(f'{product}\n')
                _file.close()
            else:
                add_product = (p1 + p3)
                _file = open(self.__file_name, 'a')
                _file.write(f'{add_product}\n')
                _file.close()
                print (f'Продукт {product.name} уже был в магазине, его общий вес теперь равен {(add_product.weight)}.')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
s1.add(p1, p2, p3)
print(s1.get_products())