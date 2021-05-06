def pifunc_str(a: str):
    p = [0] * len(a)
    j = 0
    i = 1
    while i < len(a):
        if a[i] != a[j]:
            if j == 0:
                p[i] = 0
                i += 1
            else:
                j = p[j - 1]
        else:
            p[i] = j + 1
            i += 1
            j += 1
    return p


def kmp(s: str, sub: str):
    k = 0
    l = 0
    res = list()
    p = pifunc_str(sub)
    while k < len(s):
        if s[k] == sub[l]:
            k += 1
            l += 1
            if l == len(sub):
                res.append(k-len(sub))
                l = 0
        else:
            if l == 0:
                k += 1
                if(k == len(s)):
                    res.append(-1)
            else:
                l = p[l - 1]
    return res


print(kmp("abcab=abcabd","abcabd"))
