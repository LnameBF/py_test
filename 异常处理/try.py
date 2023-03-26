"""
try/expect/else

"""


a = 10
print('请输入一个数字：', end="")
b = int(input())
try:
    c = a/b
except ZeroDivisionError:
    print("0不能做除数")
except ValueError:
    print("数据错误")
else:
    print("没有错误")
print("——————————————————————————")

try:
    f = open("测试文.txt", "r")
    s = f.read()
    print(s.upper())
except (IOError, NameError):
    print("没有找到该文件")
finally:
    f.close()
