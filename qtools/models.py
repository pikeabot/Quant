import os
import math

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