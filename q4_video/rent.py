quit = False

def load_dvds(filename):
	""" Load the dvds from a file """
	dvds = []
	with open(filename, 'r') as f:
		for l in f:
			spl = l.split(',')
			if len(spl) > 1:
				dvds.append([spl[0], int(spl[1])])
	return dvds

def show_dvds(dvds):
	""" This will show all the dvds """
	for i, d in enumerate(dvds):
		print("[{0}] {1}".format(i, d[0])) 

def select_dvd(dvds):
	""" Will allow the user to select a dvd """
	global quit
	
	idx = input("Select a dvd or press q to quit: ")
	item = None
	if idx == 'q':
		quit = True
	else:
		idx = int(idx)
		item = dvds[idx] # We are not checking the index
	return item 

def pay_for_dvd(dvd):
	""" Pay for the DVD, ask for input check if it is over $3.00 """
	p = float(input("Please pay to rent this item: "))
	print(dvd)
	if p >= 3.00:
		dvd[1] = dvd[1] - 1 #We drop the quantity by 1, if 0 should not be rentable
	


#Ignore this bit!
if __name__ == '__main__':
	while not quit:
		dvds = load_dvds('titles.dvds')
		show_dvds(dvds)
		d = select_dvd(dvds)
		if not quit:
			pay_for_dvd(d)
	
