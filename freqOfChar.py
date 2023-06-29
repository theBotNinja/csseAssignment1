st = input("Enter Your String : ")
print ("Your string is : ",st)
freq_lis = {}

for char in st:
	if char in freq_lis:
		freq_lis[char] += 1
	else:
		freq_lis[char] = 1

max_freq = 0
for i in list(freq_lis.values()):
    if max_freq<i or max_freq == 0:
        max_freq = i

for i in list(freq_lis.keys()):
    if freq_lis[i] == max_freq:
        print(f"{i} has max freq of {max_freq}")
