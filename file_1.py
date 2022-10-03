nev = input('írd be a neved: ')
print(f'Hello {nev}!')
print(f'Milyen szép név az, hogy {nev}!')
print(f'Szerintem már most Beléd vagyok zúgva, {nev}! uwu <3')

valasz = input(f'szeretsz programozni {nev}? ')
if valasz == 'igen':
    print('Akkor még itt sokra viheted!')
else:
    print('Akkor remélem, majd megszereted... :(')

print('Na, még két, aztán végeztünk mára:')

szam = int(input('Hányszor írjam ki a meved? '))
for x in range(szam):
    print(f'{nev}', end=' ')

print('\nok, végeztünk, köszönj el szépen!')
while input() != 'Viszlát!':
    print('hát ez nem jött össze, próbáld újra!')
print(f'Rendben {nev}, tmostmár tényleg végeztünk!')
print('Legyen szép napod!')