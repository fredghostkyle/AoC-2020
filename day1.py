f = open("\input.txt", "r")
y = f.read().split()

for i in range(0,len(y),1):
	for j in range(0, len(y),1): # Remove this loop and its references for part 1. 
		for k in range (i+1, len(y),1):
			temp = int(y[i]) + int(y[j])+ int(y[k])
			#print(str(y[i]) + " + " + str(y[j]) + " = " + str(temp))

			if  temp == 2020:
				print(str(y[i]) + " + " + str(y[j]) + " + " + str(y[k]) + " = " + str(temp))
				temp1 = int(y[i]) * int(y[j]) * int(y[k])
				print(str(y[i]) + " * " + str(y[j]) + " * " + str(y[k]) + " = " + str(temp1))
