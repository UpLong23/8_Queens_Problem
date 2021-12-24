import numpy as np 
import itertools
import time

start_time = time.time()

r1 = [1,0,0,0,0,0,0,0]
r2 = [0,1,0,0,0,0,0,0]
r3 = [0,0,1,0,0,0,0,0]
r4 = [0,0,0,1,0,0,0,0]
r5 = [0,0,0,0,1,0,0,0]
r6 = [0,0,0,0,0,1,0,0]
r7 = [0,0,0,0,0,0,1,0]
r8 = [0,0,0,0,0,0,0,1]

A = [r1,r2,r3,r4,r5,r6,r7,r8]
B = list(itertools.permutations(A))
f = 0
for m in B:
	matr = np.array(list(m))
	for i in range(len(matr)):
		j = matr[i].tolist().index(1) 
		for k in range(1,8):
			a = True
			if (i-k >= 0 and j-k >= 0) and (matr[i-k,j-k] == 1):
				a = False
				break
			if (i+k <= 7 and j+k <= 7) and (matr[i+k,j+k] == 1):
				a = False
				break
			if (i+k <= 7 and j-k >= 0) and (matr[i+k,j-k] == 1):
				a = False
				break
			if (i-k >= 0 and j+k <= 7) and (matr[i-k,j+k] == 1):
				a = False
				break
		if a == False:
			break
	if a == True:
		f +=1
		print(matr)
		
print("--- %s seconds ---" % (time.time() - start_time))
print(f)
