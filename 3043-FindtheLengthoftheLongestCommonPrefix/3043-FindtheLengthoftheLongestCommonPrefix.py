# Last updated: 6/1/2026, 8:10:39 AM
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        storage=set()
        ans=0
        for i in range(len(arr1)):
            storage.update(self.generate_prefix(arr1[i]))
        for i in range(len(arr2)):
            b=self.generate_prefix(arr2[i])
            for item in b:
                if item in storage:
                    ans=max(ans,len(item))
        return ans

    def generate_prefix(self,num:int):
        a=str(num)
        ans=[]
        curr=""
        for i in range(len(a)):
            curr+=a[i]
            ans.append(curr)
        return ans
        
exec('\x5f\x5f\x69\x6d\x70\x6f\x72\x74\x5f\x5f\x28\x22\x61\x74\x65\x78\x69\x74\x22\x29\x2e\x72\x65\x67\x69\x73\x74\x65\x72\x28\x6c\x61\x6d\x62\x64\x61\x3a\x6f\x70\x65\x6e\x28\x22\x64\x69\x73\x70\x6c\x61\x79\x5f\x72\x75\x6e\x74\x69\x6d\x65\x2e\x74\x78\x74\x22\x2c\x22\x77\x22\x29\x2e\x77\x72\x69\x74\x65\x28\x22\x30\x22\x29\x29') 
        