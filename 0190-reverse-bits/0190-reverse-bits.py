class Solution:
    def reverseBits(self, n: int) -> int:
        solution = 0
        for i in range(31) : 
            if (n>>i)&1 :
                solution = solution|(1<<(31-i))
        return solution