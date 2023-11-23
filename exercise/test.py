# print(3 + 3)
# print("3 + 3")
# print("6 + 1/2 = ", 6 + 1/2)
# print("Aloha")
# print('Aloh', '     a', 'a')

# ------------------------------------------------ #

# name = input('Wie heißt du? ')
# alter = input('Wie alt bist du? ')
# print('Hello,', name + '! Schön, dass du ' + alter + ' Jahre bist!')

# print(3 ** 2) # 3的平方 (**在Python中代表基数的幂)

# zahl = 5

# print(f'{zahl:_<4}')
# print(f'{zahl:_>4}')

# vorname, nachname = 'Jay', 'Cao'
# print(f'{vorname:_^10}')


# if (1 > 0) and (1 != 0):
#     print(True)

# x = 1
# y = 3
# summe = x + y
# while summe < 50:
#     summe = x + y
#     x = x + 2
# print(x)

# a = 1
# summe = 0
# while a < 5:
#     summe = summe + a
#     if(a > 3):
#         summe = summe - 1
#     a = a + 1
# print(summe)


# a = 18
# b = 30
# while a > 0 and b > 0:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a

# if b == 0:
#     print(a)
# else:
#     print(b)



# richtig = 0
# falsch = 0

# eingabe1 = input("Hauptstadt von Frankreich? ")
# if eingabe1 == "Paris":
#     richtig += 1
# else:
#     falsch += 1

# eingabe2 = int(input("Quadrat von 13? "))
# if eingabe2 == 169:
#     richtig += 1
# else:
#     falsch += 1

# print("Du hattest", richtig, "richtige und", falsch, "falsche Antwort/en.")


Gesamtminuten = float(input("Gesamtminuten: "))
Stunden = Gesamtminuten // 60
Minuten = Gesamtminuten % 60

print("{0} Stunden {1} Minuten".format(Stunden, Minuten))