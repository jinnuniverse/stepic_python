def get_command(nms, var):
    parent_key = ''

    #print('11111111111111111111111111nms_name = ', nms)
    #print('var_name = ', var)

    #print('nms_dict = ', nms_dict)

    if nms in nms_dict.keys():

        if parent_key != '':
            nms = parent_key

        if var in nms_dict[nms]['variables']:
            return print(nms)

        else:

            #print('parent_key = ', parent_key)
            #print('nms = ', nms)


            parent_key = nms_dict[nms]['parent']

            #if parent_key == 'None':
            #    return print('None')

            return get_command(parent_key, var)

            #print('33333333333key = ', key)
            #print('var = ', var)

    else:
        #print('TEEEEEEEEEEEEEEEEEEEEST')
        #print('nms_dict = ', nms_dict)

        if len(nms_dict) > 0:
            if var in nms_dict['global']['variables']:
                return print('global')
            else:
                return print('None')
        else:
            return print('None')


n_str = input()

if n_str.isdigit():

    n = int(n_str)

    if n > 0:

        nms_dict = dict()

        for i in range(n):

            #param_str = stdin.readline()
            #param_lst.append(param_str.split())

            #print('param_lst = ', param_lst)

            #for r in range(len(param_lst)):

            #    if len(param_lst[r]) == 3:

                command, nms_name, var_name = input().split()

                if command == 'create':

                    if len(nms_dict) == 0:

                        nms_dict.update({'global': {'parent': 'None', 'variables': []}})

                    if nms_name not in nms_dict.keys():
                        nms_dict.update({nms_name: {'parent': var_name, 'variables': []}})

                    if var_name not in nms_dict.keys():
                        nms_dict.update({var_name: {'parent': 'global', 'variables': []}})
                        nms_dict.update({nms_name: {'parent': var_name, 'variables': []}})

                elif command == 'add':

                    if len(nms_dict) == 0:

                        if 'global' not in nms_dict.keys():
                            nms_dict.update({'global': {'parent':'None', 'variables': []}})

                    if nms_name not in nms_dict.keys():

                        #print('nms_name = ', nms_name)

                        nms_dict.update({nms_name: {'parent': 'global', 'variables': []}})

                        #nms_dict[nms_name] = dict()
                        #nms_dict[nms_name]['parent'] = 'global'
                        #nms_dict[nms_name]['variables'] = list()

                    nms_dict[nms_name]['variables'].append(var_name)

                elif command == 'get':
                    get_command(nms_name, var_name)
    else:
        print('None')
else:
    print('None')
print('nms_dict = ', nms_dict)