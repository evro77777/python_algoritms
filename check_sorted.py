def check_sorted(a, descending=True):
    """Проверка, отсортирован ли массив
        с параметром(по возврастанию или же по
        убыванию)
        descending - по убыванию
    """
    flag = True
    s = 2 * int(descending) - 1
    # при descending = True s = 1
    # при descending = False s = -1
    for i in range(0, len(a) - 1):
        if s * a[i] < s * a[i + 1]:
            flag = False
            break
    return flag


print(check_sorted([3, 2, 1], False))
