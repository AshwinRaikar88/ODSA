from typing import List


class Solutions:
    def removeDuplicatesO(self, nums: List[int]) -> int:
        """
        Initial Solution
        :param nums: array of integers
        :return: k (int) - number of unique elements in nums
        """
        dic = {}
        count = 0

        for num in range(len(nums)):
            element = nums[num]
            if nums[num] in dic:
                nums[num] = 100000
                dic[element] += 1
                count += 1
            else:
                dic[element] = 1

        nums.sort()
        print(nums)
        return len(nums) - count

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Optimal Solution
        :param nums: array of integers
        :return: k (int) - number of unique elements in nums
        """
        if not nums:
            return 0  # Edge case: empty array

        i = 0  # Slow pointer

        for j in range(1, len(nums)):  # Fast pointer starts from the second element
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]  # Update the position for the next unique element
        print(nums)
        return i + 1  # Number of unique elements


if __name__ == '__main__':
    # Input
    arr = [1, 1, 2, 2, 3, 3, 4, 4, 4]

    # Solutions
    solver = Solutions()

    # Initial Solution
    arr1 = arr[:]  # Create a fresh copy
    print(solver.removeDuplicatesO(nums=arr1))

    # Optimal Solution
    arr2 = arr[:]  # Create a fresh copy
    print(solver.removeDuplicates(nums=arr2))