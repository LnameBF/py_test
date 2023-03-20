new_list = ['red', 'green', 'blue', 'yellow', 'white', 'black', 'asd']
print(new_list[0])
# 左开右关 不包含5
print(new_list[1:5:2])

# 更新列表 使用 append（）
new_list.append('123')
print(new_list)

# 删除列表元素
del new_list[-1]
print(new_list)


# 删除指定元素
new_list.remove("red")
print(new_list)
