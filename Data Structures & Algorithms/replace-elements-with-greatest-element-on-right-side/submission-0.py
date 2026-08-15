class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_arr=-1
        for i in range(len(arr)-1,-1,-1):
            current=arr[i]
            arr[i]=max_arr
            max_arr=max(current,max_arr)
        return arr

        