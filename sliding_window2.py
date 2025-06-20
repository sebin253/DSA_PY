#Given an array of positive integers arr and an integer target, find the length of the smallest subarray whose sum is greater than or equal to target. If no such subarray exists, return 0.
def min_subarray_len(target, arr):
    n = len(arr)
    left = 0
    total = 0
    min_length = float('inf')

    for right in range(n):
        total += arr[right]

        while total >= target:
            min_length = min(min_length, right - left + 1)
            total -= arr[left]
            left += 1

    return min_length if min_length != float('inf') else 0

# Test case
arr = [2, 3, 1, 2, 4, 3]
target = 7
print("Minimum subarray length with sum ≥", target, "is", min_subarray_len(target, arr))
