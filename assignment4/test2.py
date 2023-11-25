def retangular(m,n):
    for i in range(m):
        for j in range(n):
          print("*", end="")#In **** mà không bị xuống dòng
        print()#Sao khi kết thúc sẽ xuống dòng
retangular(2,4)