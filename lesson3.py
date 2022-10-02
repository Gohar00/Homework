"ex1"
"Write a program that allows the user to enter five numbers (read as strings). "
"Create a string that consists of the user’s numbers separated by plus signs. "

# s = ''
# numbers = input("Enter the numbers, please:  ")
# numbers = numbers.split(', ')
# for i in numbers:
#     s += i + '+'
# print(s[:len(s) - 1])

"ex2"
"Valid phone number"
# Phone_Num = input('Enter the phone number pleas: ')
# if len(Phone_Num) == 12 \
#     and Phone_Num[3] == '-' \
#     and Phone_Num[7] == '-' \
#     and Phone_Num[:3].isdigit() \
#     and Phone_Num[4:7].isdigit() \
#     and Phone_Num[9:].isdigit():
#     print('Valid')
# elif len(Phone_Num) == 14 \
#     and Phone_Num[0] == '1' \
#     and Phone_Num[1] == '-' \
#     and Phone_Num[5] == '-' \
#     and Phone_Num[9] == '-' \
#     and Phone_Num[2:4].isdigit() \
#     and Phone_Num[6:9].isdigit() \
#     and Phone_Num[10:].isdigit():
#     print('Valid')
# else:
#     print('Invalid')

"ex3"
"Use a list comprehension to produce a list that consists of all palindromic numbers between 100 and 1000."
# pal_num = []
# for i in range(100, 1001):
#     if str(i) == str(i)[::-1]:
#         pal_num.append(i)
# print(len(pal_num))

"ex4"
"Let L=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]. Use a list comprehension to produce a list of the gaps between consecutive entries in L." \
"Then find the maximum gap size and the percentage of gaps that have size 2."

# def gap_size(L):
#     gap_sizes = []
#     for i in range(len(L) - 1):
#         gap_sizes.append(L[i] - L[i - 1] - 1 )
#     return gap_sizes
#
# def max_size(lst):
#
#
#     max_size = max(lst)
#     return f'max gaps size is: {max_size}'
#
# def percentage(lst):
#
#     count = 0
#     for i in lst:
#         if i == 2:
#             count += 2
#     per = count / len(lst) * 100
#     return f'the percentage is {per}%'
# L = [2, 3, 5, 7, 11, 13, 17, 19, 22, 29, 32, 37, 41, 43, 47]
# lst_of_gap_size = gap_size(L)
# print(max_size(lst_of_gap_size))
# print(percentage(lst_of_gap_size))


"ex5"
"Write a program that repeatedly asks the user to enter product names and prices. " \
"Store all of these in a dictionary whose keys are the product names and whose values are the prices." \
" When the user is done entering products and prices, allow them to repeatedly enter" \
" a product name and print the corresponding price or a message if the product is not in the dictionary."

# di = {}
# add_product = 'yes'
# while add_product == 'yes':
#     name = input("Enter the name of product: ")
#     value = int(input("Enter the value of product: "))
#
#     di[name] = value
#
#     add_product = input("Would you like to add product? (yes/no)")
# else:
#     name = input("Enter your product's name please: ")
#     if name in di.keys():
#         print(f"the {name}'s value is {di[name]}")
#     else:
#         print('The product not in dictionary!')

"ex6"
"Write a program that reads through any dictionary like this and prints the following" \
"All the users whose phone number ends in an 8" \
"All the users that don’t have an email address listed"

# di = [{'name': 'Todd', 'phone': '555-1414', 'email': 'todd@mail.net'},
#       {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#       {'name': 'Princess', 'phone': '555-3141', 'email': ''},
#       {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@mail.net'}]
# us_names_for_phone = []
# us_names_for_email = []
# for i in di:
#     if i['phone'][-1] == '8':
#         us_names_for_phone.append(i['name'])
#     if i['email'] == '':
#         us_names_for_email.append(i['name'])
# print(f'The users whose phone number ends in an 8 -> {us_names_for_phone}')
# print(f'The users that don’t have an email address listed -> {us_names_for_email}')

"ex7"
"Create a 5 × 5 list of numbers. Then write a program that creates a dictionary whose " \
"keys are the numbers and whose values are the how many times the number occurs." \
" Then print the three most common numbers."

# from random import randint
# n = 5
# mat = [[randint(1, 10) for _ in range(n)] for i in range(n)]
#
# lst = []
# di = {}
# for i in mat:
#     for j in i:
#         lst.append(j)
# for el in lst:
#     di[el] = lst.count(el)
# print(f'the matrix is : {mat}')
# print(di)





