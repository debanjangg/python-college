str=input("Enter a string: ")
print ("Entered String: ",str)
vow = ['a','e','i','o','u']
vowCnt = conCnt = digCnt = specChar = 0
for x in str.lower():
    if x.isalpha():
        if x in vow:
            vowCnt += 1
        else:
            conCnt += 1
    elif x.isnumeric():
        digCnt += 1
    else:
        specChar += 1

print (f"No of Vowels: {vowCnt}")
print (f"No of Consonants: {conCnt}")
print (f"No of Digits: {digCnt}")
print (f"No of Special Characters: {specChar}")
