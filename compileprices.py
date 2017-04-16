import pandas;

def get_data(df, etf):
	df[etf] = pandas.read_csv(etf+'.csv', usecols=['Close'])

df = pandas.read_csv("BIV.csv", usecols=['Date'])

with open('etfs.txt', 'r') as etfs:	
	for line in etfs:
		get_data(df, line.rstrip('\n'))

df.to_csv('etfPriceData.csv')
