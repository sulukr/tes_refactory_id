input = [4,9,7,5,8,9,3]

counter = 0
num = len(input)
for i in range(num):
    for j in range(i+1, num):
        if input[i] > input[j]:
            temp = input[i]
            input[i] = input[j]
            input[j] = temp
            counter = counter + 1
            
print("sort = ", input)
print("jumlah swap = ", counter)
