percent_list = ['процентов', 'процент']
for i in range(2, 21):
    if i < 5:
        percent_list.append('процента')
    else:
        percent_list.append('процентов')

while True:
    ans = input('Введите число 0-20 ("x" чтобы выйти): ')
    if ans.isdigit() and int(ans) < 21:
        print(ans, percent_list[int(ans)])
        continue
    elif ans == 'x':
        break
    print('Введено неверное значение. Попробуйте снова!')

for i in range(21):
    print(i, percent_list[i])
