# Bài 1: Quản lý Sách
# Yêu cầu:
# Viết chương trình quản lý sách với các yêu cầu sau:
# Tạo class Book có các thuộc tính: title (tên sách), author (tác giả), year (năm xuất bản).
# Viết phương thức display_info() để hiển thị thông tin sách.
# Tạo ít nhất 2 đối tượng Book và hiển thị thông tin của chúng.
# class Book:
#     def __init__(self, tensach, tacgia, nam):
#         self.tensach = tensach
#         self.tacgia = tacgia
#         self.nam = nam
    
#     def display_info(self):
#         print(f"Title: {self.tensach}, Author: {self.tacgia}, Year: {self.nam}")

# # Tạo đối tượng Book
# book1 = Book("A", "B", 2000)
# book2 = Book("C", "D", 2001)

# # Hiển thị thông tin sách
# book1.display_info()
# book2.display_info()
# .............................................................................
# Bài 2: Quản lý tài khoản ngân hàng
# Yêu cầu:
# Tạo class BankAccount với các thuộc tính:
# account_number (số tài khoản, chỉ đọc)
# balance (số dư, mặc định là 0)
# Viết các phương thức:
# deposit(amount): Nạp tiền vào tài khoản.
# withdraw(amount): Rút tiền khỏi tài khoản (nếu số dư đủ).
# get_balance(): Trả về số dư hiện tại.
# Tạo một đối tượng tài khoản ngân hàng, thực hiện một số giao dịch và hiển thị số dư.
# class BankAccount:
#     def __init__(self, account_number, balance=0):
#         self.__account_number = account_number  # Số tài khoản chỉ đọc
#         self.balance = balance
    
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Đã nạp {amount} vào tài khoản. Số dư hiện tại: {self.balance}")
#         else:
#             print("Số tiền nạp phải lớn hơn 0.")
    
#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"Đã rút {amount}. Số dư còn lại: {self.balance}")
#         else:
#             print("Số dư không đủ hoặc số tiền rút không hợp lệ.")
    
#     def get_balance(self):
#         return self.balance
    
#     def get_account_number(self):
#         return self.__account_number

# # Tạo tài khoản ngân hàng
# account = BankAccount("1234567890", 1000)

# # Thực hiện giao dịch
# account.deposit(500)
# account.withdraw(300)
# account.withdraw(1500)  # Sẽ báo lỗi do số dư không đủ

# # Hiển thị số dư
# print(f"Số dư cuối cùng: {account.get_balance()}")
#................................................................................
# Bài 3: Kế thừa trong OOP (Inheritance)
# Yêu cầu:
# Tạo class Person với các thuộc tính: name, age.
# Tạo class Student kế thừa từ Person, có thêm thuộc tính student_id và phương thức study().
# Tạo một đối tượng sinh viên và gọi các phương thức của nó.
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def introduce(self):
#         print(f"My name is {self.name} and I am {self.age} years old.")

# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id
    
#     def study(self):
#         print(f"Student {self.name} with ID {self.student_id} is studying.")

# # Tạo một đối tượng sinh viên
# student = Student("Huy", 23, "22110132")

# # Gọi phương thức của lớp cha và lớp con
# student.introduce()
# student.study()
# ...................................................................
# Bài 4: Quản lý phương tiện giao thông
# Yêu cầu:
# Tạo class Vehicle có các thuộc tính: brand, model, year.
# Tạo các class Car và Bike kế thừa từ Vehicle:
# Car có thêm thuộc tính num_doors (số cửa).
# Bike có thêm thuộc tính type (loại xe: road, mountain,...).
# Cài đặt phương thức display_info() trong mỗi lớp.
# Tạo đối tượng từ mỗi lớp và gọi phương thức display_info().
# class Vehicle:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
    
#     def display_info(self):
#         print(f"Vehicle: {self.brand} {self.model}, Year: {self.year}")

# class Car(Vehicle):
#     def __init__(self, brand, model, year, num_doors):
#         super().__init__(brand, model, year)
#         self.num_doors = num_doors
    
#     def display_info(self):
#         print(f"Car: {self.brand} {self.model}, Year: {self.year}, Doors: {self.num_doors}")

# class Bike(Vehicle):
#     def __init__(self, brand, model, year, bike_type):
#         super().__init__(brand, model, year)
#         self.bike_type = bike_type
    
#     def display_info(self):
#         print(f"Bike: {self.brand} {self.model}, Year: {self.year}, Type: {self.bike_type}")

# # Tạo đối tượng từ mỗi lớp
# car = Car("Toyota", "Camry", 2022, 4)
# bike = Bike("Giant", "Escape 3", 2021, "road")

# # Gọi phương thức display_info()
# car.display_info()
# bike.display_info()





