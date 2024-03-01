#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <mpi.h>

#define MAX_STRING_LENGTH 100

int main(int argc, char **argv) {
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    char str[MAX_STRING_LENGTH];
    if (rank == 0) {
        printf("Enter the string: \n");
        scanf("%s", str);

        // Send the string to process 1
        //MPI_Ssend(&msg, size, data type, Destination, Tag, Comm);
        MPI_Ssend(str, strlen(str) + 1, MPI_CHAR, 1, 0, MPI_COMM_WORLD);
        printf("Process 0 sent the string: %s\n", str);

        // Receive the modified string from process 1
        //MPI_Recv(&msg, size, data type, Source, Tag, Comm, &status);
        MPI_Recv(str, MAX_STRING_LENGTH, MPI_CHAR, 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("Process 0 received the modified string: %s\n", str);
    } 
    else if (rank == 1) {
        // Receive the string from process 0
        MPI_Recv(str, MAX_STRING_LENGTH, MPI_CHAR, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("Process 1 received the string: %s\n", str);

        // Toggle the characters
        int i;
        for (i = 0; i < strlen(str); i++) {
            if (str[i] >= 'a' && str[i] <= 'z')
                str[i] = str[i] - 32; // Convert lowercase to uppercase
            else if (str[i] >= 'A' && str[i] <= 'Z')
                str[i] = str[i] + 32; // Convert uppercase to lowercase
        }

        // Send the modified string back to process 0
        MPI_Ssend(str, strlen(str) + 1, MPI_CHAR, 0, 0, MPI_COMM_WORLD);
        printf("Process 1 sent the modified string: %s\n", str);
    }

    MPI_Finalize();
    return 0;
}
