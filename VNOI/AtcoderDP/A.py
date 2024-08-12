'''https://oj.vnoi.info/problem/atcoder_dp_a'''
'''https://atcoder.jp/contests/dp/tasks/dp_a'''
n = int(input())
rocks = list(map(int, input().split()))
dp = [0] * (n)
dp[0] = 0
dp[1] = abs(rocks[0] - rocks[1])
for i in range(2, n):
    dp[i] = min(dp[i-1] + abs(rocks[i-1] - rocks[i]), dp[i-2] + abs(rocks[i-2] - rocks[i]))

print(dp[-1])

''' Editorial
Frog's initial position is at 0 (or 1, depends on your favourite).
Everytime he jumps, he can choose to jump 1 or 2 steps.
So we will traceback to see with the current rock i,
whether did he jump from rock i-1 or rock i-2 to get to rock i.

So we find the min of the cost from those 2 rocks.

Use dynamic programming, we have the frog's initial position is rock 0, 
so the cost to get there is 0, dp[0] = 0
Next, to get to rock 1, the only option is to jump from rock 0, so dp[1] = abs(rocks[1] - rocks[0])
'''