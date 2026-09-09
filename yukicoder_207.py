"""
 https://yukicoder.me/problems/no/207
"""
#Checkers for A,B's range, value and distance
def input_range_checker(x):
    if x > 2000000000 or x < 1:
        print(f"\n入力値が範囲外です。\n1～{2000000000:,}の範囲内で再入力してください。\n")
        y = False
    else:
        y = True
    return y

def input_value_checker(a, b):
    if a >= b:
        print("\nA以上の整数Bを再入力してください。\n")
        y = False
    else:
        y = True
    return y

def input_distance_checker(a, b):
    if b - a >= 100:
        print("\nAとBの差が大きすぎます。\n差が100以下の値を再入力してください。\n")
        y = False
    else:
        y = True
    return y


#Start of the program
print("正整数A、Bの値を入力してください。（A≤B）\n")

valid_a = False
valid_b = False

valid_b1 = False    #valid_b_step1~3
valid_b2 = False
valid_b3 = False


while valid_a == False:
    a = int(input("A: "))
    valid_a = input_range_checker(a)
    if valid_a == True:
        break
    else:
        continue
while valid_b == False:
    b = int(input("B: "))        

    valid_b1 = input_range_checker(b)
    valid_b2 = input_value_checker(a, b)
    valid_b3 = input_distance_checker(a, b)
    valid_b = all([valid_b1, valid_b2, valid_b3])

    if valid_b == True:
        break
    else:
        continue

num = set()
for i in range(a, b + 1):
    if i % 3 == 0 or '3' in str(i):
        num.add(i)

print(f"\n{a:,}以上{b:,}以下の整数のうち、3の倍数および3の付く数は以下の通りです。")
for i in sorted(num):
    print(i)