T = int(raw_input())
for i in range(0, T):
    A, B, C1 = [int(x) for x in raw_input().split(' ')]

    # initial number of chocolates
    no_wraps= answer = A/B
    while(no_wraps>=C1):
        answer =answer+no_wraps/C1
        no_wraps=no_wraps%C1 + no_wraps/C1

    print answer
