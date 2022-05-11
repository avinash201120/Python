def encode(s, k):
	newS = ""
	for i in range(len(s)):
		val = ord(s[i])
		dup = k
	if val + k>122:
			k -= (122-val)
			k = k % 26
			newS += chr(96 + k)
			
	else:
		newS += chr(val + k)
		k = dup
	
	
	print (newS)	
str = input("")
k = int(input())

encode(str, k)
