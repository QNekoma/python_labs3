def calculate_recursion(i):
    if i == 1:
        return 1
    elif i == 2:
        return -1/8
    else:
        return ((i-1) * calculate_recursion(i-1)) / 3 + ((i-2) * calculate_recursion(i-2)) / 4

try:
    user_input = int(input("Введите целое число для расчёта (i): "))
    result_recursion = calculate_recursion(user_input)
    print(f"Результат для i = {user_input}: {result_recursion}")
except ValueError:
    print("Пожалуйста, введите целое число.")
