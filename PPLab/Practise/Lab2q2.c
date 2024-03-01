#include <stdio.h>
#include "mpi.h"
void main(int argc, char **argv)
{
    int rank, size;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    int n;
    if (rank == 0)
    {
        printf("Enter a number : ");
        scanf("%d", &n);

        for (int i = 1; i < size; i++)
            MPI_Send(&n, 1, MPI_INT, i, 1, MPI_COMM_WORLD);
    }
    else
    {
        MPI_Recv(&n, 1, MPI_INT, 0, 1, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("Rank %d received : %d\n", rank, n);
    }
    MPI_Finalize();
}