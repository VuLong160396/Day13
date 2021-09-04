my_string = input('Mời nhập chuỗi: ')
def lenght_str(txt):
    result = 0
    for i in txt:
        result += 1
        # print(i,type(i))
    return result
print('Độ dài chuỗi vừa nhập: ',lenght_str(my_string))
