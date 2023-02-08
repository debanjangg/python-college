st = input('Enter a long string with no punctuations: ')
print(f'\nEntered string: {st}')
allWords , wordFreq = st.split() , {}

for x in allWords:
    if x.casefold() in wordFreq:
        wordFreq[x] += 1
    else:
        wordFreq[x.casefold()] = 1

print('Frequency of all words in the string:')
for x in wordFreq:
    print(f'{x} : {wordFreq[x]}')
