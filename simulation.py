import random

population=[0,1] # 0=heads and 1=tails
pattern1=[0,0,1] # HHT
pattern2=[0,1,1] # HTT
trials=100000
p1wins=0 # start both win counters at 0
p2wins=0
p1length=[] # start both length counters at 0
p2length=[]

for x in range(0,trials):
	fliplist=[] # current 3 flips - resets every time we start over
	i=0 # reset the counter
	while fliplist != pattern1 and fliplist!=pattern2:
		flip=random.choice(population) # flip the coin
		i=i+1 # add 1 to the counter
		fliplist.append(flip) # write down your flip
		fliplist=fliplist[-3:] # only look at the last 3 flips
	if fliplist==pattern1: # If pattern 1 wins
		p1wins=p1wins+1 # add a win to pattern 1
		p1length.append(i) # write down how many flips it took
	if fliplist==pattern2: # If pattern 2 wins
		p2wins=p2wins+1 # add a win to pattern 2
		p2length.append(i) # write down how many flips it took

average1=float(sum(p1length))/len(p1length) if len(p1length)>0 else float('nan')
average2=float(sum(p2length))/len(p2length) if len(p2length)>0 else float('nan')


print'The probability of Pattern 1 showing up first is:', float(100*p1wins)/trials,'%'
print 'Average flips until we see Pattern 1 is:', average1
print ' '
print 'The probability of Pattern 2 showing up first is:',float(100*p2wins)/trials,'%'
print 'Average flips until we see Pattern 2 is:', average2
