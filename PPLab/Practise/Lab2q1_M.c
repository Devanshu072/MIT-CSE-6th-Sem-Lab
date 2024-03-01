#include <stdio.h>
#include <mpi.h>
#include <stdlib.h>
#include <string.h>

//In your code, you are assuming that the length of the received string will be the same as the length of the string entered by the user in process 0. However, this assumption may not hold true, leading to buffer overflow issues.

// To fix this problem, you should ensure that the buffer size allocated for the str array is large enough to accommodate the maximum possible length of the string. Additionally, you should handle cases where the received string might exceed the allocated buffer size.

#define MAX_STRING_LENGTH 100

int main(int argc, char **argv)
{
    int rank, size;
    MPI_Init(&argc,&argv);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    char str[MAX_STRING_LENGTH];
    
    if(rank == 0){
        printf("Enter the string: ");
        scanf("%s", str);

        MPI_Ssend(str, strlen(str)+1, MPI_CHAR, 1, 0, MPI_COMM_WORLD);
        printf("Process 0 sent the string %s\n", str);

        MPI_Recv(str, MAX_STRING_LENGTH , MPI_CHAR, 1 , 0 , MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("Modifid string is: %s\n", str);
    }
    else if(rank == 1){
        MPI_Recv(str, MAX_STRING_LENGTH , MPI_CHAR, 0 , 0 , MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("Process 1 recieved the string %s\n", str);

// A segmentation fault (signal 11) typically occurs when a program attempts to access memory that it's not allowed to access. In your code, the issue might be related to accessing memory beyond the bounds of an array.

        for(int i=0 ; i<strlen(str); i++)
        {
            if (str[i] >= 'a' && str[i] <= 'z')
                str[i] = str[i] - 32;
            else
                str[i] = str[i] + 32;
        }

        MPI_Ssend(str, strlen(str)+1, MPI_CHAR, 0, 0, MPI_COMM_WORLD);
        printf("Process 1 sent the modified string: %s\n", str);
    }
    MPI_Finalize();

}