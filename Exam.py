def nth_term_arithmetic_progression(a, d, n):
    return a + (n - 1) * d

if __name__ == "__main__":
    n = int(input("Введіть номер члена арифметичної прогресії: "))
    a = 5
    d = 2
    nth_term = nth_term_arithmetic_progression(a, d, n)
    print(f"{n}-й член арифметичної прогресії: {nth_term}")
