# Задание №4
# Найти сумму целых положительных чисел
# из промежутка от a до b, кратных четырём.

def sum_multiples_of_4(a, b):
    """Возвращает сумму целых положительных чисел из [a, b], кратных 4."""
    if a > b:
        a, b = b, a
    if a < 1:
        a = 1

    total = 0
    for number in range(a, b + 1):
        if number % 4 == 0:
            total += number
    return total


def count_multiples_of_4(a, b):
    """Возвращает количество чисел, кратных 4, из [a, b]."""
    if a > b:
        a, b = b, a
    if a < 1:
        a = 1
    return len([n for n in range(a, b + 1) if n % 4 == 0])


def is_multiple_of_4(number):
    """Проверяет, кратно ли число 4."""
    return number % 4 == 0


print("  СУММА ЧИСЕЛ, КРАТНЫХ 4, ИЗ ПРОМЕЖУТКА")


a = int(input("Введите начало промежутка (a): "))
b = int(input("Введите конец промежутка (b): "))

result = sum_multiples_of_4(a, b)
count = count_multiples_of_4(a, b)

print(f"\nЧисел, кратных 4: {count}")
print(f"Их сумма: {result}")

def get_even_multiples(a, b):
    """Возвращает список чисел, кратных 4, из [a, b]."""
    if a > b:
        a, b = b, a
    if a < 1:
        a = 1
    return [n for n in range(a, b + 1) if n % 4 == 0]

def print_summary(a, b):
    """Выводит краткую сводку по промежутку."""
    total = sum_multiples_of_4(a, b)
    count = count_multiples_of_4(a, b)
    numbers = get_even_multiples(a, b)
    print(f"Числа, кратные 4: {numbers}")
    print(f"Количество: {count}")
    print(f"Сумма: {total}")