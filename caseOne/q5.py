l = [2,13,18,93,22]

def func(list):
    even_list = []
    odd_list = []

    for x in list:
        if x%2==0:
            odd_list.append(x)
        else:
            even_list.append(x)

    return even_list,odd_list

even_list,odd_list = func(l)

print(even_list)
print(odd_list)