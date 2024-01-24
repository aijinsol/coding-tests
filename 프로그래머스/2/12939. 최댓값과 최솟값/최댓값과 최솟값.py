'''Date
- 240124
'''
def solution(s):
    s_splited = list(map(int, s.split()))
    ans = str(min(s_splited)) + " " + str(max(s_splited))
    return ans