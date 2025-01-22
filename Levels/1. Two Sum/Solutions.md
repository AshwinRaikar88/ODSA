### Brute force method

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # Start j from i + 1 to avoid duplicate pairs
                if nums[i] + nums[j] == target:
                    return [i, j]
```

---

### **Optimal Solution Using a Hash Map**

The brute force solution can be improved to \(O(n)\) time complexity using a hash map to store the complements of the numbers:

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store the index of the elements
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i  # Store the index of the current number
```

#### **Explanation**:
1. For each number in the list:
   - Compute its complement (`target - num`).
   - Check if the complement exists in the dictionary (`seen`).
   - If it exists, return the indices of the complement and the current number.
   - Otherwise, store the current number's index in the dictionary.

---

### **Advantages of the Hash Map Approach**
1. **Time Complexity**: \(O(n)\) because we only traverse the list once.
2. **Space Complexity**: \(O(n)\) due to the hash map storage.