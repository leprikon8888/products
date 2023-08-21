from product import Product
from cart import Cart

if __name__ == '__main__':
    pr_1 = Product('orange', 2, 'fresh orange')
    pr_2 = Product('tea', 10, 'black ceylon loose leaf tea')
    pr_3 = Product('kola', 8, 'light refreshing drink')

    user_a = Cart()
    user_a.add_product(pr_1, 5)
    user_a.add_product(pr_3, 6)

    print(user_a)