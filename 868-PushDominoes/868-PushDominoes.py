# Last updated: 02/03/2026, 14:01:32
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        temp = ''
        
        while dominoes != temp:
            temp = dominoes
            dominoes = dominoes.replace('R.L', 'xxx')       
            dominoes = dominoes.replace('R.', 'RR')       
            dominoes = dominoes.replace('.L', 'LL')         

        return  dominoes.replace('xxx', 'R.L')