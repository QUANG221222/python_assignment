# Hàm tính tổng các chữ số của một số
def tinh_tong_cac_chu_so(so):
    # Chuyển số thành chuỗi để lặp qua từng chữ số
    chuoi_so = str(so)
    # Khởi tạo tổng bằng 0
    tong_chu_so = 0
    # Lặp qua từng chữ số và cộng vào tổng
    for chu_so in chuoi_so:
        tong_chu_so += int(chu_so)
    return tong_chu_so

# Chương trình chính
try:
    # Nhập số từ người dùng
    N = int(input("Nhập vào một số nguyên: "))
    # Tính tổng các chữ số sử dụng hàm
    ket_qua = tinh_tong_cac_chu_so(N)
    # Hiển thị kết quả
    print("Tổng các chữ số của", N, "là", ket_qua)
except ValueError:
    print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên hợp lệ.")
