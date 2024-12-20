m = int(input("กรอกจำนวนเงินที่กู้ : "))

if m <= 1000: 
    interest_rate = 10
elif m <= 10000: 
    interest_rate = 5 
else :
    interest_rate = 2

sum = (m * interest_rate)/100
total = m + sum

print (total, sum)