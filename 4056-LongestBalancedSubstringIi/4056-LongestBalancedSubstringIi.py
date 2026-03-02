# Last updated: 02/03/2026, 13:55:53
class Solution:
    def longestBalanced(self, s: str) -> int:
        d={(0,0,0):-1}
        last=[-1,-1]
        last2=[-1,-1]
        last2i=0
        a=ord('a')
        ar=[0]*3
        ma=0
        def findlongest(st,en):
            #print('start',st,en,s[st:en])
            swap=-1
            d3={0:st-1}
            total=0
            mal=0
            last=-1
            for i in range(st,en):
                
                v=ord(s[i])-ord('a')
                if v!=last:
                    last=v
                    swap*=-1
                total+=swap
                if total in d3:
                    mal=max(i-d3[total],mal)
                else:
                    d3[total]=i
                #print(s[st:i+1],mal,total,d3)
            return mal
        for ind,le in enumerate(s):
            v=ord(le)-a
            
            ar[v]+=1
            mi=min(ar)
            if(mi)>0:
                ar[0]-=mi
                ar[1]-=mi
                ar[2]-=mi
            t=tuple(ar)
            if t in d:
                ma=max(ind-d[t],ma)
            else:
                d[t]=ind
            
            
            if v!=last[0]:
                lelast=ind-last[1]
                ma=max(ma,lelast)
                if v not in last2:
                    last2=[last[0],v]
                    if (ind-last2i>ma):
                        ma=max(findlongest(last2i,ind),ma)
                    last2i=last[1]
                last=[v,ind]
        ma=max(findlongest(last2i,ind+1),ma)
        ma=max(ind+1-last[1],ma)
        return ma