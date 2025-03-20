# import pandas as pd
# print("Pandas version:", pd.__version__)
# ................................................
# import matplotlib.pyplot as plt

# # Dữ liệu trục x và y
# x = list(range(-10, 11))  # Danh sách từ -10 đến 10
# y = [i**2 for i in x]  # Bình phương từng phần tử trong x

# # Vẽ đồ thị
# plt.plot(x, y, marker='o', linestyle='-')

# # Thêm tiêu đề và nhãn trục
# plt.title("Đồ thị của y = x^2")
# plt.xlabel("Trục x")
# plt.ylabel("Trục y")

# # Hiển thị đồ thị
# plt.show()
# ....................................................
# numbers = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
# print(numbers)
# ............................................................
# def is_prime(n):
#     if n < 2:
#         return False
#     return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

# # Tạo generator expression
# prime_gen = (i for i in range(1, 21) if is_prime(i))

# # In từng số nguyên tố bằng next()
# try:
#     while True:
#         print(next(prime_gen))
# except StopIteration:
#     print("Hết số nguyên tố trong khoảng 1 đến 20")

