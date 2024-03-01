#include <stdio.h>
#include "mpi.h"
#include <math.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    int rank , size;
    MPI_Init(&argc, &argv);
    int x =2;
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    double P = pow(x,rank);
    printf("power is %f", P);
    MPI_Finalize();

}