# 1.1
Написана функция для решения задачи - с использованием рекурсии, ни используя глобальные переменные и прочие средства хранения состояния между вызовами.

Если переданный список пустой, функция возвращает 0.

Создаётся переменная total, которую инициализируем с нуля для подсчёта элементов.

Функция проходит циклом по каждому элементу списка:

  Если элемент является вложенным списком (проверка с помощью isinstance), рекурсивно вызывается функция count для этого элемента, и результат добавляется к total.
  После проверки элемента, total увеличивается на 1 для каждого элемента, вне зависимости от того, является ли он простым или вложенным.

Возврат результата

![image](https://github.com/QNekoma/python_labs3/assets/147964939/4c4fdd54-7c89-471d-99ef-9bdcee01fef9)

# 1.2
Написана функция для решения задачи - без использованием рекурсии, и глобальных переменных и прочих средств хранения состояния между вызовами.

Инициализация переменных:

  total инициализируется нулём. Эта переменная будет использоваться для счета общего количества элементов.
  number создаётся как копия переданного списка lst, чтобы не изменять оригинал.

Цикл обработки элементов:

   Используется while number, чтобы выполнять цикл, пока список number не станет пустым.
   В каждой итерации из number извлекается последний элемент с помощью метода pop().
   Если извлечённый элемент является списком, он добавляется обратно в number с помощью extend(). Это позволяет "разворачивать" вложенные списки и учесть все их элементы.
   Увеличивается значение total на 1 для каждого извлечённого элемента.

Возврат результата:
![image](https://github.com/QNekoma/python_labs3/assets/147964939/e7719f2d-7895-4aed-962e-715ca14a3c53)

# 2.1
Написана функция для решения задачи - с использованием рекурсии, ни используя глобальные переменные и прочие средства хранения состояния между вызовами.

Определение функции calculate_recursion(i)*:
    Функция принимает целочисленный аргумент i.
    Для базовых случаев:

Для случаев, когда i больше 2, функция рекурсивно вызывает себя дважды с аргументами i-1 и i-2 и применяет заданные математические операции.

Возвращаемое значение рассчитывается по заданной формуле

Обработка пользовательского ввода:
    Запрашивается ввод целого числа у пользователя.
    Если ввод корректный, вызывается функция calculate_recursion с переданным значением, и выводится результат.
    В случае некорректного ввода (например, если пользователь ввёл нечисловое значение), генерируется исключение ValueError, и выводится соответствующее сообщение.

![image](https://github.com/user-attachments/assets/51194ea0-2f07-403b-89c7-64d75359f5d8)


# 2.2
Написана функция для решения задачи - без использованием рекурсии, и глобальных переменных и прочих средств хранения состояния между вызовами.
Создан массив results, где будут храниться рассчитанные значения. Замена глобальных переменных

Условия для i = 1 и i = 2: остаются без изменений.

Цикл: Вместо рекурсии, использовал for-цикл, чтобы пройти от 3 до i и рассчитать значения по заданной формуле, используя ранее вычисленные значения из массива results.

В конце возвращается значение для заданного i.
![image](https://github.com/user-attachments/assets/b8aee4d2-d044-4452-b294-2c0ff8127f73)

