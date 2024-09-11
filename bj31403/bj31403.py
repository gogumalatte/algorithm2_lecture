a = int(input())
b = int(input())
c = int(input())
print(a + b - c)

fakeB = b
while fakeB > 0:
    fakeB = fakeB // 10
    a *= 10
print(a + b - c)
