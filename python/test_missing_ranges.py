# Welcome to Meta!

# This is just a simple shared plaintext pad, with no execution capabilities.

# When you know what language you would like to use for your interview,
# simply choose it from the dropdown in the left bar.

# Enjoy your interview!

"""
https://leetcode.com/problems/missing-ranges
Question:
Given a sorted integer array nums, where the range of elements are in the
inclusive range [lower, upper], return its missing ranges. For example,
given [0, 1, 3, 50, 75], return [“2”, “4->49”, “51->74”, “76->99”]

Example Questions Candidate Might Ask:
Q: What if the given array is empty?
A: Then you should return [“0->99”] as those ranges are missing.
Q: What if the given array contains all elements from the ranges? 
A: Return an empty list, which means no range is missing.
"""


def get_missing_frame(sorted_arr: list[int], spec_limit: list[int]) -> list[str]:
    pre = sorted_arr[0]
    res = []
    LSL = spec_limit[0]
    USL = spec_limit[1]
    if pre!= LSL:
        res.append(f"{LSL}->{pre-1}")
    
    for cur in sorted_arr[1:]:
        if cur > pre + 1:
            if cur < pre + 3:
                res.append(f"{pre+1}")
            else:
                res.append(f"{pre+1}->{cur-1}")
        pre = cur

    if cur!= spec_limit[1]:
        res.append(f"{cur+1}->{USL}")
    return res


if __name__ == "__main__":
    sorted_arr = [0, 1, 3, 50, 75]
    spec_limit = [0, 99]
    res = get_missing_frame(sorted_arr, spec_limit)
    print(res)
