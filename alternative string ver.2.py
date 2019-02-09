def alt(s,t):
    le = len(s)
    i = 0
    n = 1
    try:
        for index in range(le//2 + 1):     
            print(s[i], end = '')
            print(t[n], end = '')
            i += 2
            n += 2
    except IndexError:
        print()
        


s = "abcdefg"
t = "zzzzzzz"
alt(s,t)