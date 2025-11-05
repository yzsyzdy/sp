a=float(input(""))
b=float(input(""))
c=float(input(""))
#若构成三角形，则求三角形面积
if a+b>c and a+c>b and b+c>a:                                                            
    p=(a+b+c)/2
    area=(p*(p-a)*(p-b)*(p-c))**0.5
    print("三角形面积为：",area)
else:
    print("输入的三条边，不能构成三角形！")