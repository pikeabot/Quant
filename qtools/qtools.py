import math

'''
{ "_id" : ObjectId("53f2e5fc1d41c817974c0896"), 
"High" : 145.3, 
"Adj Close" : 144.09, 
"symbol" : "MMM", 
"Volume" : 1390200, 
"Low" : 144.01, 
"Date" : ISODate("2014-06-23T00:00:00Z"), 
"Close" : 144.09, 
"Open" : 145.1 }
'''

def least_squares(buffer):
	blen = len(buffer)

	#sum x, sumy, sumxy
	sumx=0
	sumy=0
	sumxy=0
	sumxsqrd=0
	for x in range(0, blen):
		sumx=sumx+x
		sumy=sumy+buffer[x]
		sumxy = sumxy+x*buffer[x]
		sumxsqrd=sumxsqrd+x**2

	try:
		m=(sumxy - (sumx*sumy)/blen)/(sumxsqrd-(sumx**2)/blen)
	except:
		m=.001
	return m

'''
calculate a simple moving average for the number of days equivalent to the length
of the input buffer
'''
def get_avg(buffer):
	blen = len(buffer)

	sumx=0
	for x in range(0, blen):
		sumx=sumx+buffer[x]

	return sumx/float(blen)

def standard_dev(buffer):

	blen=len(buffer)

	avg=get_avg(buffer)
	sumxusqrd=0
	for x in range(0, blen):
		sumxusqrd = sumxusqrd+(buffer[x]-avg)**2
	
	try:
		sigma = math.sqrt(1.0/(float(blen)-1.0)*sumxusqrd)
	except:
		sigma=.001
	return sigma

'''
calculate Relative Strength Index
TODO: need to add smoothing
'''
def rsi(stock_data, period):
	#blen = len(buffer)
	buffer=[]
	rsi_data=[]
	up=0.0
	down=0.0
	
	for i in range(period, len(stock_data)):
		for j in range(i-period, i):
			buffer.append(stock_data[j]['close'])
			
		for k in range(1, period):
			
			if buffer[k]>buffer[k-1]:
				up=up+buffer[k]
				
			elif buffer[k]<buffer[k-1]:
				down=down+buffer[k]

		if down==0:
			ud = 0
		else:
			ud=up/down
		rsi_data.append(100.00-(100.0/(1.0+ud)))

		buffer=[]
		up=0.0
		down=0.0

	return rsi_data


''' 
calculate exponential moving average
TODO: add smoothing
'''
def ema(curr_price, prev_ema, time_period):

	return (curr_price-prev_ema)*(2/(float(time_period)+1))+prev_ema

'''
uses get_stock_data1
'''
def macd_line(stock_data):
	b12=[]
	b26=[]
	macd=[]
	#for initial value use sma
	for i in range (14,26):
		b12.append(stock_data[i-14]['close'])

	for i in range (0, 26):
		b26.append(stock_data[i-26]['close'])

	prev_ema12 = get_avg(b12)
	prev_ema26 = get_avg(b26)

	for i in range (26, len(stock_data)):

		ema12 = ema(stock_data[i]['close'], prev_ema12, 12)
		ema26 = ema(stock_data[i]['close'], prev_ema26, 26)

		macd.append(ema12-ema26)

		prev_ema12 = ema12
		prev_ema26 = ema26
	
	return macd

'''
9 day ema of MACD macd_line
'''
def macd_signal_line(macd_data):

	ema9=[]
	#for initial value use sma
	prev_ema9 = get_avg(macd_data[0:9])

	for i in range (9, len(macd_data)):
		
		ema9.append(ema(macd_data[i], prev_ema9, 9))

		prev_ema9 = ema9[i-9]
	return ema9

def percent_k(buffer):

	buffer_len = len(buffer)

	return 100*(buffer[buffer_len-1]-min(buffer))/(max(buffer)-min(buffer))

	
def percent_d(k):
	
	return get_avg(k)

def kdj(buffer):
	pass

def Williams_perR():
	pass

def bias():
	pass

'''
volume moving average
'''
def vma(stock_data, period):
	buffer =[]
	vma_data = []

	for i in range(period, len(stock_data)):
		for j in range(i-period, i):
			buffer.append(stock_data[j]['close'])
			
		vma_data.append(get_avg(buffer))

	return vma_data
	





