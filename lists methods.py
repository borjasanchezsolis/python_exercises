numbers = [4, 7, 1, 5, 7, 22]
numbers.append(20)
print(numbers)

numbers = [4, 7, 1, 5, 7, 22]
numbers.insert(0, 43)
print(numbers)

numbers = [4, 7, 1, 5, 7, 22]
numbers.remove(7)
print(numbers)

numbers = [4, 7, 1, 5, 7, 22]
numbers.clear()
print(numbers)

numbers = [4, 7, 1, 5, 7, 22]
numbers.pop()
print(numbers)

numbers = [4, 7, 1, 5, 7, 22]
print(numbers.index(7))

numbers = [4, 7, 1, 5, 7, 22]
print(50 in numbers)

numbers = [4, 7, 1, 5, 7, 22]
numbers.sort()
numbers.reverse()
print(numbers)

numbers = [4, 7, 1, 5, 7, 22]
numbers2 = numbers.copy()
numbers.append(12)
print(numbers2)