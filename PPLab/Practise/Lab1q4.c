#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <mpi.h>

int main(int argc, char **argv) {
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    char str[10]; 
    if (rank == 0) {
        printf("Enter the string: \n");
        scanf("%s", str); 
    }

    MPI_Bcast(str, 10, MPI_CHAR, 0, MPI_COMM_WORLD);

    if (str[rank] >= 'a' && str[rank] <= 'z')
        str[rank] = str[rank] - 32;
    else
        str[rank] = str[rank] + 32;

    printf("Process %d: Modified string: %s\n", rank, str);
    MPI_Finalize();
    return 0;
}
