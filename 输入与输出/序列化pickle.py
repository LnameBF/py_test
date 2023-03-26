import pickle
import pprint


# 将文件序列化写入到文件中
datapick1 = {'name': 'liangjiawei', 'age': 20, 'address': '四川省德阳市'}


f = open('序列化测试.pkl', 'wb')
S = str(datapick1)
pickle.dump(datapick1, f)
f.close()

# #使用pickle模块从文件中重构python对象
pkl_file = open('序列化测试.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)
print(data1)

pkl_file.close()