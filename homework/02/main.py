#task 1

def rectange_square(a: int, b: int) -> str:
    result = a * b
    return f"Rectangle with sides {a} and {b} is has square {result}"

print(rectange_square(2, 3))


# task 3

def is_year_leap() -> bool:
    year = int(input("Введіть рік: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

print(is_year_leap())


# task 4

def table() -> None:
    number = int(input("Введіть число для таблиці множення: "))
    
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

table()


# task 5

def numbers() -> None:
    number = 1
    total = 0
    while number <= 50:
        is_odd = number % 2 != 0
        if is_odd:
            total += number
        number += 1
    print(f"Сума непарних чисел від 1 до 50: {total}")

numbers()


# task 6

def create_full_name(first_name: str, last_name: str = "Іванов") -> str:
    return " ".join([last_name, first_name])


full_name1 = create_full_name(first_name="Петро", last_name="Петренко")
print(f"Повне ім'я: {full_name1}")
full_name2 = create_full_name(first_name="Олена")
print(f"Повне ім'я: {full_name2}")
