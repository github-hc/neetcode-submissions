class Solution:
    def find(self, arr, target, l, r):
        if l>r:
            return False

        mid = (l+r)//2
        if arr[mid] == target:
            return True

        if target < arr[mid]:
            return self.find(arr, target, l, mid-1)
        else:
            return self.find(arr, target, mid+1, r)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
   
        top = 0
        bottom = row-1

        while top <= bottom:
            res = self.find(matrix[top], target, 0, len(matrix[top])-1)

           
            if res:
                return True
                
            top +=1

        return False

            