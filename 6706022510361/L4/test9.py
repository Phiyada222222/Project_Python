start = int(input("Enter :"))
end =  int(input("Enter :"))

sum = []
for i in range(start,end):
    if i % 3 == 0 and i != start:
        sum.append(i)
print(sum)