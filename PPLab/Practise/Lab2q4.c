#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

int main(int argc, char **argv[])
{
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    int num;
    if (rank == 0)
    {
        printf("Enter the initial number: ");
        scanf("%d", &num);
        printf("number entered at rank %d is: %d\n", rank, num);
        num++;
        MPI_Send(&num, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);

        MPI_Recv(&num, 1, MPI_INT, size - 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    }
    else
    {
        MPI_Recv(&num, 1, MPI_INT, rank - 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("Rank %d received : %d\n", rank, num);
        num++;

        if (rank == size - 1)
        {
            MPI_Send(&num, 1, MPI_INT, 0, 0, MPI_COMM_WORLD);
        }
        else
        {
            MPI_Send(&num, 1, MPI_INT, rank + 1, 0, MPI_COMM_WORLD);
        }
    }
    MPI_Finalize();
}