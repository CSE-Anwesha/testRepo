s= "hello"
max = 0
for x in s :
	x = ord(x)
	print(x)
	if(x > max):
		max = x
	else:
		continue
print(max)
