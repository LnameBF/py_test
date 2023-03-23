class a:
    def __iter__(self):
        self.b = 1
        return self

    def __next__(self):
        if self.b <= 20:
            self.b += 1
            return self.b
        else:
            raise StopIteration


# 创建a的一个实例化对象 a1
a1 = a()
# 创造一个迭代器对象
a2 = a1.__iter__()

for it in a2:
    print(it)
