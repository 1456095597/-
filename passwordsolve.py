n = input()
c_m = 0
for i in range(0, len(n) - 1):
    c = 0
    j = i - 1
    m = i + 1
    if n[i] == n[m]:
        j = i
    elif n[i] == n[j]:
        m = i
    else:
        c = 1
    while (j > 0) and (m < len(n)):
        if n[j] == n[m]:
            c += 2
        else:
            break
        j -= 1
        m += 1
    if c > c_m:
        c_m = c
print(c_m)