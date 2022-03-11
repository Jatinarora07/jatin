#(a)Sum of first n odd natural numbers

m = int(input("Enter the number: "))
sum=0
i=1
while(i<=m):
    sum=sum+i
    i=i+2
print("sum of odd numbers=",sum)


#(b) Sum of first n even natural numbers

n = int(input("Enter the number: "))
sum=0
i=2
while(i<=n):
    sum=sum+i
    i=i+2
print("sum of even numbers=",sum)

#(c)1, 2, 4, 3, 5, 7, 9, 6, 8, 10, 11, 13.. till n-th term

def findSum(num):
    sumo = 0
    sume = 0
    x = 1
    cur = 0
    ans = 0
    while (num > 0):
        inc = min(x, num)
        num -= inc
        if (cur == 0):
            ans = ans + odd_sum(sumo + inc) - odd_sum(sumo)
            sumo += inc
        else:
            ans = ans + even_sum(sume + inc) - even_sum(sume)
            sume += inc
        x *= 2
        cur ^= 1
    return(ans)
    print(findSum(n))