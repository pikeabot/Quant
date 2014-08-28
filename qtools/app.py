from flask import Flask, render_template, url_for, jsonify, json
from quandlio import *
from qtools import *

app = Flask(__name__)

data = get_stock_data1('/home/grandoverlord/quant/Stocks/GOOG-NYSE_TWTR.csv')

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
n=len(data)-1
stock = { 
"High" : data[n]['high'], 
"symbol" : "TWTR", 
"Volume" : data[n]['volume'], 
"Low" : data[n]['low'], 
"Date" : data[n]['date'], 
"Close" : data[n]['close'], 
"Open" : data[n]['open'] }

@app.route('/')
def index():
    sdata = json.dumps(data)
    macdln = macd_line(data)
    macdsg =macd_signal_line( macdln)
    rsidata=rsi(data, 10)
    vmadata=vma(data, 10)
    return render_template('index.html', 
    						stock=stock, 
    						stock_data=sdata, 
    						macd_line = json.dumps(macdln), 
    						macd_signal=json.dumps(macdsg),
                            rsi_data=json.dumps(rsidata),
                            vma_data= json.dumps(vmadata)
    						)


if __name__ == '__main__':
	app.debug = True
	app.run()