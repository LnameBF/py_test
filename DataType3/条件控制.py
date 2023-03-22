a = 5
b = 3
# 条件 语法和java有些许不同，
"""
1. 关键字 if-else -> if-elif
2. 不用加括号
"""
if a > 2:
    print("a大于2")
    if b > 3:
        print("b大于3")
    elif b == 3:
        print("b等于3")
    else:
        print("b小于3")
elif a == 2:
    print("a等于2")
else:
    print("a小于2")

