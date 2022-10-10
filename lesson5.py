"ex1"
# user = int(input('enter hour : '))
# day = input('enter am (1) or pm (2) : ')
# hour = int(input('How many hours ahead ?: '))
# hour += user
#
# if hour >= 1 and hour <= 12 and day == '1':
#     print(f'New hour : {hour} am')
#
# elif hour > 12 and hour <= 24 and day == '1':
#     hour = hour - 12
#     print(f'New hour : {hour} pm')
#
# elif hour >= 12 and hour <= 24 and day == '2':
#     hour = hour - 12
#     print(f'New hour : {hour} pm')
# elif hour > 24:
#     print('cant convert that time')


"ex2"
# import random
# score = 0
# di = {'Ո՞ր կրոնական փիլիսոփայության ուղղություններից է Դզեն ուսմունքը: 1.ՀԻնդուիզմ 2.Բուդդիզմ 3.Հուդաիզմ': 2,
#       '1932թ. ո՞ր քաղաքում է առաջին անգամ անցկացվել առաջին միջազգային կինոփառատոնը: 1.Բեռլին 2.Մոսկվա 3.Վենետիկ': 3,
#       'Ո՞վ է առաջինը Նոբելյան մրցանակ ստացել գրականության ասպարեզում: 1.դրամատուրգ 2.վիպասան 3.պոետ': 3,
#       'Ո՞ր քիմիական տարրն է անվանվել ի պատիվ ստորգետնյա չար թզուկի: 1.Կոբալտ 2.Տելուր 3.Բերիլիում': 1,
#       'Քանի՞ ծով է ողողում Բալկանյան թերակղզին։ 1.4 2.3 3.6': 3,
#       'Հին Հունաստանի բնակչուհին Օլիմպիական խաղերի ո՞ր կարգում կարող էր հաղթել: 1.վազք 2.Կառքերի մրցավազք 3.լող':2,
#       'Բացի թվային ինդեքսից, ինչպիսի՞ անվանում ունի Android օպերացիոն համակարգի յուրաքանչյուր տարբերակը: 1.քաղցր 2.ծովային 3.գարնանային': 1,
#       'Ո՞ր կղզին է անվանվել ի պատիվ հայտնի հոլանդացի ծովագնացի: 1.Մադագասկար 2.Սումատրա 3.Թասմանիա': 3,
#       'Որտեղի՞ց է գալիս ֆուժեր անվանումը:1.քաղաք 2.բույս 3.ապակեգործի անուն': 1,
#       'Ինչպե՞ս են կոչվում իշամեղուները, որոնք բույն չեն կառուցում և նեկտար չեն հավաքում.1.Ծույլ իշամեղու 2.Կկու իշամեղուներ 3.Բզզան իշամեղու': 2}
# for i in range(4):
#       question = random.choice(list(di.keys()))
#       print(question)
#       answer = int(input("Պատասխան(1,2, կամ 3): "))
#       if answer == di[question]:
#             score += 1
# print(f'Դուք հավաքել եք {score}/4 միավոր')

"ex3"
# mat = [[0, 'M', 0, 'M', 0],
#        [0, 0, 'M', 0, 0],
#        [0, 0, 0, 0, 0],
#        ['M', 'M', 0, 0, 0],
#        [0, 0, 0, 'M', 0]]
# count = 0
# for i in range(len(mat)):
#        for j in range(len(mat)):
#               if mat[i][j] != 'M':
#                      if mat[i][j-1] == 'M' and j - 1 >= 0:
#                             count += 1
#                      if j + 1 != len(mat) and mat[i][j+1] == 'M':
#                             count += 1
#                      if mat[i-1][j] == 'M' and i - 1 >= 0:
#                             count += 1
#                      if i + 1 != len(mat) and mat[i+1][j] == 'M':
#                             count += 1
#                      if mat[i-1][j-1] == 'M' and i - 1 >= 0 and j - 1 >= 0:
#                             count += 1
#                      if j + 1 != len(mat) and i + 1 != len(mat) and mat[i+1][j+1] == 'M':
#                             count += 1
#                      if j + 1 != len(mat) and mat[i-1][j+1] == 'M' and (i - 1 >= 0):
#                             count += 1
#                      if i + 1 != len(mat) and mat[i+1][j-1] == 'M' and (j - 1 >= 0):
#                             count += 1
#                      mat[i][j] = count
#                      count = 0
#               else:
#                      mat[i][j] = 'M'
# print(mat)

"ex4"
# mat = [[1, 2, 3, 4],
#        [5, 6, 7, 8],
#        [9, 10, 11, 12],
#        [13, 14, 15, 16]]
#
# n = len(mat)
#
# for i in range(n // 2):
#        for j in range(n):
#               tmp = mat[i][j]
#               mat[i][j] = mat[n - i - 1][n - j - 1]
#               mat[n - i - 1][n - j - 1] = tmp
#
# if n % 2 == 1:
#        for j in range(n // 2):
#               tmp = mat[n // 2][j]
#               mat[n // 2][j] = mat[n // 2][n - j - 1]
#               mat[n // 2][n - j - 1] = tmp
#
# print(mat)