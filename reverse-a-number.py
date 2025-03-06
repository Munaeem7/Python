num = int(input("Enter a Number? " ))
ans = 0
while(num > 0):
    mod = num % 10
    num = num // 10
    ans = ans * 10 + mod
    
print(ans)