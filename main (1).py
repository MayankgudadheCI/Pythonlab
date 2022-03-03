'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
n=int(input("enter n :"))
m=int(input("enter m : "))

for i in range(1,n+1):
    if(i%m==0):
      if(i%2==0):
          print("{0} is divisible by{1} and is even no.".format(i,m))
      else:
          print("{0} is divisible by {1} and is odd no.".format(i,m))

