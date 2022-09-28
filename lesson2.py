'ex1'
'Write a program that asks the user for a weight in kilograms and converts it to pounds. There are 2.2 pounds in a kilogram.'
# weight_kg = float(input('Enter the weight please: '))
# pounds = weight_kg * 2.2
# print("The weight is ", pounds, 'pounds')


'ex2'
'Write a program that generates and prints 50 random integers, each between 3 and 6.'
# import random
# for i in range(50):
#     print(random.randint(3, 6))


'ex3'
'Write a program that asks the user to enter two numbers, x and y , and computes | x − y | /  x+y'
# x = int(input("Input the first number please: "))
# y = int(input("Input the second number please: "))
# if x != abs(y):
#     res = abs(x - y) / (x + y)
#     print(res)
# else:
#     print("error!!! division by zero -> x+y = 0 ")

'ex4'
'A year is a leap year if it is divisible by 4, except that years divisible by 100 are not'\
' leap years unless they are also divisible by 400. Ask the user to enter a year, and, ' \
'using the // operator, determine how many leap years there have been between 1600 and that year.' \

# def count_of_years(year):
#         return (year // 4) - (year // 100) + (year // 400)
#
# def count_of_range(year):
#     s = count_of_years(1600)
#     e = count_of_years(year)
#     return e - s
# year = int(input("Enter the year please: "))
# print(count_of_range(year))

'ex5'
'A number is called a perfect number if it is equal to the sum of all of its divisors, not including the number itself'

# for i in range(2, 10001):
#     sum_of_div = 1
#     for j in range(2, i):
#         if i % j == 0 and j != i:
#             sum_of_div += j
#     if sum_of_div == i:
#         print(i)

