"""
 https://yukicoder.me/problems/no/207

A以上B以下の整数のうち、3の倍数および3の付く数を、
小さい順に出力してください。なお、「3の付く数」とは、
10進数表記にした時、少なくとも1つの桁が3であるような数のことです。
"""
#Checkers for A,B's range, value and distance
def Input_range_checker(x):
    if x > 2000000000 or x < 1:
        print(f"\n入力値が範囲外です。\n1～{2000000000:,}の範囲内で再入力してください。\n")
        y = False
    else:
        y = True
    return y

def Input_value_checker(x):
    if a >= b:
        print("\nA以上の整数Bを再入力してください。\n")
        y = False
    else:
        y = True
    return y

def Input_distance_checker(x):
    if b - a >= 100:
        print("\n2AとBの差が大きすぎます。\n差が100以下の値を再入力してください。\n")
        y = False
    else:
        y = True
    return y


#Start of the program
print("正整数A、Bの値を入力してください。（A≤B）\n")

valid_A = False
valid_B = False

while valid_A == False:
    a = int(input("A: "))
    valid_A = Input_range_checker(a)
    if valid_A == True:
        break
    else:
        continue
while valid_B == False:
    b = int(input("B: "))        
    Input_range_checker(b)
    Input_value_checker(b)
    valid_B = Input_distance_checker(b)
    if valid_B == True:
        break
    else:
        continue

