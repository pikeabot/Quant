import os
import math
import numpy 
from numpy.fft import fft, fftfreq
from qtools import *
from quandlio import *
from models import stock

BUFF_LEN=5



'''
calculate 'acceleration' of a stock price
assume buffer has a length of 3
assume time step of 1 day
'''
def acceleration(buffer):

	v1=buffer[1]-buffer[0]
	v2=buffer[2]-buffer[1]

	return v2-v1


def main():

   	#twtr_data = get_stock_data('/home/grandoverlord/quant/Stocks/GOOG-NYSE_TWTR.csv')
   	#cnat_data = get_stock_data('/home/grandoverlord/quant/Stocks/GOOG-NASDAQ_CNAT.csv')
   	tsl_data = get_stock_data1('/home/grandoverlord/quant/Stocks/GOOG-NYSE_TSL.csv')

   	sigma = 0
	for i in range(3, 178):

		
		#twtr_buffer=twtr_data.close[i-3:i]
		#cnat_buffer = cnat_data.close[i-5:i]
		tsl_buffer = tsl_data.close[i-3:i]

		acc=acceleration(tsl_buffer)
		#print fft(twtr_buffer)
		m = least_squares(tsl_buffer)
		if i>8:
			sigma = standard_dev(tsl_data.close[i-8:i])
			
		g=fft(tsl_data.close[i-1:i])
		gi=abs(g[0])-get_avg(tsl_buffer)

		'''
		print tsl_data.date[i]+ " " + str(m) +" "+ str(acc) + " "+str(gi)\
				+" " + str(sigma)
		'''
		'''
		buy low sell high
		find buy signals
		'''
		#buy
		#if m<0 and acc <0 and gi < 0 and sigma>.7:
		#	print tsl_data.date[i]

		#sell
		if m>0 and acc <0 and sigma>.7:
			print tsl_data.date[i]
	'''		
	emalist=[]
	sma=get_avg(twtr_data.close[0:19])
	emalist.append(sma)
	curr_ema=ema(twtr_data.close[20],  sma, 20)
	print curr_ema
	emalist.append(curr_ema)

	for i in range(21, 35):
		curr_ema=ema(twtr_data.close[i], emalist[-1], 20)
		print twtr_data.date[i]+ " " + str(curr_ema)
		emalist.append(curr_ema)
	'''
if __name__=='__main__':
		main()
