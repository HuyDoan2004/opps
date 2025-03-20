# #Câu 1: Tính giai thừa
# def giaithua(n):
#     if n == 0 or     n == 1:
#         return 1
#     return n*giaithua(n-1)
# print(giaithua(5))

# Phần 1: Recursion (Đệ quy)
# 1. Tính giai thừa
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# # 2. Tìm số Fibonacci thứ n
# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)

# # 3. Đảo ngược chuỗi
# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     return s[-1] + reverse_string(s[:-1])

# # 4. Tính tổng mảng
# def sum_array(arr):
#     if len(arr) == 0:
#         return 0
#     return arr[0] + sum_array(arr[1:])

# # 5. Kiểm tra chuỗi đối xứng (Palindrome)
# def is_palindrome(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return is_palindrome(s[1:-1])

# # Phần 2: Binary Search Tree (BST)
# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key

# class BST:
#     def __init__(self):
#         self.root = None

#     # 6. Chèn phần tử vào BST
#     def insert(self, key):
#         if self.root is None:
#             self.root = Node(key)
#         else:
#             self._insert(self.root, key)

#     def _insert(self, root, key):
#         if key < root.val:
#             if root.left is None:
#                 root.left = Node(key)
#             else:
#                 self._insert(root.left, key)
#         else:
#             if root.right is None:
#                 root.right = Node(key)
#             else:
#                 self._insert(root.right, key)

#     # 7. Tìm kiếm phần tử trong BST
#     def search(self, key):
#         return self._search(self.root, key)

#     def _search(self, root, key):
#         if root is None or root.val == key:
#             return root is not None
#         if key < root.val:
#             return self._search(root.left, key)
#         return self._search(root.right, key)

#     # 8. Duyệt cây theo thứ tự trung tố (Inorder Traversal)
#     def inorder_traversal(self):
#         result = []
#         self._inorder_traversal(self.root, result)
#         return result

#     def _inorder_traversal(self, root, result):
#         if root:
#             self._inorder_traversal(root.left, result)
#             result.append(root.val)
#             self._inorder_traversal(root.right, result)

# # Phần 3: Sorting Algorithms
# # 9. Cài đặt Quick Sort
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)

# # 10. So sánh thời gian chạy Bubble Sort và Merge Sort
# import time

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]

#         merge_sort(left_half)
#         merge_sort(right_half)

#         i = j = k = 0
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1

#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1

#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1

# def compare_sorting_algorithms():
#     import random
#     arr = [random.randint(0, 1000) for _ in range(1000)]

#     arr1 = arr.copy()
#     start = time.time()
#     bubble_sort(arr1)
#     bubble_time = time.time() - start

#     arr2 = arr.copy()
#     start = time.time()
#     merge_sort(arr2)
#     merge_time = time.time() - start

#     return f"Bubble Sort: {bubble_time:.6f}s, Merge Sort: {merge_time:.6f}s"

# # Chạy thử nghiệm
# if __name__ == "__main__":
#     print("Giai thừa của 5:", factorial(5))
#     print("Fibonacci thứ 6:", fibonacci(6))
#     print("Đảo ngược 'hello':", reverse_string("hello"))
#     print("Tổng mảng [1,2,3,4,5]:", sum_array([1, 2, 3, 4, 5]))
#     print("Chuỗi 'racecar' có đối xứng không?", is_palindrome("racecar"))

#     tree = BST()
#     for num in [50, 30, 70, 20, 40, 60, 80]:
#         tree.insert(num)
#     print("Duyệt cây theo thứ tự trung tố:", tree.inorder_traversal())
#     print("Tìm 40 trong BST:", tree.search(40))
#     print("Tìm 100 trong BST:", tree.search(100))

#     arr = [5, 3, 8, 1, 2, 7]
#     print("Quick Sort:", quick_sort(arr))
#     print(compare_sorting_algorithms())

