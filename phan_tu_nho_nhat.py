my_list = []
n = int(input('Nhập vào số phần tử của mảng: '))
if n > 0:
    for i in range(n):
        my_list.append(int(input(f'phần tử thứ {i+1}: ')))

result  = my_list[0]      
for i in my_list:
    if int(i) < result:
        result = int(i)
print('Phần tử nhỏ nhất của mảng: ',result)