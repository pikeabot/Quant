import os
import math
from qtools import *
from quandlio import *

BUFF_LEN=5

class stock:

	def __init__(self):
		self.money=10000.00
		self.stock_value = 0
		self.commission=9.99
		self.num_shares=0
		self.name=''
		self.buy_price=0
		self.sell_price=0
		self.last_buy_date=''
		self.last_sell_date=''

	def get_money(self):
		return self.money

	def get_name(self):
		return self.name

	def get_stock_value(self):
		return self.stock_value

	def get_num_shares(self):
		return self.num_shares

	def buy(self, stockname, curr_price, purchase_date):

		if self.num_shares==0:
			self.name=stockname
			self.num_shares=int((self.money-self.commission)/curr_price);
			self.money=self.money-self.commission - self.num_shares*curr_price;
			self.buy_price=curr_price;
			self.last_buy_date=purchase_date;
			self.stock_value=self.num_shares*curr_price;

		#buy to cover
		else:
			self.name=''
			self.money=self.money+self.num_shares*curr_price-self.commission\
						-self.num_shares*self.buy_price;
			self.sell_price=curr_price;
			self.last_buy_date=purchase_date;
			self.num_shares=0;
			self.stock_value=0;

	def sell( self, stockname, curr_price, sell_date):

		if self.name == stockname:
			self.name=''
			self.money=self.money+self.num_shares*curr_price-self.commission;
			self.sell_price=curr_price;
			self.last_sell_date=sell_date;
			self.num_shares=0;
			self.stock_value=0;

		#sell short
		else: 
			self.name=stockname
			self.num_shares=-int((self.money-self.commission)/curr_price);
			self.money=self.money-self.commission - self.num_shares*curr_price;
			self.buy_price=curr_price;
			self.last_sell_date=sell_date;
			self.stock_value=self.num_shares*curr_price;

	def update_stock_value( self, curr_price):

		self.stock_value=self.num_shares*curr_price;

def buy_signal(stock_buffer):

		#stock_buffer=thestock.close[i-5:i]

		m=least_squares(stock_buffer)

		sigma= standard_dev(stock_buffer)

		#determine best candidate to buy
		# upward slope and hit a peak
		
		if m>2 and sigma>2 :
			#thestock.buy(thestock.close[i], thestock.date[i])
			return 'buy'
		elif m<0 and sigma>2:
			#thestock.sell(thestock.close[i], thestock.date[i])
			return 'sell'

def main():

   	twtr_data = get_stock_data('/home/grandoverlord/quant/Stocks/GOOG-NYSE_TWTR.csv')
   	cnat_data = get_stock_data('/home/grandoverlord/quant/Stocks/GOOG-NASDAQ_CNAT.csv')
   	tsl_data = get_stock_data('/home/grandoverlord/quant/Stocks/GOOG-NYSE_TSL.csv')

   	#init stock for purchase
   	mystock=stock()
   	
   	
   	curr_price=twtr_data.close[2]
	mystock.buy('twtr', curr_price, twtr_data.date[2])
	
	
	curr_price=tsl_data.close[2]
	#mystock.buy('tsl', curr_price, tsl_data.date[2])
	
	last_price=curr_price

	'''
	simple trading algo
	assumes that stock is bought at the closing price and that the
	desired quantity was available at that price
	'''
	
	for i in range(5, 178):

		
		twtr_buffer=twtr_data.close[i-5:i]
		#cnat_buffer = cnat_data.close[i-5:i]
		#tsl_buffer = tsl_data.close[i-8:i]

		twtr_signal=buy_signal(twtr_buffer)
		#cnat_signal=buy_signal(cnat_buffer)
		#tsl_signal=buy_signal(tsl_buffer)

		#determine best candidate to buy
		# upward slope and hit a peak
		
		if twtr_signal=='buy':
			mystock.buy('twtr', twtr_data.close[i], twtr_data.date[i])
		elif twtr_signal=='sell':
			mystock.sell('twtr', twtr_data.close[i], twtr_data.date[i])

		'''
		if cnat_signal=='buy':
			mystock.buy('cnat', cnat_data.close[i], cnat_data.date[i])
		elif cnat_signal == 'sell':
			mystock.sell('cnat', cnat_data.close[i], cnat_data.date[i])
		
		
		if tsl_signal=='buy':
			mystock.buy('tsl', tsl_data.close[i], tsl_data.date[i])
		elif tsl_signal=='sell':
			mystock.sell('tsl', tsl_data.close[i], tsl_data.date[i])

		'''

		print twtr_data.date[i]+ " " + mystock.get_name() + " " +\
			str(mystock.get_money()+mystock.get_stock_value()) + " " + \
			str(mystock.get_num_shares())

	
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
