8/27/2014
Added MACD, RSI and VMA to chart as well as fixed low lines on chart. Added some button functionality to make things pretty.

8/26/2014
Added web based chart. Uses Flask. Missing labels and the buttons don't work.
8/14/2014
added candlestick.py to quant/qtools
	-candlestick_daily provides basic candlestick analysis
	still buggy and needs to be tuned

qa1.c and qamath.h are a simple trading algo that use least squares to calculate
trendlines and very basic candlesticking. 

qtools is intended to be a collection of common technical analysis tools. Currently
implemented are:
	simple moving average
	exponential moving average
	RSI
	least squares 
	standard deviation
	

Stock data comes from Quandl. Currently only daily data is available.

