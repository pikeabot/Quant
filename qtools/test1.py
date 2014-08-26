import os
import math
import numpy 
from numpy.fft import fft, fftfreq
from qtools import *
from quandlio import *
from models import stock
from flask import jsonify
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
   	d = jsonify(high=145.3, low=144.01)
	print d
if __name__=='__main__':
		main()
