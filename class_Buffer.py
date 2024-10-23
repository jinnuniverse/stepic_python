class Buffer:
    def __init__(self):
        self.a = list()

    def add(self, *a):
        if len(self.a) == 0:
            self.a = list(a)
        else:
            self.a += list(a)

        len_a = len(self.a)

        if len_a >= 5:
            cycle = int(len_a / 5)

            if cycle > 1:
                print('self.a = ', self.a)
                print('cycle = ', cycle)
                for j in range(cycle):
                    print(sum(self.a[0:5]))

                    for i in self.a[:5]:
                        self.a.remove(i)
                        cycle -= 5
            elif cycle == 1:
                if len(self.a) >= 5:
                    print(sum(self.a[0:5]))

                    for i in self.a[:5]:
                        self.a.remove(i)

    def get_current_part(self):
        return self.a

'''
buf = Buffer()
buf.add()
a = buf.get_current_part()
print(a)
buf.add(4, 5, 6)
a = buf.get_current_part()
print(a)
buf.add(7, 8, 9, 10)
a = buf.get_current_part()
print(a)
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
a = buf.get_current_part()
print(a)
buf.add(4,6,7,3)
a = buf.get_current_part()
print(a)
'''