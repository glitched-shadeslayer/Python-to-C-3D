#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main() //main function begins
{

//Defining the variables
int m,n;//integers
double **A,**B,**crossB,k, r, **O, **crossprod;

//Given points
A = loadtxt("./data/A.dat",3,1);
B = loadtxt("./data/B.dat",3,1);

//Matrix for cross product
crossB= loadtxt("./data/crossB.dat",3,3);

//To calculate the constant k
O = matmul(transpose(B,3,1),A,1,3,1);
r = linalg_norm(O,1);
//printf("%lf\n",r);

k = -r/((linalg_norm(A,3))*(linalg_norm(A,3)));
//printf("%lf\n",k);

crossprod= matmul(crossB,A,3,3,1);
crossprod= scalarmul(crossprod,3,1,k);
printf("\nThe cross product vector = \n");
print(crossprod,3,1);

//free(A);
//free(B);
//free(crossB);
//free(O);
return 0;
}

