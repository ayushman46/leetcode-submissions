class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        c = m * n
        count = 0
        top = 0
        r = n - 1
        l = 0
        bottom = m - 1
        result = []

        while count<c:
            for i in range(l,r+1):
                result.append(matrix[top][i])
                count+=1
                
            top+=1
            if count==c:
                    break


            for i in range(top,bottom+1):
                result.append(matrix[i][r])
                count+=1
                
               
            r-=1
            if count==c:
                    break


            for i in range(r,l-1,-1):
                result.append(matrix[bottom][i])
                count+=1
                
            bottom-=1
            if count==c:
                    break


            for i in range(bottom,top-1,-1):
                result.append(matrix[i][l])
                count+=1
                
                
            l+=1
            if count==c:
                    break
        return result