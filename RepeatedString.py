def repeatedString(s, n):
    cnt =0
    quotient = int(n/len(s))
    reminder = n%len(s)
    for x in s:
        if x=='a':
            cnt+=1
    if reminder==0:
        return cnt*(quotient)
    else:
        subcount = 0
        for y in s[:reminder]:
            if y =='a':
                subcount+=1
        return cnt*(quotient) + subcount
