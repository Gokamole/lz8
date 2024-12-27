def sum_of_divisors(n, divisor=1):
    if divisor > n // 2:                # Eсли делитель больше половины числа, то выходим
        return 0
    if n % divisor == 0:                # Если делитель делит n нацело, то мы добавляем делитель к результату, продолжаем рекурсию, увеличивая делитель на 1
        return divisor + sum_of_divisors(n, divisor + 1)
    else:                               # Если n не делится на делитель, просто продолжаем рекурсию с увеличенным делителем
        return sum_of_divisors(n, divisor + 1) 

def is_perfect_number(n):
    if n <= 1:                          # Если n меньше или равно 1, возвращаем False
        return False
    return sum_of_divisors(n) == n

number = int(input('Введите число, которое хотите проверить '))
if is_perfect_number(number):
    print(f"{number} является совершенным числом.")
else:
    print(f"{number} не является совершенным числом.")