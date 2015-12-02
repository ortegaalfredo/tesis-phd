import random

origframe=[]

#Cantidad slots
M=2

#Cantidad clientes
n=2

#init slot
for i in range(M):
	origframe.append(0)


tries=1000000
nc=0
client=random.randint(0,M-1) 

for q in xrange(tries):
	fr=list(origframe)
	for i in range(n):
		fr[random.randint(0,M-1)]+=1
	if (fr[client]==0): nc+=1

print "Prob. no colision=%f" % (float(nc)/float(tries))

