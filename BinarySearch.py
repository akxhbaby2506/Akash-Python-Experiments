"""
def binarySearch(nums,ele):
    
    beg = 0
    end = len(nums)-1
    mid = (beg+end)/2
    
    while(beg<end):
        
        if (ele==nums[mid]):
            print(mid)
        elif (ele<nums[mid]):
            end = mid - 1
        elif (ele>nums[mid]):
            beg = mid + 1
        
print(binarySearch([1,3,4,6,9,12,14],9))
"""
#Idk y my bloody code is not working


def search(nums, target):
    l, r = 0, len(nums) - 1
    
    while l <= r:
        m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    return -1
print(search([1,3,4,6,9,12,14],9))