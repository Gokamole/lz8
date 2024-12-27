def partition(n, min_number=1):
    if n == 0:
        return [[]]  # Базовый случай: если осталась ноль, возвращаем пустое разбиение
    parts = []
    for i in range(min_number, n + 1):  # Проходим от min_number до n
        for part in partition(n - i, i):  # Рекурсивный вызов для оставшегося числа
            parts.append([i] + part)  # Добавляем текущее число к каждому разбиению
    return parts

def print_partitions(n):
    partitions = partition(n)
    for p in partitions:
        print(p)

print_partitions(int(input('Введите число, которое хотите разложить на сумму целых чисел ')))