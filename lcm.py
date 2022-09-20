import math


def lcm_multinum(*nums):
    """여러 자연수의 최대 공배수를 반환
    """
    nums = list(map(int,*nums))
    GCD = nums[0]
    LCM = nums[0]
    for i in range(1, len(nums)):
        # i번째 수까지의 최대공약수는 'i-1번째 수까지의 최대공약수'와 'i번째 수'의 최대공약수
        GCD = math.gcd(GCD, nums[i])
        # i번째 수까지의 최소공배수는 'i-1번째 수까지의 최소공배수'와 'i번째 수'의 최소공배수
        tmpGCD = math.gcd(LCM, nums[i])
        LCM = LCM * nums[i] // tmpGCD
    return LCM
