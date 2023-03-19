coins = int(input())
heads = 0
tails = 0
for i in range(coins):
    x = int(input())
    if x == 0:
        heads += 1
    else:
        tails += 1
if tails > heads:
    print(heads)
else:
    print(tails)
