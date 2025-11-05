s=float (input(""))
m=float(1)
if  int(s)!=s:
    s=round(s+0.5)
if  s<=3:
    m=10
else:
    m=2*(s-3)+10                       
print(s,"千米，付费",m,"元。")