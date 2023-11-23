def formatStr(selector, *args):
    text_templates = [
        'Geben Sie den {0} Wert: ',
        'Ergebnis der {0} von {1} {2} {3} = {4}'
    ]

    if selector == 0:
        value_name = args[0]
        return text_templates[selector].format(value_name)
    elif selector == 1:
        operation, num1, operator, num2, result = args
        return text_templates[selector].format(operation, num1, operator, num2, result)
    else:
        return None

def formatPrint(selector, *args):
    print(formatStr(selector, *args))

def two_decimal(val):
    return f'{val:.2f}'

try:
    wert_01 = float(input(formatStr(0, 'erste')))
    wert_02 = float(input(formatStr(0, 'zweite')))
except ValueError:
    print('Sie sollten nur natürlichen Zahlen eingeben!!!')
else:
    startKey = 0
    operation_name = ['Addition', 'Substraktion', 'Multiplikation', 'Division']
    operation_symbol = ['+', '-', '*', '/']
    try:
        operation_result = [wert_01 + wert_02, wert_01 - wert_02, wert_01 * wert_02, wert_01 / wert_02]
    except ZeroDivisionError:
        print('Wert 2 darf niemals als 0 sein!')
    else:
        wert_01 = two_decimal(wert_01)
        wert_02 = two_decimal(wert_02)

        for name in operation_name:
            formatPrint(1, name, wert_01, operation_symbol[startKey], wert_02, two_decimal(operation_result[startKey]))
            startKey += 1
