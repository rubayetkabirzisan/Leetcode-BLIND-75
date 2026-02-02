class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            # Check if the Left portion is sorted
            if nums[l] <= nums[mid]:
                # Logic: Is target inside the sorted left portion?
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            # Otherwise, the Right portion must be sorted
            else:
                # Logic: Is target inside the sorted right portion?
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
        return -1