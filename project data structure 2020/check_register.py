import re     #writen by AmirReza Zare
class checkregister: #کلاس تایید کننده اطلاعات ورودی که توسط کاربر وارد میشود 
    def __init__(self,name,family,mail,nation_code,number_mobile,username,password): #تابع شی سازنده
        self._name         = name
        self._family       = family
        self._mail         = mail
        self._nation_code  = nation_code
        self._number_mobile= number_mobile
        self._username     = username
        self._password     = password
    #----------------------------------------------------------------------------------------------------------------------------------------
    def checkname(self):#تابع چک کردن نام
        x2 = re.findall("[a-zA-Z]{1,21}", self._name) #فقط حروف انگلیسی و یک تا 21 حرف بدون فاصله 
        x3 =re.findall(".{1,21}", self._name) # 21ای 21 ای جدا کن 
        if len(x2)==1 and x2==x3: #اگر برابر بود درسته
            return True
        else:
            return False
    #-----------------------------------------------------------------------------------------------------------------------------------------
    def checklastname(self):#تابع چک کردن فامیل
        y2 = re.findall("[a-zA-Z]{1,30}", self._family) #فقط حروف انگلیسی و یک تا 30 حرف بدون فاصله 
        y3 =re.findall(".{1,30}", self._family) # 30ای 30 ای جدا کن 
        if len(y2)==1 and y2==y3: #اگر برابر بود درسته
            return True
        else:
            return False
    #-----------------------------------------------------------------------------------------------------------------------------------------
    def checkemail(self):#تابع چک کردن ایمیل 
        if not re.search(r'\b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}\b',self._mail): #check for email a@b.com
            return False
        else:
            return True
    #-----------------------------------------------------------------------------------------------------------------------------------------
    def check_code(self):#تابع چک کردن کد ملی
        if not re.search(r'^\d{10}$', self._nation_code):#check for that 10number
            return False
        check = int(self._nation_code[9])
        s = sum([int(self._nation_code[x]) * (10 - x) for x in range(9)]) % 11 #مجموع همه ارقام*جایگاه به جز رقم آخر تقسیم بر 11 را حساب کن
            #اگر کوچک تر از 2  شد خودش و بزرگتر شد از 11 کم کن باید برابر رقم آخر باشد درغیراین صورت فالس برگردان
        return (s < 2 and check == s) or (s >= 2 and check + s == 11)
    #-----------------------------------------------------------------------------------------------------------------------------------------
    def checkmobile(self):#تابع چک کردن موبایل
        if not re.search(r'^09\d{9}$', self._number_mobile):#check for that 11number and start with 09
            return False
        else:
            return True
    #-----------------------------------------------------------------------------------------------------------------------------------------
    def checkusername(self):#تابع چک کردن نام کاربری
        if not re.search(r'^[\w|@]{6,50}$', self._username):#check for that 6 to 50 character and "_" and "@"
            return False
        if self._username =="Username" or self._username =="Admin":
            return False
        else:
            return True
    #-----------------------------------------------------------------------------------------------------------------------------------------
    def password_check(self):#تابع چک کردن پسورد ساده
        if not re.search(r'^[\d][#|$|@|&|%|\w]{8,50}$', self._password):#check for that 8 to 50 character and "_" and "@"and"#"and"$"and"&"and"%"
            return False
        else:
            return True
    #-----------------------------------------------------------------------------------------------------------------------------------------
    def checkpassword(self): #تابع چک کردن پسورد امنیتی تر 
        SpecialSym =['$', '@', '#', '%'] 
        val = True
        if len(self._password) < 8: 
            print('length should be at least 8') #حداقل 8
            val = False
        if len(self._password) > 50: 
            print('length should be not be greater than 50') #حداکثر 50
            val = False  
        if not any(char.isdigit() for char in self._password): #عدد نداره فالس
            print('Password should have at least one numeral') 
            val = False   
        if not any(char.isupper() for char in self._password): #حرف بزرگ نداره فالس
            print('Password should have at least one uppercase letter') 
            val = False  
        if not any(char.islower() for char in self._password): #حرف کوچیک نداره فالس
            print('Password should have at least one lowercase letter') 
            val = False   
            #اختیاری
        #if not any(char in SpecialSym for char in password): #کاراکتر خاص فالس
            #('Password should have at least one of the symbols $@#%') 
        # val = False
        if val: 
            return val 
    #-----------------------------------------------------------------------------------------------------------------------------------------
name = input("Enter your Name:") #گرفتن نام
family = input("Enter your Family:") #گرفتن فامیلی
mail= input("Enter your Email:") #گرفتن ایمیل
nation_code=input("Enter your Nation code:") #گرفتن کد ملی
number_mobile=input("Enter your Number Mobile:") #گرفتن موبایل
username=input("Enter your Username:") #گرفتن نام کاربری
password=input("Enter your Password:") #گرفتن پسورد
cc = checkregister(name,family,mail,nation_code,number_mobile,username,password) #ساخت شی
x1=checkregister.checkname(cc)
x2=checkregister.checklastname(cc)
x3=checkregister.checkemail(cc)
x4=checkregister.check_code(cc)
x5=checkregister.checkmobile(cc)
x6=checkregister.checkusername(cc)
x7=checkregister.checkpassword(cc)
#print(x1,x2,x3,x4,x5,x6,x7)
if x1==True and x2==True and x3==True and x4==True and x5==True and x6==True and x7==True: #اگر همه ی شروط برفرار بود و ورودی ها تایید بود 
    print("register OK") 
else: #اگر ورودی تایید نبود
    print("register ERROR") 
    #writen by AmirReza Zare