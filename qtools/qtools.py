import math

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
