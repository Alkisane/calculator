import time


class ModularCalculator:
    
    #Данный класс включает в себя арсенал методов разнообразных незаменимых инструментов, необходимых для ежедневных вычислений в рамках объектно-ориентированной разработки.
    
    def add(self, numbers):
        """"Возвращает произведение чисел в числах.
        >>> add([6, 4])
        25
        >>> add([1, 0])
        1
        """ ""
        result = 0
        for number in numbers:
            result += number
        return result

    def subtract(self, numbers):
        """"Возвращает разницу между первым введенным числом и остальными введенными числами.
        >>> subtract([6, 4])
        2
        >>> subtract([10, 5, 5]) # 10 - 5 - 5
        0
        """ ""
        return numbers[0] - ModularCalculator.add(numbers[1:])

    def multiply(self, numbers):
        """"Возвращает произведение чисел в числах.
        >>> multiply([6, 4])
        24
        >>> multiply([1, 0])
        0
        """
        init = 1
        result = numbers[0]
        rest = [elem for elem in numbers[1:]]
        if 0 in numbers:
            return 0
        for rest_elem in rest:
            init = init * rest_elem
        result = result * init
        return result

    def divide(self, numbers):
        """"Функция высшего порядка, возвращающая частное числа в числах.
        >>> divide([6, 4])
        24
        >>> divide([8, 4, 2]) # 8 * 1/4 * 1/2
        1
        >>> divide([1, 0])
        Невозможно разделить на ноль. 
        """
        try:
            return numbers[0] / ModularCalculator.multiply(self, numbers[1:])
        except ZeroDivisionError:
            return 'Невозможно разделить на ноль.'

    def two_integer_exponentiate(self, base, exponent):
        """"Возвращает результат возведения основания в показатель степени, где основание и показатель степени являются целыми числами.
        >>> two_integer_exponentiate([3, 2])
        24
        >>> two_integer_exponentiate([1, 0])
        1
        >>> two_integer_exponentiate([3, 999999])
        5992367055585812... # ≈ 5.99 x 10^477120
        """
        result = 1
        i = 0
        if not isinstance(base, int) or not isinstance(
                exponent, int
        ):  # вводится в случае, если другой main() не навязывает только целочисленные значения.
            return 'База и показатель степени должны быть целыми числами.'
        if exponent == 0 or base == 1:
            return 1
        elif base == 0:
            return base
        while i < abs(exponent):  # учитывает случай отрицательного показателя.
            if exponent < 0:
                result = ModularCalculator.multiply(
                    self,
                    [result, ModularCalculator.divide(self, [1, base])])
            elif exponent > 0:
                result = ModularCalculator.multiply(self, [result, base])
            i = ModularCalculator.add(self, [i, 1])
        return result


if __name__ == '__main__':

    obj = ModularCalculator()
    print('Добро пожаловать в модульный калькулятор!')

    while True:
        choice = input(
            'Выберите операцию\n'
            '1) Плюс 2) Минус 3) Умножить 4) Поделить 5) Двухцелое возведение в степень 6) Выход\n'
        )
        if choice not in "123456":
            print("Неверный Ввод. Пожалуйста, выберите от 1 до 6.")
            continue
        elif choice == '1':
            summands = [
                float(i) for i in input(
                    'Введите числа, которые вы хотите добавить, через пробел.\n'
                ).split()
            ]
            if len(summands) < 2:
                print(
                    'Неверный номер ввода; принимает не менее двух слагаемых.\n')
                continue
            start_time = time.time()
            print(obj.add(summands))
            print('--- Калькулятор посчитал все за %s секунд(ы)! ---' %
                  (time.time() - start_time))
        elif choice == '2':
            args = [
                float(i) for i in input(
                    'Введите числа, которые вы хотите вычесть из первого, через пробел.\n'
                    'Для 8 - 4 - 4: "8 4 4"\n'
                    'Примечание. Все числа, следующие за первым, будут вычтены из первого.\n'
                ).split()
            ]
            if len(args) < 2:
                print(
                    'Неверный номер ввода; принимает не менее двух слагаемых.\n')
                continue
            start_time = time.time()
            print(obj.add(args))
            print('--- Калькулятор посчитал все за %s секунд(ы)! ---' %
                  (time.time() - start_time))

        elif choice == '3':
            multicands = [
                float(i) for i in input(
                    'Введите числа, которые вы хотите умножить, через пробел.\n'
                ).split()
            ]
            if len(multicands) < 2:
                print(
                    'Неверный номер ввода; требуется как минимум две мультиканды.\n'
                )
                continue
            start_time = time.time()
            (print(obj.multiply(multicands)))
            print('--- Калькулятор посчитал все за %s секунд(ы)!---' %
                  (time.time() - start_time))
        elif choice == '4':
            args = [
                int(i) for i in input(
                    'Введите делимое и делитель(и). Для 6 ÷ 4 ÷ 2: «6 4 2»\n'
                ).split()
            ]
            if len(args) < 2:
                print(
                    'Неверный номер ввода; принимает 1 делимое и 1 или более делителей.\n'
                )
                continue
            start_time = time.time()
            print(obj.divide(args))
            print('--- Калькулятор посчитал все за %s секунд(ы)! ---' %
                  (time.time() - start_time))
        elif choice == '5':
            try:
                args = [
                    int(i) for i in input(
                        'Введите основание и показатель степени, разделенные пробелом. Для 3^2: «3 2».\n'
                    ).split()
                ]
                base, exponent = args[0], args[1]
            except ValueError:
                print(
                    'Основание и показатель степени должны быть целыми числами. Пожалуйста, попробуйте еще раз.'
                )
                continue
            if len(args) != 2:
                print(
                    'Неверный номер ввода; принимает только 2 аргумента: 1 основание и 1 показатель степени.\n'
                )
                continue
            start_time = time.time()
            print(obj.two_integer_exponentiate(base, exponent))
            print('--- Калькулятор посчитал все за %s секунд(ы)! ---' %
                  (time.time() - start_time))
        else:
            print('До свидания!')
            break
