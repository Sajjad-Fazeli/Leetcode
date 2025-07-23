class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        def summer(arr):
            new_arr = [1]
            right = 1
            while right < len(arr):
                new_arr.append(arr[right-1] + arr[right])
                right += 1
            new_arr.append(1)
            return new_arr
        arr = [1]
        for i in range(1,numRows+1):
            res.append(arr)
            arr = summer(arr)
            
        return res
        
