lst=[]
n=int(input("Enter the number of elements:"))
print("Enter the elements:")
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
largest=max(lst[0],lst[1])
seclargest=min(lst[0],lst[1])
for i in lst:
    if i>largest:
        seclargest=largest
        largest=i
    elif i>seclargest and i!=largest:
        seclargest=i
print("Second largest element:" , seclargest)
