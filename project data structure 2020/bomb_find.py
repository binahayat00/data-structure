from itertools import chain #import کردن chain
rw_clmn=input("Enter Two Number seprate with space:") #m,n
k=int(input("Enter Number Of Bomb:")) #k
bmb=""
l=int(0)
for p in range(k): #به تعدادی که بمب میخواد
    bmb+=input("Enter Two Number seprate with space:")
    bmb+=" "
row_column=rw_clmn.split(" ") #لیست درست کردن
bomb=bmb.split(" ") #لیست درست کردن
bomb+=[999999,999999] #عدد زیاد برای رفع ارور ایندکس
bomb.pop(-3) #یک اسپیس زیادی میذاره
bomb = [int(i) for i in bomb]  #تبدیل به اینتیجر برای مفایسه و سورت کردن
def sortSecond(val): # initializing string    
    return val[0] 
split_list=[]
for io in range(1,k+1): #تبدیل یک لیست
    split_list += [2*io]
# to perform custom list split 
temp = zip(chain([0], split_list), chain(split_list, [None])) # using itertools.chain() + zip() 
res = list(bomb[i : j] for i, j in temp) # initializing split index list
res.sort() 

l=0
for i in range(1,int(row_column[0])+1):
    for j in range(1,int(row_column[1])+1):
       # print(i,j,end=" ")
        #print(l,end="=") 
        if int(i)==int(res[l][0]) and int(j)==int(res[l][1]):
            print("*",end="   ") #نمایش بمب
            l+=1
        else:
            print(l,end="   ") # بمب نباشه
    print("")




#bomb_tuple=[]
#bomb_list=[]
#for count in range(0,2*k,2):
#    bomb_tuple=[int(bomb[count]),int(bomb[count+1])]
#    bomb_list+=bomb_tuple[0]
#res = [ (bomb_tuple[i], bomb_tuple[i+1]) for i, bomb_tuple[i+1] in bomb_list for bomb_tuple[i] in i ] 
#print(temp)
#print(res)
#print(row_column,bomb)