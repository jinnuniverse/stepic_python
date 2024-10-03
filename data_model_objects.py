#objects = [1, 2, 1, 2, 3, True, False, '78', {1: 'a', 2: 'b', 3: 'c'}, [], (1, '45', 7)]
#objects = [1, 2, 0, 3, 4, 1, True, True, False, [True], None, [None, 1, True], {None}, {1: None}, [False, 1], {345}, {345}, 1, [2], 1, [2], 3, bin(1), bin(3), '0b1', '0b11', 0b11, 0b1]
s = set()

for obj in objects:

    if id(obj) not in s:
        s.add(id(obj))

print(len(s))