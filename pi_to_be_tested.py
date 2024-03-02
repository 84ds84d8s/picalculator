#uses the BBP formula instead, please check if it is faster
print("pi generator v1.0.1 beta")
print("may take quite a few minutes")
print("input digits of pi required")
y=int(input())
print("here we go")
print("Generating. Please wait patiently.")
from decimal import *
getcontext().prec = y
x = Decimal(1)
sum = Decimal(0)
u = 10
t=Decimal(0)
while True:
	  sum = sum+ (1/16**t)*((4/(8*t+1))-(2/(8*t+4))-(1/(8*t+5))-(1/(8*t+6)))
	  t+=1
	  if u == sum:
	  	with open('pi.txt', 'w') as f:
	  		print(Decimal(sum))
	  		f.write(str(Decimal(sum)))
	  	print("Press anything to exit. You can find your value of pi in pi.txt. Note the final few digits aren't guaranteed to be correct.")
	  	input()
	  	break
	  u = su 
