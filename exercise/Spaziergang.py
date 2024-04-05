'''
Sie stehen in Ingolstadt, sind in zehn Minuten verabredet,
möchten aber nicht zu früh erscheinen.
Deshalb wollen Sie einen Spaziergang machen,
der genau 10 Minuten dauert.
Der Spaziergang ['n','s','n','s','o','w','n','s','n','s'] ist
dazu geeignet, wenn Sie von einer Straßenecke zur nächsten
genau 1 Minute brauchen. Die Buchstaben stehen hier
für Himmelsrichtungen, in die Sie nacheinander gehen können.
Schreiben Sie eine Funktion spaziergang(),
die solche Arrays als Argument erwartet und einen Wahrheitswert
zurückliefert, der angibt, ob der Spaziergang in Frage kommt.
Neben der Dauer müssen Sie dazu auch überprüfen,
ob Sie anschließend wieder an Ihrem Ausgangspunkt ankommen.
'''


#Funktion spaziergang, die eine route als Liste bekommt
#und prüft, ob der Spaziergang 10 Minuten in Form von 10
#Listenelementen dauert


#Variable x (Himmelsrichtung Ost und West) und y (Himmelrichtung Nord und Süd) mit 0


#For-Schleife (0, len(route)) und step = route[i]
#und if-Verzweigung für Prüfung auf n, s, o, w


    #Print "Ausgangspunkt erreicht", wenn x und y == 0 ist


x = 0
y = 0

def direction(str):
    global x, y
    msg = 'Sie gehen 1 Schritt nach {0};'
    if str == 'n':
        y += 1
        msg = msg.format('Nord')
    elif str == 's':
        y -= 1
        msg = msg.format('Süd')
    elif str == 'w':
        x -= 1
        msg = msg.format('West')
    elif str == 'o':
        x += 1
        msg = msg.format('Ost')
    print(msg, f'Aktuelle Koordinaten ist: ( {x} | {y} )')

    if x == 0 and y == 0:
        print('+++Sie sind wieder in Startpunkt!+++')

def spaziergang(array):
    array_len = len(array)

    if array_len != 10:
        print('Sparziergang dauert nicht 10 Minuten!')
        return
    else:
        for i in range(0, array_len):
            direction(array[i])

#Funktionsaufruf spaziergang
spaziergang(['n','s','n','s','w','o','o','w','o','w'])
