'ex1'
# #'a program that asks the user to enter a number, checks and prints whether the number is even or odd'
# num = int(input("Please enter the number:  "))
# if num % 2 == 0:
#     print("The number is even!")
# else:
#     print("The number is odd!")

'ex2'
##'a program that asks the user to enter a character, checks and prints whether the character is a consonant or a vowel'
# character = input("Please enter the character:  ")
# vowels = ['a', 'e', 'i', 'o', 'u', 'y']
# if character in vowels:
#     print("The char is vowel!")
# else:
#     print("The char is consonant!")

'ex3'
##'a program that asks the user to enter n number and prints the n-th Fibonacci number'
# def Fib(n):
#
#     if n <= 0:
#         return "The number must be positive!"
#     elif n == 1:
#         return 0
#     elif n == 2 or n == 3:
#         return 1
#     else:
#         return Fib(n-1) + Fib(n - 2)
#
# num = int(input("Please enter the number:  "))
# print(Fib(num))

'ex4'
##'a program that asks the user to enter a number and prints the sum of its digits on the screen'
# num = int(input("Please enter the number:  "))
# sum = 0
# while (num != 0):
#
#     sum += num % 10
#     num = num // 10
#
# print(sum)

'ex5'
##'a program that prints the following image on the screen. Use cycles'
# n = 5
# for i in range(n):
#     if i in range(1, 4):
#         for j in range(0,n,4):
#                 print('*', end='   ')
#     else:
#         for j in range(n):
#             print('*', end='')
#     print('')