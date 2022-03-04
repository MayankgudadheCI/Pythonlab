
t=int(input())
while(t>0):
    n=int(input())
    arr=[int(x) for x in input().split()]
    count=0
    l=n//2
    if(arr[0]==1 and arr[l]==7):
        for i in range(l):
            if(arr[i]==arr[-i-1] and arr[i+1]-arr[i]<=1 and arr[i]<=7):
                count+=1
            else:
                print("no")
                break;
        if(count==l):
            print("yes")
    
    else:
        print("no")
    
    t=t-1
