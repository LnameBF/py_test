s = range(10)
for a in s:
    print(a)

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
s1 = [x * y for x in vec1 for y in vec2]
for s in s1:
    print(s, end=" ")


print("嵌套列表")
# 嵌套列表
matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
]
s = [[raw[c] for raw in matrix] for c in range(4)]
print(s)

