# 定义一个列表
Code_list = ["apple", "orange", "banana"]

# 一个字典推导式，利用字符串长度作为值   key_expr: value_expr for value in collection
# name: len(name)字典结构，name作为字典的key，len(name)作为字典的value
name_dict = {name: len(name) for name in Code_list}
print(name_dict)

print("--------------------------------------")
# 如果列表里面就是一个字典
tuple_name = [("apple", 1), ("oranger", 2), ("banana", 3)]
tuple_dict = {fruit: code for fruit, code in tuple_name}
print(tuple_dict)
