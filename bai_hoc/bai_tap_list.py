""" N=int(input("Enter N="))
l=[]
for i in range(N):
    num=int(input(f"A[{i}]="))
    l.append(num)
l.reverse()
print(l)
element=int(input("Enter new element:"))
l.append(element)
print(l) """
#a: Code:
n = int(input("Nhập độ dài danh sách: "))

numbers = []
for i in range(n):
    value = float(input("Nhập phần tử thứ %d: " % (i+1)))
    numbers.append(value)

numbers.reverse()

print("Danh sách đảo ngược là: ", numbers)
#d:
""" Duyệt từng phần tử trong danh sách bằng vòng lặp for
Kiểm tra nếu phần tử đó bằng X cần tìm
Thêm chỉ số i (vị trí của phần tử) vào danh sách positions
Sau khi duyệt xong, in ra danh sách các vị trí """
#d: Code
numbers = [1, 5, 2, 5, 9, 5, 2]

x = int(input("Nhập phần tử cần tìm: "))

positions = []
for i in range(len(numbers)):
    if numbers[i] == x:
        positions.append(i)

print("Vị trí xuất hiện của", x, "là: ", positions)
#f:
""" Cách làm:

Duyệt danh sách bằng vòng lặp while với biến đếm i
Nếu gặp phần tử bằng X thì dùng remove() để xóa nó
Nếu không phải thì tăng i lên 1 để duyệt tiếp
Kết thúc vòng lặp khi i == độ dài danh sách
Lưu ý:

Không thể dùng for để duyệt và xóa cùng lúc vì danh sách sẽ bị thay đổi
Phải dùng while để kiểm soát chỉ số i """
numbers = [1, 5, 2, 5, 9, 5, 2]
