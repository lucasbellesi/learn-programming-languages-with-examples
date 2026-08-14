#include <iostream>
using namespace std;

class Date {
  public:
    Date(int monthValue, int dayValue) : month(monthValue), day(dayValue) {}

    bool isValid() const {
        if (month < 1 || month > 12) {
            return false;
        }

        const int daysInMonth[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        return day >= 1 && day <= daysInMonth[month - 1];
    }

  private:
    int month;
    int day;
};

int main() {
    int month = 0;
    int day = 0;

    cout << "Enter month and day: ";
    cin >> month >> day;

    Date date(month, day);
    cout << (date.isValid() ? "Valid date" : "Invalid date") << '\n';

    return 0;
}
