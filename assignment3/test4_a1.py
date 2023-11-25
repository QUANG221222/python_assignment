def tong_chu_so(num):
    chu_so_le=str(num)
    tong=0
    for num in chu_so_le:
        tong+=int(num)
    return tong

try:
    n=int(input("Nhập N: "))
    tong_tat_ca=tong_chu_so(n)
    print("Tổng các chữ số:  ",tong_tat_ca)
except ValueError:
    print("Nhập ko hợp lệ")
    

