class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = dict()

        for i,v in enumerate(nums):
            compl = target - v
            if compl in visited:
                return [visited[compl], i]
            else:
                visited[v] = i