#Find the area of the football field

height = 92
width = 48.8
print(f'Area of the football field is: {height*width} sq.meter')

#You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar.
# Find out using python, how many dollars is the shopkeeper going to give you back?

total = 1.49*9
print(f'The shopkeeper will give {20-total} dollars back.')


#You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length.
# If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles.
# Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)

Barea = 5.5 ** 2
cost = 500*Barea
print(f'The cost of tiles: {cost}')


#Print binary representation of number 17

num = 17
conv = bin(num)[2:]
print(f'The binary representation of 17: {conv}')
# ^^^ built in method

number = 17
print('The binary conversion of 17 is: ',format(number,'b'))
