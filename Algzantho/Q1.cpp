#include <iostream>
#include <string>

using namespace std;

int main() {
    string moves;
    cin >> moves;

    int ballPosition = 1; 
    for (char move : moves) {
        if (move == 'A') {
  if (ballPosition == 1) {
     ballPosition = 2;
  } else if (ballPosition == 2) {
          ballPosition = 1;
            }
        } else if (move == 'B') {
  if (ballPosition == 2) {
                ballPosition = 3;
            } else if (ballPosition == 3) {
                ballPosition = 2;
            }
        } else if (move == 'C') {
            if (ballPosition == 1) {
                ballPosition = 3;
            } else if (ballPosition == 3) {
                ballPosition = 1;
            }
             }
    }

    cout << ballPosition << endl;

    return 0;
}