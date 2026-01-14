lst = [5, 2, 9, 1, 7, 6]
n = len(lst)

for i in range(n):
    for j in range(i + 1, n):
        if lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print("List in descending order:", lst)
