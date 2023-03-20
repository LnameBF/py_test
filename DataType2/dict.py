new_dict = {'name': "zly", 'age': 20, 'address': 'lesan'}
# 字符串输出字典
print(str(new_dict))
# 删除 指定的字典值
del new_dict['name']
print(str(new_dict))

# 字典复制
dict_one = new_dict.copy()
print(dict_one)