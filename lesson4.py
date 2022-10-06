"ex1"
"English-Armenian dictionary"
# di = {}
# with open("dictionary.txt", encoding='utf-8') as f:
#     for line in f:
#
#         line = line.split(' - ')
#         di[line[0]] = line[1]
#         print(line)
# print(di)

"ex2"
"n this task I have data with names of people and their ages․I submitted it in dictionary,then I singled the names of thoses people,who is palindrom," \
"and there I added the names of the people whose age was older than 45"
# di = {}
# with open("data.txt", encoding='utf-8') as f:
#     for line in f:
#             line = line.split(' - ')
#             di[line[0]] = line[1]
#
# palindrom_name_lst = []
# for name in di.keys():
#     name = name.split(' ')
#     if name[0].lower() == name[0][::-1].lower():
#         palindrom_name_lst.append(name[0])
#
# tp = ("")
# for name, age in di.items():
#     if int(age) > 45:
#         tp = tp + name + '\n'
#
# print(f'The data names and their age is:\n {di}')
# print(f'The palindrom names is:  {palindrom_name_lst}')
# print(f'The names whose age is > 45 are:\n{tp}')
#

"ex3"
# import dis
#
# def myfunc(alist):
#     return len(alist)
#
# dis.dis(myfunc)


