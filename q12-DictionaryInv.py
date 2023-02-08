dic = {}
while True:
    key=input('Enter the key: ')
    value=input('Enter the value: ')
    dic[key] = value
    if input('Enter 0 to exit: ') == '0':
        break
    print()

print(f'\nEntered Dictionary: {dic}')
keys , values = list(dic.keys()) , list(dic.values())

for x in values:
    if values.count(x) > 1:
        print(f'Repeated Value: {x}')
        exit()

dic.clear()
for (x,y) in zip(keys,values):
    dic[y] = x
print(f'Inverted Dictionary: {dic}')
