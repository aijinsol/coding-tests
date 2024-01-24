'''Date
- 240124
'''
def solution(s):
    ans = ""
    for idx, chr in enumerate(s):
        if idx == 0:
            ans += chr.upper()
        elif chr.isalpha() and s[idx-1] == " ":
            ans += chr.upper()
        else:
            ans += chr.lower()
    return ans