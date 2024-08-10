my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
n = 0
len_my_list = len(my_list)
while n < len_my_list:
    if my_list[n] >= 0:
        if my_list[n] > 0:
            print(my_list[n])
    else:
        break
    n = n + 1
    