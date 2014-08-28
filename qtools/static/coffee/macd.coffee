root = exports ? this

###
draw main stock chart
###

chart = document.getElementById 'chart'
chart_ctx = chart.getContext '2d'
chart_ctx.translate(0.5, 0.5);

point_width=5

x_step = 10
chartline = data.length*x_step
x=0


chart_ctx.beginPath();
chart_ctx.moveTo(0,100);
chart_ctx.lineTo(chartline,100);
chart_ctx.moveTo(0,200);
chart_ctx.lineTo(chartline,200);
chart_ctx.moveTo(0,300);
chart_ctx.lineTo(chartline,300);

###
assume range of 0 to 80
###

for d, i in data
	delta = Math.round(Math.abs(d.close-d.open)*8)
	x=i*x_step

	if d.close >d.open
		y=600-d.close*8
		chart_ctx.fillStyle="#00CC33";
		chart_ctx.fillRect(x, y ,point_width, delta) 

	else
		chart_ctx.fillStyle="#CC0000";
		y = 600-d.open*8
		chart_ctx.fillRect(x,y  ,point_width, delta) 

	### draw high line ###
	chart_ctx.moveTo(x+3, y)
	chart_ctx.lineTo(x+3, 600-d.high*8)

	### draw low line ###
	chart_ctx.moveTo(x+3, y+delta)
	chart_ctx.lineTo(x+3, 600-d.low*8)

chart_ctx.stroke()

###
vol
###

vol = document.getElementById 'vol'
vctx = vol.getContext '2d'
vctx.translate(0.5, 0.5);

point_width=5
offset=10
x=0

### draw center line ###
vctx.beginPath();
vctx.moveTo(0,75);
vctx.lineTo(chartline,75);

for d, i in data
	### 
	scale volume to fit 150px height box 
	assume max of 150,000,000 for twitter
	###
	delta = d.volume/1000000

	vctx.fillStyle="#888888 ";
	vctx.fillRect(x+i*x_step, 150-delta ,point_width, delta) 
	

vctx.stroke()

###
vma
###
root.showVma = -> 
	vol = document.getElementById 'vol'
	vctx = vol.getContext '2d'
	vctx.translate(0.5, 0.5);
	vctx.rect(x+(i+offset)*x_step, vma_point*10+75 ,point_width, point_height) for vma_point, i in vma_data
	vctx.stroke()




###
macd
###


macd = document.getElementById 'macd'
ctx = macd.getContext '2d'
ctx.translate(0.5, 0.5);

point_width=2
point_height=2
offset=26
x=0

### draw center line ###
ctx.beginPath();
ctx.moveTo(0,75);
ctx.lineTo(chartline,75);
ctx.rect(x+(i+offset)*x_step, macd_point*10+75 ,point_width, point_height) for macd_point, i in macd_line

ctx.fillStyle="#CC0000";
ctx.fillRect(x+(i+offset)*x_step, macd_sgpt*10+75,point_width, point_height) for macd_sgpt, i in macd_signal
ctx.stroke()

###
RSI
###

rsi = document.getElementById 'rsi'
rsi_ctx = rsi.getContext '2d'
rsi_ctx.translate(0.5, 0.5);

point_width=2
point_height=2
offset=10
x=0

### draw center line ###
rsi_ctx.beginPath();
rsi_ctx.moveTo(0,75);
rsi_ctx.lineTo(chartline,75);

rsi_ctx.rect(x+(i+offset)*x_step, rsi_point ,point_width, point_height) for rsi_point, i in rsi_data
rsi_ctx.stroke()


