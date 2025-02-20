#bài 1
def dao_nguoc_mang(mang):
    return mang[::-1]

print(dao_nguoc_mang([1, 2, 3, 4]))  # Output: [4, 3, 2, 1]



#bài 2
def so_lon_thu_hai(mang):
    mang_khac_nhau = list(set(mang))  
    mang_khac_nhau.sort(reverse=True)  
    return mang_khac_nhau[1] if len(mang_khac_nhau) > 1 else None

print(so_lon_thu_hai([4, 2, 6, 6, 1]))  # Output: 4


#Bài 3
def xoa_phan_tu_trung(mang):
    return list(set(mang))

print(xoa_phan_tu_trung([1, 2, 2, 3, 4, 4]))  # Output: [1, 2, 3, 4]



#Bài 4
class Nut:
    def __init__(self, du_lieu):
        self.du_lieu = du_lieu
        self.ke_tiep = None  

class DanhSachLienKet:
    def __init__(self):
        self.dau = None  

    def them(self, du_lieu):
        nut_moi = Nut(du_lieu)  
        if not self.dau:  
            self.dau = nut_moi
            return
        cuoi = self.dau
        while cuoi.ke_tiep:  
            cuoi = cuoi.ke_tiep
        cuoi.ke_tiep = nut_moi  

    def in_danh_sach(self):
        tam = self.dau
        while tam:
            print(tam.du_lieu, end=" -> ")
            tam = tam.ke_tiep
        print("None")

dslk = DanhSachLienKet()
dslk.them(1)
dslk.them(2)
dslk.them(3)
dslk.in_danh_sach()  # Output: 1 -> 2 -> 3 -> None



#Bài 5
import heapq

class HangDoiNhoNhat:
    def __init__(self):
        self.heap = []

    def them(self, gia_tri):
        heapq.heappush(self.heap, gia_tri)  

    def lay_nho_nhat(self):
        return heapq.heappop(self.heap) if self.heap else None  

heap = HangDoiNhoNhat()
heap.them(5)
heap.them(1)
heap.them(3)
print(heap.lay_nho_nhat())  # Output: 1



#Bài 6
def sap_xep_heap(mang):
    heapq.heapify(mang)  
    return [heapq.heappop(mang) for _ in range(len(mang))]  

print(sap_xep_heap([4, 1, 7, 3, 8, 5]))  # Output: [1, 3, 4, 5, 7, 8]



#Bài 7
class NganXep:
    def __init__(self):
        self.ngan_xep = []

    def them(self, phan_tu):
        self.ngan_xep.append(phan_tu)

    def lay_ra(self):
        return self.ngan_xep.pop() if self.ngan_xep else None

ngan_xep = NganXep()
ngan_xep.them(1)
ngan_xep.them(2)
print(ngan_xep.lay_ra())  # Output: 2



#Bài 8
from collections import deque

class HangDoi:
    def __init__(self):
        self.hang_doi = deque()

    def them(self, phan_tu):
        self.hang_doi.append(phan_tu)

    def lay_ra(self):
        return self.hang_doi.popleft() if self.hang_doi else None

hd = HangDoi()
hd.them(1)
hd.them(2)
print(hd.lay_ra())  # Output: 1



#Bài 9
class BangBam:
    def __init__(self):
        self.bang = {}

    def chen(self, khoa, gia_tri):
        self.bang[khoa] = gia_tri

    def lay(self, khoa):
        return self.bang.get(khoa, None)

bb = BangBam()
bb.chen("ten", "Alice")
print(bb.lay("ten"))  # Output: Alice



#Bài 10
from collections import Counter

def so_xuat_hien_nhieu_nhat(mang):
    dem = Counter(mang)
    return max(dem, key=dem.get)

print(so_xuat_hien_nhieu_nhat([1, 3, 3, 2, 1, 3, 4]))  # Output: 3
