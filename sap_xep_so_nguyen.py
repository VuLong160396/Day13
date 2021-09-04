my_list = []
def nhap_so_nguyen():
    for i in range(3):
        my_list.append(int(input(f'Nhập số nguyên thứ {i+1}: ')))

nhap_so_nguyen()
print(my_list)
my_list.sort()
print('List số nguyên sau khi sắp xếp tăng dần: ',my_list)


        