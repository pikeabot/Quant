import os
import math
from qtools import *
from candlestick import *
from quandlio import get_stock_data, get_stock_data1

BUFF_LEN=5

class stock:

	def __init__(self):
		self.money=10000.00
		self.stock_value = 0
		self.commission=9.99
		self.num_shares=0
		self.buy_price=0
		self.sell_price=0
		self.last_buy_date=''
		self.last_sell_date=''

	def get_money(self):
		return self.money

	def get_stock_value(self):
		return self.stock_value

	def get_num_shares(self):
		return self.num_shares

	def buy(self, curr_price, purchase_date):

		if self.money>curr_price:
			self.num_shares=int((self.money-self.commission)/curr_price);
			self.money=self.money-self.commission - self.num_shares*curr_price;
			self.buy_price=curr_price;
			self.last_buy_date=purchase_date;
			self.stock_value=self.num_shares*curr_price;

	def sell( self, curr_price, sell_date):

		self.money=self.money+self.num_shares*curr_price-self.commission;
		self.sell_price=curr_price;
		self.last_sell_date=sell_date;
		self.num_shares=0;
		self.stock_value=0;

	def update_stock_value( self, curr_price):

		self.stock_value=self.num_shares*curr_price;


def main():

   	twtr_data = get_stock_data1('/home/grandoverlord/quant/Stocks/GOOG-NYSE_TWTR.csv')
   	#twtr_data = get_stock_data('/home/grandoverlord/quant/Stocks/GOOG-NASDAQ_CNAT.csv')
   	#twtr_data = get_stock_data('/home/grandoverlord/quant/Stocks/GOOG-NYSE_TSL.csv')
   	#init stock for purchase
   	'''
   	twtr=stock()
   	curr_price=twtr_data.close[2]
	twtr.buy(curr_price, twtr_data.date[2])
	last_price=curr_price
	'''
	'''
	macdln=macd_line(twtr_data)

	macdsg= macd_signal_line( macdln)
	for i in range (0,len(macdsg)):
		print macdsg[i]
	'''
	'''
	simple trading algo
	assumes that stock is bought at the closing price and that the
	desired quantity was available at that price
	'''
	'''
	for i in range(5, 178):
		time_buffer=twtr_data.close[i-5:i]
		m=least_squares(time_buffer)
		sigma= standard_dev(time_buffer)

		# upward slope and hit a peak
		
		if m>.5 and sigma>.5 :
			twtr.buy(twtr_data.close[i], twtr_data.date[i])
		elif m<0 and sigma>.5:
			twtr.sell(twtr_data.close[i], twtr_data.date[i])
		print twtr_data.date[i]+ " " + str(m) + " "+ str(sigma) + " " +\
			str(twtr.get_money()+twtr.get_stock_value()) + " " + \
			str(twtr.get_num_shares())
		'''

	'''
	rsi_data=rsi(twtr_data, 10)
	
	for i in range(0, len(rsi_data)):
		print rsi_data[i]
	'''
	vma_data=vma(twtr_data, 10)
	
	for i in range(0, len(vma_data)):
		print vma_data[i]

	''''
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
	'''
	for i in range(0, 184):
		c = candlestick_daily(twtr_data.openp[i], twtr_data.close[i], twtr_data.high[i], twtr_data.low[i])

		print twtr_data.date[i] + " " + c
	'''
if __name__=='__main__':
		main()
