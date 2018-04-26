import rent

def test_load_dvds():
	dvds = rent.load_dvds('titles.dvds')
	example = [("Casablanca", 0),
				("Citizen Kane",2),
				("The Wizard Of Oz",1),
				("Star Wars",3),
				("Dr Strangelove",0),
				("Aladdin",2)]
	
	i = 0;
	while i < len(dvds):
		assert dvds[i][0] == example[i][0]
		assert dvds[i][1] == example[i][1]
		i += 1

def test_search_dvd_1():
	dvds = rent.load_dvds('titles.dvds')
	title = 'Dr Strangelove'
	i = 0;
	found = False
	while i < len(dvds):
		if dvds[i][0] == title:
			found = True
		i+= 1
			
	assert found == True
	
def test_search_dvd_2():
	dvds = rent.load_dvds('titles.dvds')
	title = 'Simpsons Movie'
	i = 0;
	found = False
	while i < len(dvds):
		if dvds[i][0] == title:
			found = True
		i += 1
			
	assert found == False
	

def test_select_dvd_1():
	dvds = rent.load_dvds('titles.dvds')
	d = dvds[0]
	assert d[0] == 'Casablanca'
	
#Add your test cases here	

test_load_dvds()
test_search_dvd_1()
test_search_dvd_2()
test_select_dvd_1()
# Once you have written your test case, add it here

print("All tests passed")
