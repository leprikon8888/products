from product import Product


class CartIter:
    def __init__(self, products, quantities):
        self.__products = products
        self.__quantities = quantities
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.__products):
            self.index += 1
            return self.__products[self.index - 1], self.__quantities[self.index - 1]
        raise StopIteration()


class Cart:
    def __init__(self):
        self.products = []
        self.quantities = []

    def add_product(self,
                    product: Product,
                    quantity: int | float):
        if not isinstance(product, Product):
            raise TypeError('Error in Product datatype')
        elif not isinstance(quantity, int | float):
            raise TypeError('Error in quantity of Product')
        elif quantity <= 0:
            raise ValueError('Quantity must be > 0. But less or equal got.')
        self.products.append(product)
        self.quantities.append(quantity)

    def total(self):
        summa = 0
        for product, quantity in zip(self.product, self.quantities):
            summa += product.price * quantity
        return summa

    def __getitem__(self, index):
        if isinstance(index, int):
            if 0 <= index < len(self.products):
                return self.products[index]
            raise IndexError("Index out of range")

        if isinstance(index, slice):
            start = 0 if index.start is None else index.start
            stop = len(self.products) if index.stop is None else index.stop
            step = 1 if index.step is None else index.step

            tmp = []
            if start < 0 and stop > len(self.products):
                raise IndexError
            for i in range(start, stop, step):
                tmp.append(self.products[i])
            return tmp

    def __len__(self):
        return len(self.products)


    def __iter__(self):
        return CartIter(self.products, self.quantities)

    def __str__(self):
        res = ''
        for product, quantity in zip(self.products, self.quantities):
            res += f'{product} x {quantity} = {product.price * quantity}$ \n'
        return res
