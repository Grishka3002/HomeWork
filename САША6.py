# от маленького к большому)
a = list(map(int, input().split(',')))
def axox(a):
    for i in range(len(a)):
        minchislo = i
        for j in range(i + 1, len(a)):
            if a[j] < a[minchislo]:
                minchislo = j
        a[minchislo],a[i] = a[i],a[minchislo]
    print(a)
axox(a)
