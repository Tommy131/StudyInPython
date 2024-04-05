from math import sqrt

def nullstellen():
    a = float(input('Bitte geben Sie den Wert a: '))
    b = float(input('Bitte geben Sie den Wert b: '))
    c = float(input('Bitte geben Sie den Wert c: '))

    diskriminante = b ** 2 - 4 * a * c
    if diskriminante < 0:
        print('Es gibt kein Ergebnis, weil die Diskriminante ist kleiner als 0!')
    else:
        x1 = (0 - b + sqrt(diskriminante)) / 2 * a
        x2 = (0 - b - sqrt(diskriminante)) / 2 * a

        if b < 0:
            b = abs(b)
            b = f'- {b}'
        else:
            b = f'+ {b}'

        if c < 0:
            c = abs(c)
            c = f'- {c}'
        else:
            c = f'+ {c}'

        gleichung = f'{a}x^2 {b}x {c}'
        print(f"Die Nullstellen der Funktion [ {gleichung} ] sind: ({x1} | 0) und ({x2} | 0)")