my_list=[]
param=''
str=input('Enter Anything: ')
param=input('Give Parameter: ')
if param=='':
    param=' '
str=str+'\n'
s=''
i=0
while i<len(str):
    if str[i]!=param and str[i]!='\n':
        s=s+str[i]
    elif str[i]==param:
        my_list.append(s)
        s=''
        if str[i+1]==' ':
            i=i+1
    elif str[i]=='\n':
        my_list.append(s)
    i=i+1

#my_list contains list of elements seprated with reference to Parameter.
print(my_list)