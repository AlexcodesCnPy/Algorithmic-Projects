

l = [2,1,4,5,6,7,9,8]

print(l)

for i in range(1,len(l)):
	if l[i] < l[i-1]:
		temp = l[i]
		l[i] = l[i-1]
		l[i-1] = temp




print(l)
