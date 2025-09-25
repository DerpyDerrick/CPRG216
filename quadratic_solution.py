a = int(input("Please input Value a: "))
b = int(input("Please input Value b: "))
c = int(input("Please input Value c: "))

if(a == 0) :
    print("The equation you entered is linear. x =", -c/b)
else :
    if(b*b <= 4*a*c) :
        x1 = float (-b + ((b*b - 4*a*c)**0.5))/(2*a)
        x2 = float (-b - ((b*b - 4*a*c)**0.5))/(2*a)
        print("Solution one is:",x1,"Solution two is:",x2)
    else :
        print("No solution in the real domain. Entered values: a=",a,", b=", b, ", c=",c)
    