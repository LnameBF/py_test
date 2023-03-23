s = range(10)
for a in s:
    print(a)

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
s1 = [x * y for x in vec1 for y in vec2]
for s in s1:
    print(s, end=" ")
