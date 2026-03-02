# Last updated: 02/03/2026, 13:55:37
class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        b_c=[-1,-1]
        m_q=-1
        cx,cy=center
        for x,y,q in towers:
            d=abs(x-cx)+abs(y-cy)
            if d <=radius:
                if q>m_q:
                    m_q=q
                    b_c=[x,y]
                elif q==m_q:
                    if [x,y]<b_c:
                        b_c=[x,y]
        return b_c