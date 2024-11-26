def calculate(i):
    if i == 1:
        return 1
    elif i == 2:
        return -1 / 8

    # список для хранения результатов
    results = [0] * (i + 1)
    results[1] = 1
    results[2] = -1 / 8

    for j in range(3, i + 1):
        results[j] = ((j - 1) * results[j - 1]) / 3 + ((j - 2) * results[j - 2]) / 4

    return results[i]

try:
    user_input = int(input("Введите целое число для расчёта (i): "))
    result = calculate(user_input)
    print(f"Результат для i = {user_input}: {result}")
except ValueError:
    print("Пожалуйста, введите целое число.")
