def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')

# this is a comment: keywords siempre despues de los de posicion
print('Start')
greet_user(first_name='John', last_name='Smith')
print('Finish')

def cost(total, shipping, discount):
    print(f'Total: {total}€, Shipping: {shipping}€, Discount: {discount}€')


cost(total=50, shipping=5, discount=0.2)


def square(number):
    return number * number


print(square(3))





