"""
Задание 2.
Реализуйте две версии функции, которая генерирует первые n чисел Фибоначчи.
Первая версия функции должна быть обычной функцией, которая возвращает список чисел Фибоначчи,
а другая версия должна быть функцией-генератором, которая производит числа Фибоначчи по одному.
Сравните использование памяти и производительность во время выполнения обеих реализаций
и поделитесь своими результатами.

Тесты:
1.	n = 100 000
2.	n = 1 000 000
3.	n = 10 000 000
"""

import sys
import time
from typing import Generator, List

sys.set_int_max_str_digits(1000000)


def get_fibonacci_list(numbers: int) -> List[int]:
    fib_sequence = []

    if numbers < 0:
        raise ValueError("числа должны быть неотрицательными")
    elif numbers == 0:
        fib_sequence.append(0)
    elif numbers == 1:
        fib_sequence.append(0)

    prev_num = 0
    curr_num = 1

    for _ in range(numbers):
        fib_sequence.append(prev_num)
        prev_num, curr_num = curr_num, prev_num + curr_num
    return fib_sequence


def get_fibonacci_generator(numbers: int) -> Generator[int, None, None]:
    if numbers < 0:
        raise ValueError("числа должны быть неотрицательными")
    elif numbers == 0:
        yield 0
    elif numbers == 1:
        yield 0
        return
    else:
        prev_num: int = 0
        curr_num: int = 1

        for _ in range(numbers):
            yield prev_num
            prev_num, curr_num = curr_num, prev_num + curr_num


if __name__ == '__main__':
    numbers: int = 300000

    start_time = time.time()
    fib_list = get_fibonacci_list(numbers)
    end_time = time.time()
    time_list = end_time - start_time

    start_time = time.time()
    fib_gen = get_fibonacci_generator(numbers)
    for num in fib_gen:
        pass
    end_time = time.time()
    time_gen = end_time - start_time

    print(f"Время выполнения списка: {time_list:.6f} секунд")
    print(f"Время выполнения генератора: {time_gen:.6f} секунд")

    print(f"Ускорение: {(time_list / time_gen):.2f}x")

"""
Результаты:
При n = 100000:
Время выполнения списка: 0.145756 секунд
Время выполнения генератора: 0.115855 секунд
Ускорение: 1.26x

При n = 200000:
Время выполнения списка: 0.589516 секунд
Время выполнения генератора: 0.462256 секунд
Ускорение: 1.28x

При n = 300000:
Время выполнения списка: 1.298429 секунд
Время выполнения генератора: 1.092308 секунд
Ускорение: 1.19x

Вывод:
В разный период времени время в зависимости от самой машины, где выполняется код, и от заданного числа n,
можем заметить, что время выполнения генератора меньше времени выполнения списка. 
Соотсветственно, на моей машине время выполнения генератора в 1,3-5 раза быстрее чем время выполнения списка.
По памяти выполнение генератора занимает меньше памяти чем выполнение списка.

Если нужно получить список первых n чисел Фибоначчи, лучше использовать функцию get_fibonacci_list.
Если нужно поочередно получать числа Фибоначчи и важна произодитлеьность, 
то лучше использовать функцию get_fibonacci_generator. 
"""
