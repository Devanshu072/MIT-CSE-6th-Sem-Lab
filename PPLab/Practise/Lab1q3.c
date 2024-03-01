#include <stdio.h>
#include <mpi.h>
#include <math.h>

int main( int argc, char **argv)
{
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    int a, b;
    printf("Enter number a: \n");
    scanf("%d", &a);
    printf("Enter number b: \n");
    scanf("%d", &b);
    if(rank == 0)
        printf("ADD:%d\n", a+b);
    if(rank == 1)
        printf("SUB: %d\n", a-b);
    if(rank == 2)
        printf("DIV: %d\n", a/b);
    if (rank == 3)
        printf("MUL: %d\n", a*b);
    MPI_Finalize();
}