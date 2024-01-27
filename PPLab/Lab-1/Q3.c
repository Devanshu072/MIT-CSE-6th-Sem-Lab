#include <mpi.h>
#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[])
{
    int rank, size, a = 148, b = 7;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    if (rank == 0)
        printf("Process %d says, Sum of %d and %d is %d\n", rank, a, b, a + b);
    if (rank == 1)
        printf("Process %d says, Difference of %d and %d is %d\n", rank, a, b, a - b);
    if (rank == 2)
        printf("Process %d says, Product of %d and %d is %d\n", rank, a, b, a * b);
    if (rank == 3)
        printf("Process %d says, Quotient of %d and %d is %f\n", rank, a, b, (double)a / b);
    MPI_Finalize();
    return 0;
}