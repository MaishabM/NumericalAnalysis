'''india = ["mumbai", "banglore", "chennai", "delhi"]
   pakistan = ["lahore","karachi","islamabad"]
   bangladesh = ["dhaka", "khulna", "rangpur"]'''
#i) Write a program that asks user to enter a city name and it should tell which country the city belongs to
#ii) Write a program that asks user to enter two cities and it tells you if they both are in same country or not.
#For example if I enter mumbai and chennai, it will print "Both cities are in India"
# but if I enter mumbai and dhaka it should print "They don't belong to same country"

india = ['mumbai','bangalore','chennai','delhi']
pakistan = ['lahore','karachi','islamabad']
bangladesh = ['dhaka','khulna','rangpur']
print('Enter a city name: ')
city = input().lower()
if city in india:
    print('The city belongs to India')
elif city in pakistan:
    print('The city is in Pakistan')
elif city in bangladesh:
    print('The city is in Bangladesh')
else:
    print('The city is not in the list')
#^^^ first ques solution

print('Enter two cities: ')
c1,c2 = input().lower().split()
if c1 in india and c2 in india:
    print('Both cities are in India.')
elif c1 in pakistan and c2 in pakistan:
    print('Both cities are in Pakistan')
elif c1 in bangladesh and c2 in bangladesh:
    print('Both cities are in Bangladesh')
else:
    print("They don't belong in the same country.")
#^^^ second ques solution


# Write a python program that can tell you if your sugar is normal or not.
# Normal fasting level sugar range is 80 to 100.
# i)Ask user to enter his fasting sugar level
# ii)If it is below 80 to 100 range then print that sugar is low
# iii)If it is above 100 then print that it is high otherwise print that it is normal

sugar = int(input('What is your sugar level? '))
if sugar<80:
    print('Your sugar level is low.')
elif sugar>100:
    print('Your sugar level is high.')
else:
    print('Your sugar level is normal.')