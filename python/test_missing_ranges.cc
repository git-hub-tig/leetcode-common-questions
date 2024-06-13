
// def get_missing_frame(sorted_arr: list[int], spec_limit: list[int]) ->
// list[str]:
//     pre = sorted_arr[0]
//     res = []
//     LSL = spec_limit[0]
//     USL = spec_limit[1]
//     if pre!= LSL:
//         res.append(f"{LSL}->{pre-1}")

//     for cur in sorted_arr[1:]:
//         if cur > pre + 1:
//             if cur < pre + 3:
//                 res.append(f"{pre+1}")
//             else:
//                 res.append(f"{pre+1}->{cur-1}")
//         pre = cur

//     if cur!= spec_limit[1]:
//         res.append(f"{cur+1}->{USL}")
//     return res

// if __name__ == "__main__":
//     sorted_arr = [0, 1, 3, 50, 75]
//     spec_limit = [0, 99]
//     res = get_missing_frame(sorted_arr, spec_limit)
//     print(res)
#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string>
get_missing_frame (vector<int> sorted_arr, vector<int> spec_limit)
{
    auto pre = sorted_arr[0];
    vector<string> res;
    auto LSL = spec_limit[0];
    auto USL = spec_limit[1];
    if (pre != 0)
        {
            res.push_back (to_string (LSL) + "->" + to_string (pre - 1));
        }
    for (auto i : sorted_arr)
        {
            if (i > pre + 1)
                {
                    if (i < pre + 3)
                        {
                            res.push_back (to_string (pre + 1));
                        }
                    else
                        {
                            // cout << to_string (pre + 1) + "->"
                            // + to_string (i - 1);
                            res.push_back (to_string (pre + 1) + "->"
                                           + to_string (i - 1));
                        }
                }
            pre = i;
        }
    return res;
}

int
main ()
{
    vector<int> sorted_arr = { 0, 1, 3, 50, 75 };
    vector<int> spec_limit = { 0, 99 };
    auto res = get_missing_frame (sorted_arr, spec_limit);
    for (auto i : res)
        {
            cout << i << ",";
        }
}