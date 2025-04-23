#Create 3 variables to store street, city and country, now create address variable to store entire address.
# Use two ways of creating this variable, one using + operator and the other using f-string.
# Now Print the address in such a way that the street, city and country prints in a separate line

street = 'Shahid Baki Sharak'
city = 'Dhaka'
country = 'Bangladesh'
address = 'Street: ' +street+ '\nCity: ' +city+ '\nCountry: ' +country
print('Address: ',address)
#^^^ first method

print(f'Street: {street}\nCity: {city}\nCountry: {country}')
#^^^ second method

#Create a variable to store the string "Earth revolves around the sun"
#Print "revolves" using slice operator
#Print "sun" using negative index

store = 'Earth revolves around the sun'
print(f'The word is- {store[6:14]}')
print(f'The second word is- {store[-3:]}')


#Create two variables to store how many fruits and vegetables you eat in a day.
# #Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday
# #Use python f string for this

print('How many fruits do you eat everyday? ')
fruit = int(input())
print('How many vegetables do you eat everyday? ')
veg = int(input())
print(f'I eat {veg} veggies and {fruit} fruits daily.')


#I have a string variable called s='maine 200 banana khaye'.
# #This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'.
# #Replace incorrect words in original string with new ones and print the new string.
# #Also try to do this in one line.

s = 'maine 200 banana khaye'
print(s.replace('200 banana','10 samosa'))