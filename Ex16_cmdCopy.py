import sys  # 모듈 사용

if len(sys.argv) != 3:
    print("사용형식이 잘못되었습니다")
    print("사용형식]>python {}원본파일명 사본파일명".format(__file__))
else:  #Ex16_cmdCopy.py song.txt song4.txt
    sf = open(sys.argv[1], 'r')
    df = open(sys.argv[2], 'w')
    df.write(sf.read())
    sf.close()
    df.close()
    print("{{{0}}}을 {{{1}}}로 복사했습니다".format(sys.argv[1], sys.argv[2]))