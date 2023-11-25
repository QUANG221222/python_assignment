con_giap = {
    0: "Khỉ",
    1: "Gà",
    2: "Chó",
    3: "Heo",
    4: "Chuột",
    5: "Bò",
    6: "Hổ",
    7: "Thỏ",
    8: "Rồng",
    9: "Rắn",
    10: "Ngựa",
    11: "Cừu"
    }

def xac_dinh_con_giap(nam):
    chi_so=nam % 12
    return con_giap[chi_so]

try:
    nam=int(input("Nhập năm sinh của bạn:  "))
    con_giap= xac_dinh_con_giap(nam)
    print(f"Con giáp theo Trung Quốc tương ứng với năm {nam} là : {con_giap}")
except ValueError:
    print("Nhập ko hợp lệ")
