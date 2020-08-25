# Memoized Recursive Solution (Top Down DP Solution)
def climbStairs(n):
  hashmap = {}

  def helper(n):
    if n in hashmap:
      return hashmap[n]
    val = 0
    if n == 0:
      val = 1
    elif n < 0:
      val = 0
    else:
      val = helper(n - 1) + helper(n - 2)
    hashmap[n] = val
    return val
  
  return helper(n)

# Bottom Up DP Solution
def climbStairsDP(n):
  if n == 1:
    return n
  
  dp = []
  dp.append(1)
  dp.append(2)
  for i in range (2, n):
    dp.append(dp[i - 1] + dp[i - 2])
  
  return dp[n - 1]

print(climbStairsDP(3))
print(climbStairs(3))