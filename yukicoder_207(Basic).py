def input_checker_1(x, y):
    if x > y:
        print("\nA≤Bが必須です。AとBを再入力してください。\n")
        return False
    return True

def input_checker_2(x, y):
    if x < 1 or y > 2000000000 or y - x >= 100:
        print(f"""\n入力値が範囲外です。\n1～{2000000000:,}の範囲内で、
        差が100以下のA、Bの値を再入力してください。\n""")
        return False
    return True

def input_func():
    input_num = [int(i) for i in input().split()]
    a = input_num[0]
    b = input_num[1]
    return [a, b]


print("整数A、Bの値を入力してください。\n半角スペースで区切ってください。（A≤B）\n")

input_checked = False
valid_ab = input_func()
a = valid_ab[0]
b = valid_ab[1]
result = []

#入力値チェック
input_checked = input_checker_1(a, b)

if input_checked == False:
    a, b = input_func()
else:
    input_checked = input_checker_2(a, b)
    if input_checked == False:
        a, b = input_func()


#3の倍数および3の付く数を抽出
print(f"\n{a:,}以上{b:,}以下の整数のうち、3の倍数および3の付く数は以下の通りです。")
for i in range(a, b + 1):
    if i % 3 == 0 or '3' in str(i):
        result.append(i)
for i in sorted(result):
    print(i)