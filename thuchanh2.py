# #Câu 1:
# def songuyen():
#     a = int(input("Nhập một số nguyên: ")) 
#     if a == 0:
#         print(a, "là số 0")
#     elif a%2 == 0:
#         print(a, "là số nguyên dương")
#     else:
#         print(a, "là số nguyên âm")

# songuyen()

# #Câu 2:
# def tuoi():
#     a = int(input("nhập vào tuổi của người đó: "))
#     if a > 18:
#         print("Adult")
#     else:
#         print("Minor")
# tuoi()

# #Câu 3:
# def songuyen1():
#     a = float(input("nhập vào một số thực: "))
#     print(int(a))
# songuyen1()

# #Câu 4:
# def nhapsonguyen():
#     while True:  # Lặp vô hạn để nhập số nguyên từ người dùng
#         try:
#             a = int(input("Nhập số nguyên: "))  # Nhập số nguyên
#             print("Bạn đã nhập:", a)
#             break  # Thoát vòng lặp nếu nhập đúng
#         except ValueError:
#             print("Please enter a valid number")

# nhapsonguyen()

# #Câu 5:
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):  # Chỉ kiểm tra đến căn bậc hai của n
#         if n % i == 0:
#             return False
#     return True

# # Nhập số từ người dùng và kiểm tra
# a = int(input("Nhập một số nguyên: "))
# if is_prime(a):
#     print(a, "là số nguyên tố")
# else:
#     print(a, "không phải là số nguyên tố")

# #Câu 6:
# def dayso():
#     a =[1,3,5,7,9]
#     print(len(a))
# dayso()

# #Câu 7:
# def maxmin():
#     a = [1,5,3,5,2,6]
#     print(max(a))
# maxmin()

# #Câu 8:
# numbers = [2, 4, 6, 8]  # Danh sách ban đầu
# numbers.append(10)  # Thêm số 10 vào cuối danh sách
# print("Danh sách sau khi thêm số mới:", numbers)

#Câu 9:
# names = ["An", "Bình", "Châu", "Dũng", "Hà"]
# for name in names:
#     print(name)

#Câu 10:
students = {
    "An": 18,
    "Bình": 20,
    "Châu": 19,
    "Dũng": 22,
    "Hà": 21
}

max_age = max(students.values())  # Tìm tuổi lớn nhất
for name, age in students.items():
    if age == max_age:
        print(f"Sinh viên lớn tuổi nhất: {name}, {age} tuổi")

#Câu 11:    
grades = {
    "An": 8.5,
    "Bình": 7.0,
    "Châu": 9.0,
    "Dũng": 6.5,
    "Hà": 7.8
}

student_name = input("Nhập tên sinh viên: ")
if student_name in grades:
    print(f"Điểm của {student_name} là {grades[student_name]}")
else:
    print("Sinh viên không tồn tại.")


#Câu 12:
for i in range(1, 11):
    print(i, end=" ")

#Câu 13:
i = 0
while i <= 20:
    print(i, end=" ")
    i += 2


