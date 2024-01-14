#list chứa các phần tử có kiểu bất kỳ/ có thể khác nhau/ trùng nhau
""" l=['xoài', 'cam', True, False, 1, 2 ,4.5,[3, 4, 5]] """
#Tạo list
#Hàm list
""" l=list('abc');
print(l) """
#Trực tiếp
""" l=[1, 2, 4, 'a', 'cam'] """
#Chỉ số: giống chuỗi (string)
#Cắt list: cắt chuỗi
""" l1=list('Programming in Python')
print(l1[::-1]) """
#Các phép toán
#So sánh(phải cùng kiểu)
""" l2=[1,2,3]
l3=[1,2,4] """
#Kiểm tra phần tử có/không có trong list
""" print('m' in l1) """
#Nối/cộng list
""" l1+l2 """
#Lặp lại nội dung
""" print(l2*3) """
#Duyệt list
#Giống string
#Duyệt theo nội dung
""" for e in l2:
    print(e, end=" ") """
#Duyệt theo chiều dài
""" for i in range(len(l2)):
    print(l2[i], end=" ") """
#Các hàm trên list
#Trả về chỉ số của 1 phần tử
""" print(l2.index(2)) """
""" print(l3.index(3)) """
""" print(l3.count(3))
print(l3.extend('hello')) """#thêm kí tự
""" print(l3.append('Sầu riêng'))
print(l3.insert(2, 'Đu đủ')) """
""" print(l3.reverse()) """#đảo ngược
""" l4=[1,2,7,6,5,4,3] """
""" print(l4.sort())
print(l4.sort(reverse=true)) """
""" print(l4.pop())#xóa phần tử cuối
print(l4.remove(7)) """#xóa phần tử đã chọn
#List cô động/rút gọn
#Tạo list gồm 100 số nguyên ngẫu nhiên chẵn từ 10 đến 1000
import random
l=[i for i in range(100) if random.randint(10, 1000) % 2 == 0 ]
#l=[random.randint(10,1000) for i in range(100) if i % 2 ==0]
l=[num for num in random.sample(range(10,1001,2), 100)]
print(l)