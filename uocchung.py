a = int(input("a = "))
b = int(input("b = "))

def ucln(a,b):
    while a != b:
        if a > b:
            a = a - b;
        else:
            b = b - a;
    return a
print ("uoc chung lon nhat cua",a,"va",b,"la",ucln(a,b))