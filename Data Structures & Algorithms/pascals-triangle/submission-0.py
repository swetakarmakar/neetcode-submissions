class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            current = []

            for j in range(i+1):
                if j == 0 or j == i:
                    current.append(1)
                else:
                    value = triangle[i-1][j-1] + triangle[i-1][j]
                    current.append(value)
            
            triangle.append(current)

        return(triangle)