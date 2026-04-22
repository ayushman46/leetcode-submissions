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
        colstart = 0
        colend = n - 1
        rowstart = 0
        rowend = m - 1
        result = []

        while count < c:
            # Traverse from left to right along top row
            for i in range(colstart, colend + 1):
                result.append(matrix[rowstart][i])
                count += 1
            rowstart += 1
            if count == c:
                break

            # Traverse from top to bottom along right column
            for j in range(rowstart, rowend + 1):
                result.append(matrix[j][colend])
                count += 1
            colend -= 1
            if count == c:
                break

            # Traverse from right to left along bottom row
            if rowstart > rowend:  # Prevent invalid traversal
                break
            for i in range(colend, colstart - 1, -1):
                result.append(matrix[rowend][i])
                count += 1
            rowend -= 1
            if count == c:
                break


            for i in range(rowend, rowstart - 1, -1):
                result.append(matrix[i][colstart])
                count += 1
            colstart += 1

        return result