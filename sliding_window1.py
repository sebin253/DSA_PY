def maximum_num(arr, k):
    n =len(arr)
    if n < k:
        return "INVALID INPUT"
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, n):
        window_sum = window_sum + arr[i] - arr[i-k]
        max_sum = max(window_sum, max_sum)
    return max_sum
arr = [1,2,3,4,5,6,7,8]
k = 2
print("sum of max subarray is ",maximum_num(arr,k))
