#include <iostream>
using namespace std;

int main() {
    int n = 4;

    string points[] = {"P0", "P1", "P2", "P3"};
    int arrivals[] = {0,1, 2, 3};
    int bursts[] = {4, 3, 1,2};

    int completion[n];
    int turnaround[n];
    int waiting[n];


    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arrivals[j] > arrivals[j + 1]) {
                swap(arrivals[j], arrivals[j + 1]);
                swap(bursts[j], bursts[j + 1]);
                swap(points[j], points[j + 1]);
            }
        }
    }

    int time = 0;
    for (int i = 0; i < n; i++) {
        if (time < arrivals[i]) {
            time = arrivals[i];
        }

        completion[i] = time + bursts[i];
        turnaround[i] = completion[i] - arrivals[i];
        waiting[i] = turnaround[i] - bursts[i];

        time = completion[i];
    }


    cout << "Process   AT      BT      Completion    TAT             WT\n";
    for (int i = 0; i < n; i++) {
        cout << points[i] << "\t  "
             << arrivals[i] << "\t  "
             << bursts[i] << "\t  "
             << completion[i] << "\t\t"
             << turnaround[i] << "\t\t"
             << waiting[i] << endl;
    }


    return 0;
}
