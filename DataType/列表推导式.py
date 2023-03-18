list_demo = ['Google', 'Run', 'Taobao']
new_list = [name.upper() for name in list_demo if len(name) > 3]
print(new_list)
