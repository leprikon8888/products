from product import Product
from cart import Cart

if __name__ == '__main__':
    pr_1 = Product('orange', 2, 'fresh orange')
    pr_2 = Product('tea', 10, 'black ceylon loose leaf tea')
    pr_3 = Product('kola', 8, 'light refreshing drink')

    user_a = Cart()
    user_a.add_product(pr_1, 5)
    user_a.add_product(pr_3, 6)
    user_a.add_product(pr_2, 7)
    user_a.add_product(pr_3, 6)


    x = user_a[:]
    for i in x:
        print(i)

    print('**********')
    print(len(user_a))
    print('**********')
    y = user_a[3]
    print(y)




