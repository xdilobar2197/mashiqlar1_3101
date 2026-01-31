# mashiqlar1_3101


t1 = (1, 2, 3)
t2 = ('a', 'b', 'c')

result = []
for a, b in zip(t1, t2):
    result.append(a)
    result.append(b)

result = tuple(result)
print(result)

a = {1, 2, 3, 4, 5}
b = {3, 4}
c = {5, 6}

result = a - b - c
print(result)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
result = a ^ b
print(result)


text = "berilgan matinda barcha noyob sozlarni ajratib oling"

words = set(text.split())
result = set(sorted(words))
print(result)
