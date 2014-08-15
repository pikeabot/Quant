def candlestick_daily(stock_open, stock_close, stock_high, stock_low):

	mean = (stock_high+stock_low)/2
	delta_hl = stock_high -stock_low
	
	real_body = stock_close - stock_open

	if stock_open>=stock_close:
		upper_shadow = stock_high-stock_open
		lower_shadow = stock_close-stock_low
	else:
		upper_shadow = stock_high-stock_close
		lower_shadow = stock_close-stock_low
	#doji

	# long body

	if abs(real_body)>=.65*delta_hl:

		#long body
		if abs(real_body)>=.08*mean:
			if real_body>0:
				return 'longw'
			else:
				return 'longb'
		#short body
		else:
			if real_body>0:
				return 'shortw'
			else:
				return 'shortb'

	#long shadows
	if lower_shadow >=.98*delta_hl:
		if stock_open>=.98*stock_high or stock_close >=.98*stock_high:
			return 'dragonfly doji'

	elif lower_shadow>=.7*delta_hl:
		if stock_close>=stock_open:
			if stock_open>=.99*stock_high:
				return 'hanging hammer white'
			else:
				return 'long lower'
		else:
			if stock_close>=.99*stock_high:
				return 'hanging hammer black'
			else:
				return 'long lower'

	if upper_shadow >=.98*delta_hl:
		if stock_open>=.98*stock_low or stock_close >=.98*stock_low:
			return 'gravestone doji'

	elif upper_shadow >=.7*delta_hl:
		if stock_close>stock_open:
			if stock_open>=.99*stock_low:
				return 'inverted_hammer white'
			else:
				return 'long upper'
		else:
			if stock_close>=.99*stock_low:
				return 'inverted hammer black'
			else:
				return 'long upper'


	#spinning tops
	if abs(real_body)<.3*delta_hl:
		if real_body>0:
			if stock_open >= mean and stock_close <= mean:
				return 'spinning top white'
		else:
			if stock_close>=mean and stock_open <= mean:
				return 'spinning top black'

	return 'blah'



