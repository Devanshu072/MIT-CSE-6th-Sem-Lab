#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

int main(int argc, char **argv) {
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int M, N;
    double local_avg = 0.0, total_avg = 0.0;

    if (rank == 0) {
        printf("Enter the value of M: ");
        scanf("%d", &M);
        printf("Enter the value of N: ");
        scanf("%d", &N);
    }

    MPI_Bcast(&M, 1, MPI_INT, 0, MPI_COMM_WORLD);

    // Calculate local sum and average
    int *local_array = (int *)malloc(M * sizeof(int));
    int local_sum = 0;
    for (int i = 0; i < M; i++) {
        local_array[i] = (rank + 1) * (i + 1); // Dummy data for demonstration
        local_sum += local_array[i];
    }
    local_avg = (double)local_sum / M;

    // Reduce local averages to get total average
    MPI_Reduce(&local_avg, &total_avg, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

    // Print total average in root process
    if (rank == 0) {
        total_avg /= size;
        printf("Total average: %.2f\n", total_avg);
    }

    free(local_array);
    MPI_Finalize();
    return 0;
}
