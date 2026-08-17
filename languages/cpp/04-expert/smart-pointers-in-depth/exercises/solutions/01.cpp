#include <iostream>
#include <memory>
#include <string>
#include <utility>
using namespace std;

class Resource {
  public:
    explicit Resource(string resourceName) : name(move(resourceName)) {}

    string name;
};

int main() {
    string sourceName;
    string destinationName;
    getline(cin, sourceName);
    getline(cin, destinationName);
    unique_ptr<Resource> source =
        sourceName == "empty" ? nullptr : make_unique<Resource>(sourceName);
    unique_ptr<Resource> destination =
        destinationName == "empty" ? nullptr : make_unique<Resource>(destinationName);

    cout << "Source: " << (source ? source->name : "empty") << '\n';
    cout << "Destination: " << (destination ? destination->name : "empty") << '\n';
    if (!source) {
        cout << "Transfer: source empty\n";
    } else if (destination) {
        cout << "Transfer: destination occupied\n";
    } else {
        destination = move(source);
        cout << "Transfer: moved\n";
    }
    cout << "Source: " << (source ? source->name : "empty") << '\n';
    cout << "Destination: " << (destination ? destination->name : "empty") << '\n';

    return 0;
}
