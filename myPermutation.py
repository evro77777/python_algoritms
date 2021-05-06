def find(arr, pref):
    flag = False
    for i in range(len(pref)):
        if arr[0] == pref[i][0] and arr[1] == pref[i][1]:
            flag = True
            break
    return flag


def generate_permutations(s: str, m:int=-1, prefix=None):
    """Генерация всех перестановок строки
        с префиксом prefix
    """
    m = len(s) if m == -1 else m
    prefix = prefix or []
    if m == 0:
        for x in prefix:
            print(x[0],end="")
        print(end="\n")
        return
    for i in range(len(s)):
        if find([s[i],i], prefix):
            continue
        prefix.append([s[i],i])
        generate_permutations(s, m - 1, prefix)
        prefix.pop()



generate_permutations("abac")

