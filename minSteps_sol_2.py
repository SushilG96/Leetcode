dictn = {}

for i in s:
	if i in dictn:
		dictn[i] += 1
	else:
		dictn[i] = 1

count = 0
for i in t:
	if i not in dictn:
		count += 1
	else:
		if dictn[i] == 0:
			count += 1
		else:
			dictn[i] -= 1

return count
