LU_Sol: LU_decomposition.c
	gcc -Wall LU_decomposition.c -lm -lgsl -lgslcblas -o LU.out

clean:
	rm LU.out
