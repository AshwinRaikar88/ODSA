from typing import List


class Solutions:
    def twoSum0(self, nums: List[int], target: int) -> List[int]:
        """
        Brute force solution
        :param nums: array of integers
        :param target: target sum
        :return: araay of indices that satisfy the target sum
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # Start j from i + 1 to avoid duplicate pairs
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Optimal solution
        :param nums: array of integers
        :param target: target sum
        :return: araay of indices that satisfy the target sum
        """
        # Dictionary to store the index of the elements
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i  # Store the index of the current number


if __name__ == '__main__':
    # Input
    arr = [1, 1, 2, 2, 3, 3, 4, 4, 4]
    target = 6

    # Solutions
    solver = Solutions()

    # Initial Solution
    arr1 = arr[:]  # Create a fresh copy
    print(solver.twoSum0(nums=arr1, target=target))

    # Optimal Solution
    arr2 = arr[:]  # Create a fresh copy
    print(solver.twoSum(nums=arr2, target=target))