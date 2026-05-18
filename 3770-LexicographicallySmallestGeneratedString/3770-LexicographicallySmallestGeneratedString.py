# Last updated: 5/18/2026, 5:01:18 PM
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        ans = ["a"]*(m+n-1)
        ind = [-1]*(m+n-1)
        
        j = m
        for i in range(m+n-1): 
            if i < n and str1[i] == 'T': j = 0 
            if j < m: 
                ans[i] = str2[j]
                ind[i] = j
            j += 1
        
        k = 0
        lps = [0]
        for i in range(1, m):
            while k and str2[k] != str2[i]: k = lps[k-1]
            if str2[k] == str2[i]: k += 1
            lps.append(k)
        
        k = 0
        last = -1
        for i, ch in enumerate(ans): 
            if ind[i] == -1: last = i 
            while k and (k == m or str2[k] != ch): k = lps[k-1]
            if str2[k] == ch: k += 1
            if i >= m-1: 
                if str1[i-m+1] == 'T' and k < m: return ""
                if str1[i-m+1] == 'F' and k == m: 
                    if last < i-m+1: return ""
                    ans[last] = 'b'
                    if ind[i] != -1: k = ind[i]+1
                    else: k = 0 
        
        return "".join(ans)