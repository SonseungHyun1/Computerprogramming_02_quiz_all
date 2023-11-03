# 10주차 퀴즈
x = int(input("몇 층 트리를 만들어드릴까요?"))

for i in range(x):
    for j in range(x - i):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()
