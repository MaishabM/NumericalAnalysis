weight = float(input('Weight = '))
unit = input('l for Lbs or k for Kg: ')
check = unit.upper()

if check=='L':
    print(f'in Kg: {weight*0.453592}')
elif check =='K':
    print(f'in Lbs: {weight*2.20462}')
else:
    print('Wrong input')

