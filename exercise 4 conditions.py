is_hot = False
is_cold = True

if is_hot:
    print('It´s a hot day')
    print('Drink plenty of water')
elif is_cold:
    print('It´s cold')
    print('Wear nice clothes')
else:
    print('It´s a lovely day')

print('Enjoy yor day')


is_good_credit = True
is_bad_credit = False

if is_good_credit:
    print(1000000 - (1000000*0.10))
if is_bad_credit:
    print(1000000 - (1000000*0.20))


price = 1000000
good_credit = True

if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print (f"Down payment: {down_payment}€")