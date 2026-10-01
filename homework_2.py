import re
from typing import Callable


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

# Створили функцію яка приймає рядок з аргументом
def generator_numbers(text: str):
    
    # Використали регулярні вирази для ідентифікації дійсних чисел у тексті, з урахуванням, що числа чітко відокремлені пробілами.
    numbers = re.findall(r'\b\d+(?:\.\d+)?\b', text)
     
    for number in numbers:
        yield float(number)  # Застосуйте конструкцію yield у функції generator_numbers для створення генератора.
        
# Створили функцію яка використовує генератор функції generator_numbers.       
def sum_profit(text: str, func: Callable):
    total = 0
    
    for number in func(text):
        total += number
    return total
       
     
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")   