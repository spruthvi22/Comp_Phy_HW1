/*
* Author:Pruthvi Suryadevara
* Email: pruthvi.suryadevara@tifr.res.in
* Description: Solving linear system LU decomposition 
* Compile using makefile with output LU.out
*/

#include<stdio.h>
#include<stdlib.h>
#include<gsl/gsl_linalg.h>

int main()
{
  double A_data[]={1,0.67,0.33,0.45,1,0.55,0.67,0.33,1};  /* Defining A,b in solving A.x=b*/
  double b_data[]={2,2,2};
  int n=sizeof(b_data)/sizeof(b_data[0]);
  gsl_matrix_view A=gsl_matrix_view_array(A_data,n,n);    /* Creating a Matrix view of A for using in GSL functions */
  gsl_vector_view b=gsl_vector_view_array(b_data,n);      /* Creating a Vector view of B for using in GSL functions */
  gsl_vector *x=gsl_vector_alloc(n);                      /* Allocating storage for solution vector x */
  int s;
  gsl_permutation *p=gsl_permutation_alloc(n);            /* Creating a permutation variable for LU decompostion */
  gsl_linalg_LU_decomp(&A.matrix,p,&s);                   
  gsl_linalg_LU_solve(&A.matrix,p,&b.vector,x);           /* Solving system using LU Decomposition */  
  printf(" Solution= \n");
  gsl_vector_fprintf(stdout,x,"%g \n");                   /* Printing the solution of x */
  gsl_permutation_free(p);
  gsl_vector_free(x);
  return 0;
}

/* The solution matches with implies the decomposition is correct */
