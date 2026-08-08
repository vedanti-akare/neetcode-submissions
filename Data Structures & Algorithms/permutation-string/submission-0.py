class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1={}
        count2={}

        for ch in s1:
            count1[ch]=count1.get(ch,0)+1
        for ch in s2[:len(s1)]:
            count2[ch]=count2.get(ch,0)+1

        if count1==count2:
            return True
        
        left=0
        for right in range(len(s1),len(s2)):
            count2[s2[right]]=count2.get(s2[right],0)+1
            count2[s2[left]]-=1
            if count2[s2[left]]==0:
                del count2[s2[left]]
            left+=1

            if count1==count2:
                return True
            
        return False

        