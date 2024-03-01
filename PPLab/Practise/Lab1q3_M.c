#include <stdio.h>
#include <mpi.h>
#include <math.h>

int main(int argc, char **argv) {
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int a, b;
    if (rank == 0) {
        printf("Enter number a: \n");
        scanf("%d", &a);
        printf("Enter number b: \n");
        scanf("%d", &b);
    }

    MPI_Bcast(&a, 1, MPI_INT, 0, MPI_COMM_WORLD);
    MPI_Bcast(&b, 1, MPI_INT, 0, MPI_COMM_WORLD);

    int result;
    switch (rank) {
        case 0:
            result = a + b;
            printf("ADD: %d\n", result);
            break;
        case 1:
            result = a - b;
            printf("SUB: %d\n", result);
            break;
        case 2:
            result = a / b;
            printf("DIV: %d\n", result);
            break;
        case 3:
            result = a * b;
            printf("MUL: %d\n", result);
            break;
    }

    MPI_Finalize();
    return 0;
}
