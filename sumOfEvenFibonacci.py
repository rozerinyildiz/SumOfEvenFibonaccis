def sumOfEvenFibonacci(limit):
    sum=0
    first=1
    second=2
    while(first<limit):
        if first%2==0:
            sum= sum + first
        temp=first
        first=second
        second= temp+second
    return sum
print(sumOfEvenFibonacci(4000000))

