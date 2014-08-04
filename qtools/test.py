import os
import math
from qtools import *

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

	date=[]
	openp=[]
	high=[]
	low=[]
	close=[]
	volume=[]

	filename='/home/grandoverlord/quant/GOOG-NYSE_TWTR.csv'

	try:
		fh=open(filename, "r")

	except IOError:
   		print "Error: can\'t find file or read data"
	else:
   		fh.readline()

   		for i in range(0, 178):
	   		line=fh.readline()
	   		l=line.split(',')
	   		date.append(l[0])
	   		openp.append(float(l[1]))
	   		high.append(float(l[2]))
	   		low.append(float(l[3]))
	   		close.append(float(l[4]))
	   		volume.append(float(l[5]))
 
   		date.reverse()
   		openp.reverse()
   		high.reverse()
   		low.reverse()
   		close.reverse()
   		volume.reverse()
   		fh.close()

   	#init stock for purchase
   	twtr=stock()
   	curr_price=close[2]
	twtr.buy(curr_price, date[2])
	last_price=curr_price

	'''
	simple trading algo
	assumes that stock is bought at the closing price and that the
	desired quantity was available at that price
	'''
	'''
	for i in range(5, 178):
		time_buffer=close[i-5:i]
		m=least_squares(time_buffer)
		sigma= standard_dev(time_buffer)

		# upward slope and hit a peak
		
		if m>2 and sigma>2 :
			twtr.buy(close[i], date[i])
		elif m<0 and sigma>2:
			twtr.sell(close[i], date[i])
		print date[i]+ " " + str(m) + " "+ str(sigma) + " " +\
			str(twtr.get_money()+twtr.get_stock_value()) + " " + \
			str(twtr.get_num_shares())
	'''

	'''
	for i in range(0, 25):
		print rsi(close[i:i+10])
	'''

	emalist=[]
	sma=get_avg(close[0:19])
	emalist.append(sma)
	curr_ema=ema(close[20],  sma, 20)
	print curr_ema
	emalist.append(curr_ema)

	for i in range(21, 35):
		curr_ema=ema(close[i], emalist[-1], 20)
		print date[i]+ " " + str(curr_ema)
		emalist.append(curr_ema)

if __name__=='__main__':
		main()
