import math

try:
    inputted = float(input('Geben Sie die gesamten Minuten: '))

    stunden = inputted / 60
    kombination = math.modf(stunden)

    # destruction of <type: tuple("kombination")>
    (minuten, stunde) = kombination

    stunde = round(stunde)
    minuten = round(minuten * 60)

    print('Gegebenen Minuten in Stunden ist:', str(stunde), 'Stunde', str(minuten), 'Minuten')
except:
    print('Sie sollten nur natürlichen Zahl eingeben!!!')