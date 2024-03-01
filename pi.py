print("pi generator v0.0.0")
print("may take quite a few minutes")
print("input digits of pi required")
y=int(input())
print("here we go")
print("Generating. Please wait patiently.")
from decimal import *
getcontext().prec = y
x = Decimal(1)
sum = 0
u = 10
t = 0
while True:
	  sum = sum+ 1/(x*2*abs(x)) +1/(x*3*abs(x))
	  if x > 0:
	  	x = -(x+2)
	  else:
	  	x = -(x-2)
	  t += 1
	  if u == sum:
	  	with open('pi.txt', 'w') as f:
	  		print(Decimal(4*sum))
	  		f.write(str(Decimal(4*sum)))
	  	print("Press anything to exit. You can find your value of pi in pi.txt. Note the final few digits aren't guaranteed to be correct.")
	  	input()
	  	break
	  u = sum
