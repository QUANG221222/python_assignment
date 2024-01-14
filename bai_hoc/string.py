""" chuoi=input("Nhập chuỗi:")
tu_khoa=chuoi.replace('.',' ').split()
l=[]
for word in tu_khoa:
    if word not in l:
        l.append(word)
for word in l:
    print(f"{word}: {tu_khoa.count(word)}") """
""" s1="Covid"
s2="1/12/2019"
print("Same" if(len(s1)==len(s2)) else "not")
s2=s2.split('/')
print(s2[1]) """
s="nguyễn nhậT quang"
print(s.capitalize())
print(s.swapcase())
print(s.title())