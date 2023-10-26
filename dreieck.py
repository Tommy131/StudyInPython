try:
    a = float(input('Geben Sie eine Länge des Dreieck: '))
    b = float(input('Geben Sie noch eine Länge des Dreieck: '))
    einheit = input('Geben Sie die Einheit: ')

    print('Gegebenen Längen sind: ' + 'a = ' + str(a), einheit + '; b = ' + str(b), einheit)

    area = a * b / 2

    print('Fläche des Dreieck: ' + str(area), einheit + '^2')
except:
    print('Sie sollten nur natürlichen Zahl eingeben!!!')