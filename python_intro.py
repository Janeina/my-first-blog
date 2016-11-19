print('Hello, Django girls!')
ziom = {'imie' : 'Jane', 'liczby' : [2, 4, 5]}
if 4 > 3:
    print('It works!')
if 5 > 3:
    print('ok')
else:
    print('nope')


name = 'Jane'
if name == 'Ewa':
    print('Yo, Ewa!')
elif name == 'Jane':
    print('Yo, Jane!')
else:
    print('Yo, ziomalu!')


food = 'duza porcja'
if food == 'mala porcja':
    print('Im hungry')
elif food == 'srednia porcja':
    print('still hungry')
elif food == 'duza porcja':
    print('Im good :)')
else:
    print('where is my food???')


def hej():
    print('Hey!')
    print('How are you?')

hej()

def hej(imie):
    if imie == 'Ania':
        print('Yo, Ania!')
    elif imie == 'Jane':
        print('Hey, Jane!')

hej('Ania')

dziewczyny = ['Ala', 'Jane', 'Zosia', 'Hania', 'Ola']

def hej(imie):
    print('Hej ' + imie + '!')

for imie in dziewczyny:
    hej(imie)

e = [2, 7, 5, 6]
for i in e:
    print(i)
