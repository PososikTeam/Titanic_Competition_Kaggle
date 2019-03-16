import numpy as np


from learning_algorithms.network import Network
from pandas import read_csv, DataFrame, Series


data = read_csv('train.csv')

#data.pivot_table('PassengerId', 'Pclass', 'Survived', 'count').plot(kind='bar', stacked=True)


data.drop('Cabin', 1, inplace = True)
data.drop('Ticket', 1, inplace = True)
data.drop('Name', 1, inplace = True)
sex = list()
#print(data['Sex'])

for i in range(len(data['Sex'])):
    if(data['Sex'][i]=='male'):
        data['Sex'][i] = 1
    else:
        data['Sex'][i] = 0
    if data['Embarked'][i] == 'C':
        data['Embarked'][i] = 3
    elif data['Embarked'][i] == 'S':
        data['Embarked'][i] = 2
    elif data['Embarked'][i] == 'D':
        data['Embarked'][i] = 1
    else:
        data['Embarked'][i] = 2

print(data['Age'].mean())
