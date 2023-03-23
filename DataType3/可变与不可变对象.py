# 传一个不可变对象
def charge(a):
    a = 10
    print(id(a))


"""
输出
2367942060336
2367942060624

a已经指向了另一个值10的地址
"""
a = 1
print(id(a))
charge(a)


# 传入一个可变对象 例如一个列表
print("---------可变对象-------------")
def able_charge(ch_list):
    ch_list.append([1, 2, 3, 4])
    print("改变之后list，在函数内读值", ch_list)


list_new = ['1', '2', '3', '4']
print("改变之前", list_new)

able_charge(list_new)
print("改变之后在函数外读值", list_new)
"""
改变之前 ['1', '2', '3', '4']
改变之后list，在函数内读值 ['1', '2', '3', '4', [1, 2, 3, 4]]
改变之后在函数外读值 ['1', '2', '3', '4', [1, 2, 3, 4]]
"""