for i in range (1,101):
    a = i%3
    b = i%5
    if a == 0 and b != 0:
        print("Foo", end = " ")
    elif b == 0 and a != 0:
        print("Bar", end = " ")
    elif b == 0 and a == 0:
        print("FooBar", end = " ")
    else:    
        print(i, end = " ")