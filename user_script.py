"""
# Compare two integers

print("Enter two integers and I will tell you the realationship they satisfy")

number1 = int(input("Enter first integer: "))

number2 = int(input("Enter second integer: "))

#print(number1 + number2)

if number1 == number2: print(number1, "is equal to", number2)

if number1 != number2: print(number1, "is not equal to", number2)

if number1 < number2: print(number1, "is less than", number2)

if number1 <= number2: print(number1, "is less than or equal to", number2)

if number1 > number2: print(number1, "is greater than", number2)

if number1 >= number2: print(number1, "is greater than or equal to", number2)

"""
"""
# Find the minimum of three values

number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))
number3 = int(input("Enter third number:"))

print("The smallest number of the set is:",min(number1, number2, number3))

"""
"""
# Open Webpage
import webbrowser

url_google = ("https://google.com")

def show_goog():
    webbrowser.open_new(url_google)

show_goog()

"""
# Part 1 - Domain is bowling

import math

game1 = (float(input("Enter first game total score: ")))
game2 = (float(input("Enter second game total score: ")))
game3 = (float(input("Enter third game total score: ")))
curavg = (float(input("Enter your current per game average: ")))

total = (game1, game2, game3)

sum = sum(total)
avg = (sum / 3)
product = (game1 * game2 * game3)
product_alt = (math.prod(total))
smallest = (min(game1, game2, game3))
largest = (max(game1, game2, game3))

print("The sum of the three games is:", sum)
print("The average of the three games is:", round(avg,2))
print("The product of the three games is:", product)
#print(product_alt)
print("The smallest of the three games is:", smallest)
print("The largest of the three games is:", largest)
print("The range of the three games is:", smallest, '-', largest)

if game1 > curavg:
    print("Your first game was above your average of", curavg)
if game1 < curavg:
    print("Your first game was below your average of", curavg)
if game1 == curavg:
    print("Your first game was equal to your average of", curavg)

if game2 > curavg:
    print("Your second game was above your average of", curavg)
if game2 < curavg:
    print("Your second game was below your average of", curavg)
if game2 == curavg:
    print("Your second game was equal to your average of", curavg)

if game3 > curavg:
    print("Your third game was above your average of", curavg)
if game3 < curavg:
    print("Your third game was below your average of", curavg)
if game3 == curavg:
    print("Your third game was equal to your average of", curavg)
