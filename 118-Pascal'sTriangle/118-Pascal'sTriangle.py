# Last updated: 6/1/2026, 12:04:44 PM

def facteur(n):
    l=[]
    for i in range(0,n+1):
        l.append(int(factorial(n)/(factorial(i)*factorial(n-i))))
    return l

class Solution:
    def generate(self, n: int) -> List[List[int]]:
        L=[]
        for i in range(0,n):
            L.append(facteur(i))
        return L

        