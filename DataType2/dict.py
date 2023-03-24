new_dict = {'name': "zly", 'age': 20, 'address': 'lesan'}
new_dict2 = {'name2': "zly", 'age2': 20, 'address2': 'lesan'}
# 字符串输出字典
print(str(new_dict))
# 删除 指定的字典值
del new_dict['name']
print(str(new_dict))

# 字典复制
dict_one = new_dict.copy()
print(dict_one)
# 字典遍历
print("键值对")
for k, v in new_dict.items():
    print(k, "+"
          , v)
