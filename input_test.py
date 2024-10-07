from sys import stdin

n = int(input())

nms_dict = dict()

nms_list = list()

param_lst = list()

for i in range(n):

    param_str = stdin.readline()
    param_lst.append(param_str.split())

    # print('param_lst = ', param_lst)

    for r in range(len(param_lst)):

        if len(param_lst[r]) == 3:

            # command, nms_name, var_name = input().split()
            command = param_lst[r][0]
            nms_name = param_lst[r][1]
            var_name = param_lst[r][2]

            if command == 'create':
                if var_name == 'global':

                    if len(nms_dict) == 0:
                        nms_list.append(nms_name)

                        nms_dict['global'] = dict()
                        nms_dict['global']['parent'] = 'None'
                        nms_dict['global']['variables'] = nms_list


print('nms_dict = ', nms_dict)
'''
p = list()
s = stdin.readline()

pos = 0



p.append(s.split())

print(p)

print(s)

'''
