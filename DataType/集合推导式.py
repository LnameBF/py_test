code = [1, 1, 3]
# 表达式a*3 遍历 code将值传入a*3
# 这是一个集合，集合set中不包含重复的数字
new_set = {a*3 for a in code}
print(new_set)
