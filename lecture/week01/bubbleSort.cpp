#include <iostream>
using namespace std;

void bubbleSort(int data[], int n) {
    for (int i = n-1; i > 0; i--) {
        for (int j = 0; j < i; j++) {
            if (data[j] > data[j+1]) {
                int tmp = data[j];
                data[j] = data[j+1];
                data[j+1] = tmp;
            }
        }
    }
}