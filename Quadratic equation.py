"""This is a program for solving quadratic equations of the type:
ax**2 + b*x + c = 0"""


"""Это программа для решения квадратных уравнений типа:
                    ax**2 + b*x + c = 0"""


from fractions import Fraction

# ТОЧНОСТЬ РЕШЕНИЯ - ЗНАКОВ ПОСЛЕ ЗАПЯТОЙ
A = 2
st = ' '
st1 = '_'
mis_input = 'Ошибка: некорректный ввод данных! Повторите ввод.'


def main():
    print()
    print('******* Это программа для решения квадратных уравнений типа: *******')
    print(25*st + 'ax**2 + b*x + c = 0')
    t = 'None'
    while t != 'n':
        while True:
            print()

            # НАСТРОЕН КОРРЕКТНЫЙ ВВОД ТОЛЬКО ЗНАЧЕНИЯ <a>
            a = input('Введите значение <а> : ')
            a = a.replace(' ', '')
            if a.isdigit():
                av = a
                break
            elif '-' in a and '/' not in a:
                a1 = a.replace(a[0], '')
                if a1.isdigit():
                    av = a
                    break
                else:
                    print(mis_input)
            elif ('/' in a and a.index('/') != 0) and \
                    ('/' in a and a.index('/') != len(a)-1):
                if '-' in a and a.index('/') != 1:
                    a1 = a.replace(a[0], '')
                    a2 = a1.replace('/', '', 1)
                    if a2.isdigit():
                        av = a
                        a = Fraction(a)
                        break
                    else:
                        print(mis_input)
                else:
                    a1 = a.replace('/', '', 1)
                    if a1.isdigit():
                        av = a
                        a = Fraction(a)
                        break
                    else:
                        print(mis_input)
            else:
                print(mis_input)


        while True:
            print()
            b = input('Введите значение <b> : ')
            b = b.replace(' ', '')
            if b.isdigit():
                bv = b
                break
            elif b.replace('-', '', 1).isdigit():
                bv = b
                break
            elif '/' in b:
                b1 = b.replace('-', '', 1)
                if b1.replace('/', '', 1).isdigit():
                    bv = b
                    b = Fraction(b)
                    break
                else:
                    print(mis_input)
            else:
                print(mis_input)
        while True:
            print()
            c = input('Введите значение <c> : ')
            c = c.replace(' ', '')
            if c.isdigit():
                cv = c
                break
            elif c.replace('-', '', 1).isdigit():
                cv = c
                break
            elif '/' in c:
                c1 = c.replace('-', '', 1)
                if c1.replace('/', '', 1).isdigit():
                    cv = c
                    c = Fraction(c)
                    break
                else:
                    print(mis_input)
            else:
                print(mis_input)
        print()
        a = float(a)
        b = float(b)
        c = float(c)
        d = b**2 - 4*a*c
        x1 = (-b + d**0.5)/2*a
        x2 = (-b - d**0.5)/2*a
        print(70*st1)
        print(f'Решение квадратного уравнения:'
              f' ({av})x**2 + ({bv})x + ({cv}) = 0')
        print(f'Дискриминант ревен: {d: .{A}f}')
        print(f'x1 = {x1: .{A}f}')
        print(f'x2 = {x2: .{A}f}')
        print(70*st1)
        t = input('Для ПРОДОЛЖЕНИЯ нажмите <любую клавишу> для ВЫХОДА <n> : ')
    print()
    print('*** Программа решения квадратных уравнений: ЗАКРЫТА! ***')


if __name__ == '__main__':
    main()