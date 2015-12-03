import math

b1=4.0
b0=4.0
n=8.0
M=256.0


for K in range(1,30):
	print K,
	for b1 in range(2,5):
		P1=b1/(b1+b0)
		Pnc1=1
		P0=b0/(b1+b0)
		Pnc0=math.pow((1.0-(1.0/M)),(n*K*b1))
		Pnc0=math.pow(1.0-Pnc0,K)
		print Pnc0,
		Pnc=P1*Pnc1+P0*Pnc0
	print

	#print "K: %d  Pn: %f" % (K,Pnc)
