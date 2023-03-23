# 输出字符串
print("hello world")

# 输出变量值
i = 234 * 345
print(i)

# 简单数学运算
x = 2
y = 3
z = 4
n = x * y + z
print(n)

# 定义一个列表并且打印
my_list = ['google', 'runoob', 'taobao']
for list in my_list:
    print(list)

# for循环打印范围数字
for code in range(1, 10):
    print(code)

# else 语句
a = 4
if a == 4:
    print("a等于4")
elif a > 4:
    print("a大于4")
else:
    print("a不等于4")

# 输出一个斐波那契数列
a, b = 0, 1
while b < 10:
    print(b)
    """
    a=b
    b=a+b
    """
    a, b = b, a + b

