sum = 0

for i in range (1,101):
    sum += i
print (sum)    

for i in range (100, 0, -1):
    print(i)

number = int(input("Enter the number: "))
for i in range (11):
    #print(i*number)   
    print(f"{number}*{i}={number*i}")