def alt(s,t):
    le = len(s)
    i = 0
    n = 1
    for index in range(le//2):     
        print(s[i], end = '')
        print(t[n], end = '')
        i += 2
        n += 2
        
    if le%2 != 0:
        print(s[-1])
    

s = "abcdefg"
t = "zzzzzzz"
alt(s,t)