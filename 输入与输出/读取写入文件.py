f = open('写入文件测试.txt', 'r+')
f.write("java是一门非常好的文件，py也是")


new_dict2 = {'name2': "zly", 'age2': 20, 'address2': 'lesan'}
f.write(str(new_dict2))
f.close()