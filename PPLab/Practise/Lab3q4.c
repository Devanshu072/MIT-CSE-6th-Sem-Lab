#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <mpi.h>

int main(int argc, char **argv) {
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    char str1[100];
    char str2[100];
    char fstr1[100];
    char fstr2[100];
    char C[200];
    int m;
    int n = size;
    int concat[100];
    
    if (rank == 0) {
        printf("Enter string 1:");
        scanf("%s", str1);
        printf("Enter string 2:");
        scanf("%s", str2);
        int len1 = strlen(str1);
        int len2 = strlen(str2);

        if (len1 != len2 || len1 % size != 0) {
            printf("Strings are not of proper length or not equal in length\n");
            MPI_Finalize();
            return 1;
        }
        m = len1 / size;
    }

    MPI_Bcast(&m, 1, MPI_INT, 0, MPI_COMM_WORLD);
    MPI_Scatter(str1, m, MPI_CHAR, fstr1, m, MPI_CHAR, 0, MPI_COMM_WORLD);
    MPI_Scatter(str2, m, MPI_CHAR, fstr2, m, MPI_CHAR, 0, MPI_COMM_WORLD);

    int l = 0;
    for (int i = 0; i < m; i++) {
        concat[l++] = fstr1[i];
        concat[l++] = fstr2[i];
    }

    MPI_Gather(concat, 2 * m, MPI_CHAR, C, 2 * m, MPI_CHAR, 0, MPI_COMM_WORLD);

    if (rank == 0) {
        printf("Resultant string: %s\n", C);
    }

    MPI_Finalize();
    return 0;
}
