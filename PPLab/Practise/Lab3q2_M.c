#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

int main(int argc, char **argv) {
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int M, N;
    double total_sum = 0.0;

    if (rank == 0) {
        printf("Enter the value of M: ");
        scanf("%d", &M);
        printf("Enter the value of N: ");
        scanf("%d", &N);

        // Allocate memory for the array
        int *array = (int *)malloc(M * N * sizeof(int));
        if (array == NULL) {
            fprintf(stderr, "Memory allocation failed\n");
            MPI_Abort(MPI_COMM_WORLD, 1);
        }

        // Initialize the array
        for (int i = 0; i < M * N; i++) {
            array[i] = i + 1;
        }

        // Scatter data to all processes
        MPI_Scatter(array, M, MPI_INT, MPI_IN_PLACE, M, MPI_INT, 0, MPI_COMM_WORLD);

        free(array);
    } else {
        // Receive the value of M from the root process
        MPI_Bcast(&M, 1, MPI_INT, 0, MPI_COMM_WORLD);
    }

    // Calculate local sum
    int *local_array = (int *)malloc(M * sizeof(int));
    MPI_Scatter(NULL, 0, MPI_INT, local_array, M, MPI_INT, 0, MPI_COMM_WORLD);
    
    double local_sum = 0.0;
    for (int i = 0; i < M; i++) {
        local_sum += local_array[i];
    }
    free(local_array);

    // Calculate local average
    double local_avg = local_sum / M;

    // Gather all local averages to the root process
    double *recv_buf = NULL;
    if (rank == 0) {
        recv_buf = (double *)malloc(size * sizeof(double));
    }
    MPI_Gather(&local_avg, 1, MPI_DOUBLE, recv_buf, 1, MPI_DOUBLE, 0, MPI_COMM_WORLD);

    // Calculate total average in root process
    if (rank == 0) {
        for (int i = 0; i < size; i++) {
            total_sum += recv_buf[i];
        }
        double total_avg = total_sum / size;
        printf("Total average: %.2f\n", total_avg);
        free(recv_buf);
    }

    MPI_Finalize();
    return 0;
}
