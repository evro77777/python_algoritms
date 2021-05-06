def merge(a:list, b:list):
    c = [0] * (len(a)+len(b))
    i=k=n=0
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            c[n] = a[i]
            i += 1
            n += 1
        else:
            c[n] = b[k]
            k += 1
            n += 1
    while i < len(a):
        c[n] = a[i]
        i += 1
        n += 1
    while k < len(b):
        c[n] = b[k]
        k += 1
        n += 1
    return c

def merge_sort(a):
    if len(a) <= 1:
        return
    middle = len(a)//2
    l = [a[i] for i in range(0,middle)]
    r = [a[i] for i in range(middle,len(a))]
    merge_sort(l)
    merge_sort(r)
    c=merge(l,r)
    for i in range(len(a)):
        a[i] = c[i]
    return a
print(merge_sort([6,1,7,2,9,8]))  