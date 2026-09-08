'''
https://yukicoder.me/problems/no/804
idsigmaさんの目の前には，A個の野菜とB個の肉があります。
彼は野菜が苦手ですが，健康のため，今日は野菜を少しでも食べようとしています。
idsigmaさんが野菜をあるx個数食べるためには，その個数のC
倍の肉を同時に食べる必要があります。しかし，idsigmaさんは今日は野菜と肉を合わせて
D個までしか食べられません。 idsigmaさんは今日，野菜を最大何個食べられるでしょうか？
'''
a, b, c, d = map(int, input().split())

e = d // (c + 1)
print(e if e <= a and e * c <= b else min(a, b // c))

'''
# another solution
a, b, c, d = map(int, input().split())

count = 0
for i in range(a + 1):
    if i * c > b or i + i * c > d:
        break
    else:
      count = i
print(count)

'''