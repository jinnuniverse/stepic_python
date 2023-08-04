#lst = [int(input()) for i in range(int(input()))]
#print(sum(lst))

#objects = [1, '2', True, {1: 'a', 2: 'b', 3: 'c'}, 67, '90']
objects = [1, 2, 1, 2, 3, True, False, '78', {1: 'a', 2: 'b', 3: 'c'}, 'false', [], (1, '45', 7, True, 67.9)]
s = {}
cnt = 0
for obj in objects:

    for i in range(len(objects)):
        if obj is objects[i]:
            if type(obj) not in s:

                str_type = (str(type(obj)).split()[1])
                str_type_class = str_type[0:len(str_type)-1]
                if str_type_class != "'dict'" and str_type_class != "'list'" and str_type_class != "'set'" and str_type_class != "'tuple'":

                    s[type(obj)] = 1
                    cnt += 1
                    break
                else:
                    print('objects[i] = ', objects[i])
                    if len(objects[i]) > 0:
                        for k in objects[i]:
                            if type(k) not in s:
                                s[type(k)] = 1
                                cnt += 1
                    else:
                        s[type(objects[i])] = 1
                        cnt += 1


print(cnt)
print('s = ', s)