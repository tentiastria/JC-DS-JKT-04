def tickets(peopleInLine):
    list = []
    money = {}
    idx = [25,50,100]
    
    for i in idx:
        if i not in money.keys():
            money[i] = 0   

    for j in peopleInLine:
        if j == 25:
            money[25] += 1
            list.append(j)
        elif j == 50 and money[25] > 0:
            money[25] -= 1
            money[50] += 1
            list.append(j)
        elif j == 50 and money[25] == 0:
            print('NO')
            break
        elif j == 100 and money[50] >= 1 and money[25] >= 1:
            money[100] += 1
            money[50] -= 1
            money[25] -= 1
            list.append(j)      
        elif j == 100 and money[25] >= 3:
            money[100] += 1
            money[25] -= 3
            list.append(j)
        else:
            print('NO')
            break            
    if len(list) == len(peopleInLine):
        print('YES')

peopleInLine = [25, 25, 25, 100, 25, 50]   
               
tickets(peopleInLine)   

