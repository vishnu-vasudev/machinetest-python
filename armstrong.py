n=int(input("Enter the number:"))
t=n
s=0
while t>0:
    i=t%10
    s = s + (i**3)
    t=t//10
if s==n:
    print("Armsrong number")
else:
    print("Not Armstrong")