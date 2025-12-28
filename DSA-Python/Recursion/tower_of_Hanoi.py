class Solution:
    def towerOfHanoi(self, n, start, goal, mid):
        if n == 0:
            return
        
        self.towerOfHanoi(n-1, start, mid, goal)
        
        print(f"Move disk {n} from {start} to {goal}")
        
        self.towerOfHanoi(n-1, mid, goal, start)

sol = Solution()
sol.towerOfHanoi(2, "1", "3", "2")