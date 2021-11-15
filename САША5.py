# СЛОВАРИК С ВОЗРАСТОМ И ИМЯ ЧТОБЫ БЫЛО
a = list(map(str,input().split()))
b = list(map(int,input().split()))
def uxox(a,b):
    c = {}
    if len(a) == len(b):
        c = dict(list(zip(a,b)))
    else:
        print("Списки имеют разную длину")
    print(c)
uxox(a,b)


