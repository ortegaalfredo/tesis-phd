import math

b1=2.0
b0=10.0
n=128.0
M=4095.0


for K in range(1,25):
	P1=b1/(b1+b0)
	Pnc1=1
	P0=b0/(b1+b0)
	Pnc0=math.pow((1.0-(b1/((b1+b0)*M))),(n*K*b1))
	print Pnc0
	Pnc=P1*Pnc1+P0*Pnc0
	print "K: %d  Pn: %f" % (K,Pnc)
