def josephus(n, k):
    result = 0
    for i in range(1, n + 1):
        result = (result + k) % i
    return result + 1  

n = 100
k = 2
last_person = josephus(n, k)
print("The last person with the knife is at position:", last_person)
