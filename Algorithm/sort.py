def quick_sort(L, left, right):
    def division(L, left, right):
        target = L[left]
        while left < right:
            while left < right and L[right] >= target:
                right -= 1
            L[left] = L[right]
            while left < right and L[left] <= target:
                left += 1
            L[right] = L[left]
        L[right] = target
        return right
    if left<right:
        ind = division(L, left, right)
        quick_sort(L, ind+1, right)
        quick_sort(L, left, ind-1)
    return L

def bubble(L):
    n = len(L)
    for i in range(n-1):
        flag = False#表示本趟冒泡是否发生交换的标志
        for j in range(n-1-i):
            if L[j]>L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
                flag = True
        if not flag:#本趟遍历后没有发生交换，说明表已经有序
            return L
    return L

