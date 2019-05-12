l = input()
l = list(l)
a = []
length = len(l)-1
while (length>=0):
    a.append(l[length])
    length -= 1
if (a == l):
    print('YES')
else:
    print('NO')

