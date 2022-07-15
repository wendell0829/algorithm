"""
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

示例 1:
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

提示：
0 <= num < 2^31

"""

class Solution:
    def translateNum(self, num: int) -> int:
        i = 1
        n = num
        while n>=10:
            n = n//10
            i *= 10
        return self.process(num, i)

    def translateNum2(self, num: int) -> int:
        i = 1
        n = num
        while n>=10:
            n = n//10
            i += 1
        # print(i)
        return self.process2(num, i)

    def process(self, num:int, i:int):
        # num: 待翻译的整数
        # i:num对应的整十倍数,方便对num取余
        # i==1,转化到了最后1位
        # i==0,最后1位已被转化
        if i <= 1:
            return 1
        # 提取当前位
        m = num // i
        # m==1,有2种转化方式,1作为'a'或1和后边1位一起转
        if m == 1:
            next_num = num % i
            next_i = i // 10
            return self.process(next_num, next_i) + self.process(next_num%next_i, next_i//10)
        # m==2,有2种转化方式,2作为'b'或2和后边1位一起转,但要注意后边1位0-6时才可以
        elif m == 2:
            next_num = num%i
            next_i  = i//10
            next_m = next_num//next_i
            if next_m<6:
                return self.process(next_num, next_i) + self.process(next_num%next_i, next_i//10)
            else:
                return self.process(next_num, next_i)
        # 其他情况,该位单独转
        else:
            return self.process(num%i, i//10)

    def process2(self,num:int, i:int):
        dp = [0] * (i+1)
        dp[0] = 1
        dp[1] = 1
        j = 2
        pre_m = num%10
        while j<=i:
            num = num // 10
            m = num % 10
            if m == 1:
                dp[j] = dp[j-1]+dp[j-2]
            elif m == 2:
                if pre_m < 6:
                    dp[j] = dp[j-1]+dp[j-2]
                else:
                    dp[j] = dp[j-1]
            else:
                dp[j] = dp[j-1]
            pre_m = m
            j += 1
        return dp[i]


s = Solution()
print(s.translateNum(18), s.translateNum2(18))
print(s.translateNum(218), s.translateNum2(218))
print(s.translateNum(2218), s.translateNum2(2218))
print(s.translateNum(12218), s.translateNum2(12218))
print(s.translateNum(25), s.translateNum2(25))
print(s.translateNum(26), s.translateNum2(26))
# print(s.translateNum(218))
# print(s.translateNum(2218))
# print(s.translateNum(12218))
# print(s.translateNum(25))
# print(s.translateNum(26))
# print(s.translateNum(11))
# print(s.translateNum(506))
# print(s.translateNum(1068385902))