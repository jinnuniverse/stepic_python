elem_cnt, comb_cnt = map(int, input().split())

#pairs_lst = [[0 for j in range(k)] for i in range(n)]
pairs_lst = []

print('pairs_lst = ', pairs_lst)

def comb_function(n, k):

    if n < k:
        c_res = 0

    if n == k:
        c_res = 1

    if n > k and k == 0:
        c_res = 1

    else:

        c_res = comb_function(n - 1, k) + comb_function(n - 1 , k - 1)


comb_function(elem_cnt, comb_cnt)



