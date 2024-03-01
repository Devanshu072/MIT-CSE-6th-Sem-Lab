#include <stdio.h>
#include <string.h>
#include <mpi.h>

int countNonVowels(char *str)
{
    int non_vowel_count = 0;
    for (int i = 0; str[i] != '\0'; i++)
    {
        char c = str[i];
        if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' &&
            c != 'A' && c != 'E' && c != 'I' && c != 'O' && c != 'U')
        {
            non_vowel_count++;
        }
    }
    return non_vowel_count;
}

int main(int argc, char **argv)
{
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    char str[100];
    int m;

    if (rank == 0)
    {
        printf("Enter the string which is divisible of %d: ", size);
        scanf("%s", str);
        m = strlen(str) / size;
    }

    char str2[100];
    MPI_Bcast(&m, 1, MPI_INT, 0, MPI_COMM_WORLD);

    MPI_Scatter(str, m, MPI_CHAR, str2, m, MPI_CHAR, 0, MPI_COMM_WORLD);

    int nonvowel;
    nonvowel = countNonVowels(str2);

    char ans[100];

    MPI_Gather(&nonvowel, 1, MPI_INT, ans, 1, MPI_INT, 0, MPI_COMM_WORLD);

    if (rank == 0)
    {
        int sum = 0;
        for (int i = 0; i < size; i++)
        {
            sum += ans[i];
        }
        printf("Total number of non vowels = %d\n", sum);
    }
    MPI_Finalize();
}