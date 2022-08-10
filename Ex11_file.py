sf = open("song.txt", 'r')  #애국가
df = open("song2.txt", 'w')  #복사시키기: 없으면 만들고 있으면 덮어쓴다
while True:
    line = sf.readline()
    if not line: break
    if line == "\n":
        df.write("*" * 70)
        df.write("\n")
    else:
        df.write(line)
sf.close()
df.close()
