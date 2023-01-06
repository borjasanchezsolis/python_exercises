import random

for number in range(3):
    print(random.random())

for number in range(3):
    print(random.randint(10, 30))

members = ['Mary', 'Borja', 'Bob', 'Reme']
leader = random.choice(members)
print(leader)