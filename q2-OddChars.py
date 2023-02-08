st=input("Enter a String: ")
print("Entered string: ",st)
print("Characters in Odd numbered positions: ",end='')
for x in st[::2]:
    print(x+'  ',end='')
print()
