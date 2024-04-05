#F-String: Beispiele
name = "Max"
alter = 25
output = "Hallo %s, Du bist %d Jahre alt" % (name, alter)
output2 = "Hallo {0}, Du bist {1} Jahre alt".format(name, alter)
output3 = "Hallo {}, Du bist {} Jahre alt".format(name, alter)
output4 = "Hallo {NAME}, Du bist {ALTER} Jahre alt".format(NAME=name, ALTER=alter)
output5 = f"Hallo {name}, Du bist {alter} Jahre alt"
print(output)
print(output2)
print(output3)
print(output4)
print(output5)

vorname, nachname = 'Ralf', 'Hersel'
print(f'{vorname:^10}')
print(f'{vorname:>20}{nachname:>20}')
print(f'{vorname:<20}{nachname:<20}')

f, n, m = 123.45, 123, 123456789
print(f'{f:.4f}')
print(f'{n:08}')
print(f'{m:,}')
print(f'{m:_}')

zahl = 42
print (f'{zahl:<4}' )
print (f'{zahl:_<4}')
print (f'{zahl:04d}')

grösse=1.827
print(f'{grösse:.5f}')
print(f'{grösse:.2f}')
print(f'{grösse:0>12.5f}')
