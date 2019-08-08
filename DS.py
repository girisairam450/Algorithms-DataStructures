import os
from RepeatedString import repeatedString

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    n = int(input())
    result = repeatedString(s, n)
    print(str(result))
    # fptr.write(str(result) + '\n')
    # fptr.close()
