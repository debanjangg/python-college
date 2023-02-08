n=int(input("Enter no of elements: "))
lst,s=[],' '

for x in range(n):
    lst.append(input(f'Enter element {x+1}: '))

print(f'The List: {lst}')
print(f'The List as a String: {s.join(ele for ele in lst)}')