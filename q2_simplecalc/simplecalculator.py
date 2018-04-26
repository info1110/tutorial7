

def add(a, b):
	pass
	
def sub(a, b):
	pass
	
def mul(a, b):
	pass
	
def div(a, b):
	pass

#Left shift a << b	
def lsh(a, b):
	pass

#Right shift a << b	
def rsh(a, b):
	pass
	
def mod(a, b):
	pass
	
#Try and write this operating without using the abs() function or math library.
def abs(a):
	pass
	
#This will run until q is entered
line = input()
while line != 'q':
	spl = line.split()
	if len(spl) >= 3:
		if spl[0] == 'add':
			add(int(spl[1]), int(spl[2]))
		if spl[0] == 'sub':
			sub(int(spl[1]), int(spl[2]))
		if spl[0] == 'mul':
			mul(int(spl[1]), int(spl[2]))
		if spl[0] == 'div':
			div(int(spl[1]), int(spl[2]))
		if spl[0] == 'lsh':
			lsh(int(spl[1]), int(spl[2]))
		if spl[0] == 'rsh':
			rsh(int(spl[1]), int(spl[2]))
		if spl[0] == 'mod':
			mod(int(spl[1]), int(spl[2]))
	if len(spl) >= 2:
		if spl[0] == 'abs':
			abs(int(spl[1]))
		line = input()
	else:
		print("Not valid operation")
