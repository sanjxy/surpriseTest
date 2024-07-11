value=input("enter two numbers separated by an operator")
x,y,z=value.split()
if len([x,y,z])!=3:
    exit()



else:
#    x,y,z=value
    x=float(x)
    z=float(z)

if y=='+':
    result=x+z
elif y=='-':
    result=x-z
elif y=='*':
    result=x*z
elif y=='/':
    if z==0:
        print("zero not allowed")
        exit()
    else:
        result=x/z
else:
    print("not an operator")

print("result= ", result)
