n=int(input("Enter the number of terms:"))
i=0
a=0
b=1
if n<=0:
    print("Enter a positive number")
elif n==1: 
    print("Fibonacci series:")
    print(a)
else:
    print("Fibonacci series:")
    while i<n:
        print(a)
        c=a+b
        a=b
        b=c
        i+=1