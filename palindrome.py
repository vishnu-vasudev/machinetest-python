n=input('Enter a string:')
s = ''
for i in n:
    s = i + s
if(n==s):
    print("Palindrome")
else:
    print("Not Palindrme")
