import pandas as pd
data = pd.read_csv ('titanic.csv', index_col = 'PassengerId')
x = int(input('Kakoe kolichestvo muzhchin i zhenshin sootvetstvenno plyli na titanice?'))
if x != 891:
    print ('Nevernoe kolichestvo')
else:
    male = 0
    female = 0
    for i in range(1, x+1):
        if str(data['Sex'][i]) == 'male':
            male = male + 1
        else:
            female = female + 1
    print (male, 'muzhchin i ', female, 'zhenshin')
    survived = 0
    dead = 0
    for i in range (1, x+1):
        if str(data['Survived'][i]) == '1':
            survived = survived + 1
        else:
            dead = dead + 1
    Dolya = survived/(dead+survived) * 100
    print ('Survived: ', survived, 'and', 'Dead ', dead,', Percentage of survived:', Dolya)
    first = 0
    for i in range (1, x+1):
        if str(data['Pclass'][i]) == '1':
            first = first + 1
            prs = first/x * 100
    print ('Ludei pervogo klassa:', first,'Eto', prs)
    
        