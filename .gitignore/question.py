print('Программа "Загадка"\n Вам будет загадано 10 загадок \n После каждого ответа Вам будет сообщено правильно ли вы ответили или нет \n В конце, программа выдас Вам общую статистику Ваших ответов')

name = input('Как вас зовут? ...')
rigth = []
wrong = []
print('Здравствуйте ' + name + ' мы начинаем ...')

q1 = ('','Question1  ...', 'Question2  ...', 'Question3  ...', 'Question4  ...', 'Question5  ...', 'Question6  ...', 'Question7  ...', 'Question8  ...', 'Question9  ...', 'Question10  ...')
a1 = ('','Answer1', 'Answer2', 'Answer3', 'Answer4' , 'Answer5', 'Answer6', 'Answer7', 'Answer8', 'Answer9', 'Answer10')


for a in range(1,11):
    answer = input(q1[a])
    if (a1[a].lower() == answer.lower()):
        print('Вы ответили верно...')
        rigth.append(1)
    else:
        print('Вы ответили не верно ... :( ')
        wrong.append(1)

print('Количество правильных ответов:', rigth.count(1))
print('Количество НЕ правильных ответов:', wrong.count(1))

if rigth.count(1) <= 5:
    print('Все очень плохо  ' + name + '.... :(')
else:
    print('Вы молодец  ' + name + '!!!')

