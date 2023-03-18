

def add(a, b):
    return a + b

def sum():
    num = [i for i in range(30) if i % 3 == 0]
    return num

bbb = sum()


def create_dict():
    list_demo = ['Google', 'Runoob', 'Taobao']
    new_dict = {key: len(key) for key in list_demo}
    print(new_dict)
create_dict()
print("----------------------")
print(bbb)
print("-----------------------")
a = 1.2
b = 1
c = add(a, b)
print(f"ab+={c}")
