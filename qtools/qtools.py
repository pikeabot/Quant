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
def rsi(buffer):
	blen = len(buffer)

	up=0.0
	down=0.0

	for i in range(1, blen-1):
		#print buffer[i]
		if buffer[i]>buffer[i-1]:
			up=up+buffer[i]
		elif buffer[i]<buffer[i-1]:
			down=down+buffer[i]

	return 100.00-(100.0/(1.0+(up/down)))

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
def macd_signal_line(stock_data, macd_data):
	#for initial value use sma
	prev_ema9 = get_avg(macd_data[0:9])

	for i in range (9, len(macd_data)):
		buffer_9day[i-9] = macd_data[i-9:i]
		ema9[i-9] = ema(stock_data[i].close, prev_ema9, 9)

		prev_ema9 = ema9
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
def vma(buffer):

	get_avg(buffer)





