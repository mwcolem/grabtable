from urllib.request import urlopen

def get_data(etf):
	print(etf)
	url = 'http://chart.finance.yahoo.com/table.csv?s='+ etf +'&a=5&b=15&c=2001&d=3&e=15&f=2017&g=d&ignore=.csv' 

	print(url)
	data = urlopen(url)
	
	with open(etf + '.csv', 'wb') as output:
	        output.write(data.read())

	output.close()

with open('etfs.txt', 'r') as etfs:
	for line in etfs:
		get_data(line.rstrip('\n'))	

etfs.close()
