# Viết chương trình tính và in ra trung bình cộng của một dãy số được nhập vào từ bàn phím (không hạn chế số lượng số nhập vào).
# Qui ước số nhập có giá trị là 9999 là “số cầm canh” (nghĩa là nhập đến khi nhập số 9999 thì dừng việc nhập). 
print("Nhập dãy n (nhập 9999 để kết thúc)")
sum=0
count=0
while(True):
    num=int(input(" "))
    if(num==9999): break
    else: 
        sum+=num
        count+=1
if count>0:
    average=sum/count
    print("Gía trị trung bình của dãy là:",average)
else: print("Chưa có giá trị nào nhập")
    
