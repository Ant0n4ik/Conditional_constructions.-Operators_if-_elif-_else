one = int(input('Введите первое число: '))
two = int(input('Введите второе число: '))
three = int(input('Введите третье число: '))
if one == two == three:
    print(3)
elif one == two or one == three or two == three:
    print(2)
elif one != two or one != three or two != three:
    print(0)