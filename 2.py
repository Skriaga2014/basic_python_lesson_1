#list_ = [i**3 for i in range(1000) if i % 2 == 1]
list_ = []
for i in range(1000):
    if i % 2 == 1:
        list_.append(i**3)

print(list_)

# a)
#sum_ = sum([i for i in list_ if sum([int(a) for a in str(i)]) % 7 == 0])
sum_ = 0
for item in list_:
    item_sum = 0
    for sign in str(item):
        item_sum += int(sign)
    if item_sum % 7 == 0:
        sum_ += item

print(sum_)

# b)
#sum_2 = sum([i + 17 for i in list_ if sum([int(a) for a in str(i + 17)]) % 7 == 0])

sum_2 = 0
for item in list_:
    item_sum = 0
    for sign in str(item + 17):
        item_sum += int(sign)
    if item_sum % 7 == 0:
        sum_2 += item + 17
print(sum_2)



