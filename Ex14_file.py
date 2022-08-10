sf = open("song.txt", 'r')

# 한줄씩 리스트로 읽기
lines = sf.readline()
print(type(lines), lines)

for line in lines:
    print(line.strip())
sf.close()

print("*" * 80)

# 한번에 스트링으로 모두 읽기
sf = open("song.txt", 'r')  #애국가
print(sf.read())
sf.close()
