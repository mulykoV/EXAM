def nth_term_arithmetic_progression(a, d, n):
    return a + (n-1) * d

#Введення значень
n = int(input("Введіть номер чену арифметичної прогресії: "))

a=5
d=2

#Розрахунок
nth_term = nth_term_arithmetic_progression(a, d, n)
print(f"{n}-й член арифметичної прогресії: {nth_term}")