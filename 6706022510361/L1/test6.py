print("***Calculate the sum between start and stop number***")
start = int(input("Enter the start number :"))
end = int(input("Enter the end number :"))
list =[]
for i in range(start,end+1):
    list.append(i)

print("The sum from ",start," to ",end," is : ",sum(list))