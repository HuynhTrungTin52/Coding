str=input("Enter a string :")
letters=[]
for i in range(len(str)):
	if str[i] not in letters and str[i] !=" ":
		letters.append(str[i])
freq=[]
for i in letters:
    freq.append(str.count(i))
    
for i in range(len(letters)):
    print(freq[i],end="")
    print(letters[i],end="")