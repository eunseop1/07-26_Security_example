for i in range(2, 10):
    print("\n{0}단".format(i))
    for j in range(1, 10):
        print("{0} x {1} = {2}".format(i, j, i * j))

result = [x * y for x in range(2, 10) for y in range(1, 10)]  # 이중 for문, 앞에 있는게 바깥의 for문이고 두번째가 안쪽의 for문
print(result)
for index in range(len(result)):
    print("{0:4}".format(result[index]), end="")
    if (index + 1) % 9 == 0: print()
