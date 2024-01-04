//Question:
//Design and implement a TwoSum class. It should support the following
//operations: add and find.
//add(input) – Add the number input to an internal data structure.
//find(value) – Find if there exists any pair of numbers which sum is
//equal to the value.
//
//For example,
//add(1); add(3); add(5); find(4) - true; find(7) - false
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class TwoSum {
private:
    vector<int> data;
public:
    void add(int number) {
        data.push_back(number);
    }
    bool find(int target) {
        unordered_map<int, int> hash;
        for (int i = 0; i < data.size(); i++) {
            int numberToFind = target - data[i];
            //if numberToFind is found in map, return them
            if (hash.find(numberToFind) != hash.end()) {
                return true;
            }
            //number was not found. Put it in the map.
            hash[data[i]] = i;
        }
        return false;
    }
};
/*
no instance of overloaded function "std::__1::vector<_Tp, _Allocator>::insert [with _Tp=int, _Allocator=std::__1::allocator<int>]" matches the argument listC/C++(304)
03_two_sum_III.cpp(19, 14): argument types are: (int)
03_two_sum_III.cpp(19, 14): object type is: std::__1::vector<int, std::__1::allocator<int>>

*/

int main(){
    auto s = TwoSum ();
    s.add (1);
    s.add (3);
    s.add (5);

    cout << s.find (4) << endl;
    //  - true;

    cout << s.find (7) << endl;
    // - false
}