import math 
print('''1=square
2=circle
3=rectangle
4=triangle''')
list2=int(input("Enter Just One Number between(1-2-3-4):"))
a,b,c,d,e,h=1,1,1,1,1,1 #مقدار اولیه
#def condition(list):
if list2==1: #مربع
    a=int(input("Enter Number for square:"))
if list2==2: #دایره
    b=int(input("Enter Number for circle:"))
if list2==3: #مستطیل
    d=int(input("Enter Number rectangle:"))
    e=int(input("Enter Number rectangle:"))
if list2==4: #مثلث
    h=int(input("Enter Number h triangle:"))
    c=int(input("Enter Number triangle:"))
def get_func(list2,a,b,c,d,e,h):#محاسبه مساحت
    if list2==1:
        s=a*a
    if list2==2:
        s=(math.pi)*b
    if list2==3:
         s=d*e
    if list2==4:
         s=(h*c)/2
    return s
#y=condition(list2)
if list2<4: #اگر کوچیکتر 4 بود
    x=get_func(list2,a,b,c,d,e,h)
    print(x)
else:
    print("ERROR INPUT!!!!")
