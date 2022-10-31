str_in = input().split()

new_list = [[]]

for len_substr in range(len(str_in)):
    for i in range(len(str_in) - len_substr):
        new_list.append(str_in[i:i + len_substr + 1])

print(new_list)
