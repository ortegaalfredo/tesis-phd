import random

#Calculo de Pnc=P(1)*Pnc(1)+P(0)*Pnc(0)

origframe=[]

#Cantidad slots
M=2

#Cantidad clientes
n=2

#inicia frame
for i in range(M):
	origframe.append(0)


tries=1000000
nc=0 #almacena si no colisiona



for q in xrange(tries):
	fr=list(origframe)
	#selecciona slot random (opcional)
	client=random.randint(0,M-1) 
	#Selecciona e inserta los datos:
	data=random.randint(0,1)
	fr[client]=data
	#Inserta valores de los n clientes en el frame
	for i in range(n):
		fr[random.randint(0,M-1)]|=random.randint(0,1)
	#Si lo datos se mantienen, aumenta contador de "no colision"
	if (fr[client]==data): nc+=1

print "Prob. no colision=%f" % (float(nc)/float(tries))

