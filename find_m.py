#!/usr/bin/env python3
def find_max(nums):
    max_num = nums[0]
    for i in nums:
        if max_num < i:
            max_num = i
    return max_num

def find_min(nums):
    min_num = nums[0]
    for i in nums:
        if min_num > i:
            min_num = i
    return min_num

def main():
    a = [2, 4, 9,  19, 94, 5]
    print(find_max(a))
    print(find_min(a))

if __name__ == '__main__':
    main()
