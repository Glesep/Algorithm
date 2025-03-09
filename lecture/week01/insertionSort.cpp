#include <iostream>
using namespace std;

void insertionSort(int n, int data[]) {
    for (int i = 1; i < n; i++) {
        int tmp = data[i];
        int j = i-1;
        while (j >= 0 && data[j] > tmp) {
            data[j+1] = data[j];    // j 자리에 있던 데이터를 한칸 뒤로(j+1 위치로) shift
            j--;
        }
        data[j+1] = tmp;
    }
}