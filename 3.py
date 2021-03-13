percent_list = ['procentov', 'protsent']
for i in range(2, 21):
    if i < 5:
        percent_list.append('protsenta')
    else:
        percent_list.append('protsentov')

while True:
    ans = input('Enter number 0-20 ("x" for exit): ')
    if ans.isdigit() and int(ans) < 21:
        print(ans, percent_list[int(ans)])
        continue
    elif ans == 'x':
        break
    print('You entered wrong value. Try again!')

for i in range(21):
    print(i, percent_list[i])