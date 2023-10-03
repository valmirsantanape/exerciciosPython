soma = 0
for c in range(0, 101):
    if c > 1:
        for i in range(2, c):
            if(c % i == 0):
                break
            else:
                soma += c

print(soma)
