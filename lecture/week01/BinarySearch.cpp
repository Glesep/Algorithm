#include <iostream>
using namespace std;

int binarySearch(int n, char *data[], char *target) {
    int begin = 0, end = n-1;

    while(begin <= end) {
        int middle = (begin + end) / 2;
        int result = strcmp(data[middle], target);

        if (result == 0)
            return middle;
        else if (result < 0)
            begin = middle+1;
        else
            end = middle-1;
    }

    return -1;
}