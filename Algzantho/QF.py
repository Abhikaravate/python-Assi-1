from collections import deque

def journey(t, cases):
    results = []
    for _ in range(t):
        n, k = cases[_][:2]
        arr = cases[_][2]
        
        dp = [0] * n
        dp[0] = arr[0]
        
        dq = deque()
        dq.append(0)
        
        for i in range(1, n):
            while dq and dq[0] < i - k:
                dq.popleft()
            
            dp[i] = dp[dq[0]] + arr[i]
            
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
            
            dq.append(i)
        
        results.append(dp[-1])
    
    return results

t = int(input())
cases = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    cases.append((n, k, arr))

results = journey(t, cases)
for res in results:
    print(res)
