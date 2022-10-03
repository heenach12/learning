import collections


def maxSlidingWindow(nums, k):
    output= []
    q = collections.deque()
    l = r = 0
    while(r < len(nums)):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        if l > q[0]:
            q.popleft()
        if (r+1) >= k:
            output.append(nums[q[0]])
            l += 1
        r+= 1
    return output






    # q = []
    # res = []
    # for i, cur in enumerate(nums):
    #     while q and nums[q[-1]] <= cur:
    #         q.pop()
    #     q.append(i)
    #     if q[0] == i - k:
    #         q.pop(0)
    #     if i >= k - 1:
    #         res.append(nums[q[0]])
    # return res
    # output = []
    # q = collections.deque()
    # l = r = 0
    # while(r < len(nums)):
    #     while q and nums[q[-1]] < nums[r]:
    #         q.pop()
    #     q.append(r)
    #
    #     if l > q[0]:
    #         q.popleft()
    #     if (r+1) >=k:
    #         output.append(nums[q[0]])
    #         l += 1
    #     r += 1
    # return output

arr = [1,3,-1,-3,5,3,6,7]
j = maxSlidingWindow(nums=arr, k=3)
print(j)
