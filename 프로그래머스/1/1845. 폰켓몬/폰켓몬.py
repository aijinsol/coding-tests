def solution(nums):
    unique_nums = set(nums)
    if len(unique_nums) <= len(nums)//2:
        ans = len(unique_nums)
    else:
        ans = len(nums)//2
    return ans

# 전체 숫자 갯수 n
# 뽑아야하는 숫자 갯수 n/2

# [1,2,3,4,5,6,6,6,6,6] -> 1,2,3,4,5,6
# [1,1,1,1,1,1,1,1,1,1] -> 1
# [1,2,1,1,1,1,1,1,1,1] -> 2
# [1,2,2,1,1,1,1,1,1,1] -> 2
# [1,2,3,4,5,5,1,1,1,1] -> 5
# [1,2,3,4,5,6,1,1,1,1] -> 5
