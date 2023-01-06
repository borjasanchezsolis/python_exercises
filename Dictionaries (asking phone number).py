customer = {
    'name': 'John Smith',
    'age': 30,
    'is_verified': True
}
print(customer.get('name'))

phone_number = input('Phone: ')
numbers = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four'
}
output = ''
for character in phone_number:
   output += numbers.get(character, '!') + ' '
print(output)