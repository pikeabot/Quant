#include <stdio.h>
#include <stdbool.h>
#include <stdarg.h>


const int BUFF_LEN=3;

struct least_squares {
	double m;
	double y_intercept;
	};

double get_average(double buff[BUFF_LEN]) {
	double total=0;
	int i;
	double avg;

	for (i=0; i<BUFF_LEN; i++ ) {
		total=total+buff[i];
	}
	avg = total/(double)BUFF_LEN;
	return avg;
}

struct least_squares calc_least_squares(double buff[BUFF_LEN]) {

	double sumx=0;
	double sumy=0;
	double xy=0;
	double xsqrd=0;
	double m;
	struct least_squares ls;
	int i;

	//printf("%f  %f  %f\n", buff[0], buff[1], buff[2] );

	//sum(x)
	for (i=1; i<BUFF_LEN+1; i++) {
		sumx=i+sumx;
		xsqrd=xsqrd+i*i;
	}
	//printf("sumx = %f  ", sumx );
	//sum(y)
	for (i=0; i<BUFF_LEN; i++) {
		sumy=sumy+buff[i];
		xy=xy+buff[i]*(i+1);
	}

	m=(xy-((sumx*sumy)/BUFF_LEN))/(xsqrd-(sumx*sumx)/BUFF_LEN);

	ls.m=m;
	ls.y_intercept=m/(sumx/BUFF_LEN);

	return ls;

}