
To solve this problem efficiently, we can use the **two-pointer technique**, which allows us to iterate through the array while maintaining the desired order and eliminating duplicates in-place. Here's how the approach works step-by-step:

---

### Algorithm:

1. Use two pointers:
   - `i` to track the position of the current unique element (slow pointer).
   - `j` to iterate through the array (fast pointer).

2. Start with both pointers:
   - `i` initialized to `0` (the first position of the array).
   - `j` initialized to `1` (the second position of the array).

3. Compare elements at `j` and `i`:
   - If `nums[j]` is different from `nums[i]`, it means we have encountered a new unique element.
   - Move `i` forward, and update `nums[i]` with `nums[j]`.

4. Continue until `j` reaches the end of the array.

5. The number of unique elements (`k`) will be `i + 1`.

---

### Code:

Here's the Python implementation:

```python
def removeDuplicates(nums):
    if not nums:
        return 0  # Edge case: empty array
    
    i = 0  # Slow pointer
    
    for j in range(1, len(nums)):  # Fast pointer starts from the second element
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]  # Update the position for the next unique element
    
    return i + 1  # Number of unique elements
```

---

### Explanation of Example:

#### Input:
```python
nums = [0, 0, 1, 1, 2, 2, 3, 3, 4]
```

#### Execution:
1. Initial: `nums = [0, 0, 1, 1, 2, 2, 3, 3, 4]`, `i = 0`, `j = 1`
2. `nums[j] == nums[i]` (both are 0), move `j` to 2.
3. `nums[j] != nums[i]` (1 != 0), move `i` to 1, set `nums[1] = 1`.
4. Repeat for `j` through the array:
   - After processing, `nums` becomes: `[0, 1, 2, 3, 4, ..., ..., ...]`.

#### Output:
```python
k = 5
nums[:k] = [0, 1, 2, 3, 4]
```

---

### Complexity:

- **Time Complexity**: \(O(n)\) — Single pass through the array.
- **Space Complexity**: \(O(1)\) — No extra space used.

This approach modifies the array in-place and returns the correct count of unique elements, achieving the desired efficiency.