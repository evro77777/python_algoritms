def generate_numbers(n: int, m: int, prefix=None):
    """Генерирует все числа (с лидирующими нулями)
    в n-ричной системе счисления (n<=10)
    длины m"""
    prefix = prefix or []
    if m == 0:
        print( prefix)
        return
    for digit in range(n):
        prefix.append(digit)
        generate_numbers(n, m - 1, prefix)
        prefix.pop()





def gen_bin(m, prefix=""):
    """генерирует все числа для двоичной сис.сч."""
    if m == 0:
        print(prefix)
        return
    for digit in "0", "1":
        gen_bin(m-1, prefix+digit)


generate_numbers(2,2)