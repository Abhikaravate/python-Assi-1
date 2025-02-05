def cal_total(M, N, diff):
    MOD = 10**9 + 7
    
    xor = 0
    for d in diff:
        xor ^= d
    
    if M % 2 == 0:
        return 0
    else:
        return xor % MOD

M, N = map(int, input().split())
diff = list(map(int, input().split()))

print(cal_total(M, N, diff))