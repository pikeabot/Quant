#include <stdio.h>
#include <stdbool.h>
#include <stdarg.h>
#include <math.h>
#include "qamath.h"


char *data[177][6];
const int STOCK_DATA_LEN=178;

struct stock {
	double money;
	double stock_value;
	double commission;
	int num_shares;
	double buy_price;
	double sell_price;
	char *last_buy_date;
	char *last_sell_date;
};

//parse data out of csv sheet containing daily stock info
char *getdata(char filename[]) {
	FILE *ifp;
	char *mode = "r";
	char s[2]=",";
	char *token;
	int i,j,k;
	//char data[178][6];

	//char inputFilename[] = "GOOG-NYSE_TWTR.csv";

	ifp = fopen(filename, mode);

	if (ifp == NULL) {
	  fprintf(stderr, "Can't open input file %s!\n", filename);
	  exit(1);
	}

	static char line[178][200];  /* One extra for nul char. */

	//while (fscanf(ifp, "%s %d", username, &score) != EOF) {
	
	for (i=0; i<178; i++) {

		if (fscanf(ifp, "%s", line[i])!=EOF) {
	  //printf("%s \n", line[i]);
		}
		else{
			break;
		}
	}
	fclose(ifp);

	j=0;k=0;
	   /* get the first token */
	for (i=STOCK_DATA_LEN-1; i>-1; i--) {
	   token = strtok(line[i], s);
	   
	   /* walk through other tokens */
	   while( token != NULL ) 
	   {
	      //printf( " %s ", token );
	    data[j][k]=token;
	    //printf( " %s ", data[j][k] );
	    k++;
	    if (k==6) {
	    	k=0;
	    	j++;
	    	//printf( " \n" );
	    }
	      token = strtok(NULL, s);
	   }
	}
	return data;
}


/*
	Buy stock
	
	Assumptions:
	You can get the desired quantity.
	You get the maximum number of shares you can afford
	You get them at the closing price
*/
struct stock buy( struct stock tckr, double curr_price, char *purchase_date){

	tckr.num_shares=(int)(tckr.money-tckr.commission)/curr_price;
	tckr.money=tckr.money-tckr.commission - (double)tckr.num_shares*curr_price;
	tckr.buy_price=curr_price;
	tckr.last_buy_date=purchase_date;
	tckr.stock_value=tckr.num_shares*curr_price;
	//printf("%d \n", tckr.num_shares);
	return tckr;
}

/*
	Sell stock

	Assumptions:
	You can sell all of the currently held stock.
	You sell them at the closing price
*/
struct stock sell( struct stock tckr, double curr_price, char *sell_date){

	tckr.money=tckr.money+(double)tckr.num_shares*curr_price-tckr.commission;
	tckr.sell_price=curr_price;
	tckr.last_sell_date=sell_date;
	tckr.num_shares=0;
	tckr.stock_value=0;

	return tckr;
}

struct stock update_stock_value( struct stock tckr, double curr_price){

	tckr.stock_value=(double)tckr.num_shares*curr_price;
	return tckr;
}

char candlestick(char *daily_data[]) {
	double open;
	double high;
	double low;
	double close;
	double delta_co;	//change between opening and closing price
	double delta_hl;		//change between high and low prices
	double daily_mean;
	double hl2co; //ratio of open to close to high and low;

 	sscanf(daily_data[1], "%lf", &open);
 	sscanf(daily_data[2], "%lf", &high);
 	sscanf(daily_data[3], "%lf", &low);
 	sscanf(daily_data[4], "%lf", &close);

 	delta_co=close-open;
 		if (delta_co==0) {
 			delta_co=.001;
 		}
 	delta_hl=high-low;
 	daily_mean=delta_hl/2;
 	hl2co=delta_hl/delta_co;

 	if (fabs(hl2co) > 5) {
 		return 'p';
 	}
	else {
		return 'n';
	}
}


/* 
	Run backtesting for simple trading algo using Quandl data for Twitter.
	Data comes in csv format and trades are done on a minimum of a day to day 
	basis as no minute information is available. Analysis is done using trendlines
	calculated via least squares and basic candlesticking.
*/

int main() {

	char inputFilename[] = "GOOG-NYSE_TWTR.csv";
	double time_buffer[BUFF_LEN];
	int i, j, k;
	double avg_price;
	double avg_price_last=0;
	double last_price;
	double curr_price;
	struct least_squares ls;
	struct stock twtr;
	char signal;
	char *day_data[6];

	//get data out of csv file
	getdata(inputFilename);

	//initialize stock info and buy as much stock as possible on the first day
	twtr.money=10000; //starting with $10k
	twtr.commission=9.99; //cost per trade
	twtr.num_shares=0;
	sscanf(data[2][4], "%lf", &curr_price);
	twtr=buy(twtr, curr_price, data[2][0]);
	last_price=curr_price;

	//loop through dates
	for (i=2; i<STOCK_DATA_LEN-1; i++) {
	//for (i=2; i<3; i++) {
		for (j=0; j<BUFF_LEN;j++) {
			sscanf(data[i+j-2][4], "%lf", &time_buffer[j]);
		}
		avg_price_last=avg_price;
		avg_price=get_average(time_buffer);

		//get approximate trendline via least squares
		ls=calc_least_squares(time_buffer);

		for (k=0; k<6;k++) {
			day_data[k]=data[i][k];
		}
		//printf("%s ", data[i][0] );

		signal=candlestick(day_data);
		sscanf(data[i][4], "%lf", &curr_price);
		twtr=update_stock_value(twtr, curr_price);

		if (signal=='p' && ls.m <2 && twtr.num_shares==0 ) {
			twtr=buy(twtr, curr_price, data[i][0]);
		}
		else if (signal=='p' && ls.m >1 && twtr.num_shares>0 ) {
			twtr=sell(twtr, curr_price, data[i][0]);
		}

		else if (twtr.stock_value>1.1*twtr.buy_price*twtr.num_shares) {
			twtr=sell(twtr, curr_price, data[i][0]);
		}

		else if ((last_price-curr_price)/last_price <-.07) {
			twtr=sell(twtr, curr_price, data[i][0]);
		}

		else if (ls.m<.01) {
			twtr=sell(twtr, curr_price, data[i][0]);
		}

		//printf("%f  %f  %f  ", time_buffer[0], time_buffer[1], time_buffer[2] );
		//printf("%s  %f\n", data[i][0], ls.m );
		last_price=curr_price;
		printf("%s  %f %f\n", data[i][0], twtr.money, twtr.money+twtr.num_shares*curr_price);

	}
}