import os


class stock_data:
	def __init__(self, date, openp, high, low, close, volume):
		self.date=date
		self.openp=openp
		self.high=high
		self.low=low
		self.close=close
		self.volume=volume

def get_stock_data(filename):
	data=[]
	date=[]
	openp=[]
	high=[]
	low=[]
	close=[]
	volume=[]

	#filename='/home/grandoverlord/quant/Stocks/GOOG-NYSE_TWTR.csv'

	try:
		fh=open(filename, "r")

	except IOError:
   		print "Error: can\'t find file or read data"
	else:
   		fh.readline()

   		for i in range(0, 184):
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


   	return stock_data(date, openp, high, low, close, volume)

def get_stock_data1(filename):
	data=[]
	date=[]
	openp=[]
	high=[]
	low=[]
	close=[]
	volume=[]

	#filename='/home/grandoverlord/quant/Stocks/GOOG-NYSE_TWTR.csv'

	try:
		fh=open(filename, "r")

	except IOError:
   		print "Error: can\'t find file or read data"
	else:
   		fh.readline()

   		for i in range(0, 184):
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

   		for i in range (0, 184):
   			data.append({"date":date[i], 
   						"open":openp[i], 
   						"high":high[i],
   						"low": low[i],
   						"close":close[i],
   						"volume": volume[i]})

   	return data
