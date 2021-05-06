def find(number, arr):
    """ищет number в arr и возвращает True если такой есть
    иначе - False
    """
    flag = False
    for x in arr:
        if number == x:
            flag = True
            break
    return flag

def generate_permutations(n:int,m:int=-1,prefix=None):
    """Генерация всех перестановок n чисел в m позициях
        с префиксом prefix
    """
    m=n if m==-1 else m
    prefix = prefix or []
    if m == 0:
        print(prefix)
        return
    for number in range(1,n+1):
        if find(number,prefix):
            continue
        prefix.append(number)
        generate_permutations(n,m-1,prefix)
        prefix.pop()

generate_permutations(5)