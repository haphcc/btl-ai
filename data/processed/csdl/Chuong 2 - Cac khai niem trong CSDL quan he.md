# HỌC VIỆN NGÂN HÀNG
BANKING ACADEMY OF VIETNAM

# CHƯƠNG 2
# CÁC KHÁI NIỆM TRONG CSDL QUAN HỆ


<!-- page 2 -->

# NỘI DUNG CHÍNH

- **Mô hình cơ sở dữ liệu quan hệ**
- **Các ràng buộc toàn vẹn trên quan hệ**
- **Các phép toán đại số trong CSDL quan hệ**


<!-- page 3 -->

# 1. Mô hình CSDL quan hệ

- **Mô hình quan hệ** là cách biểu diễn dữ liệu dưới dạng quan hệ (bảng).
- Trong đó, quan hệ là một bảng 2 chiều, mô tả một thực thể.

| MaNV | TenNV | NgaySinh | DiaChi | Luong |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Nguyen Hai Dang | 1977-08-08 00:00:00.000 | Hoa Binh | 4000000.00 |
| 2 | Tran Cao Ha | 1978-09-01 00:00:00.000 | Yen Bai | 3500000.00 |
| 3 | Hoang A Na | 1975-01-02 00:00:00.000 | Ha Noi | 2300000.00 |
| 4 | Tran Hong Nam | 1976-08-07 00:00:00.000 | Nam Dinh | 3200000.00 |
| 5 | Le Thi Hang | 1976-03-04 00:00:00.000 | Thanh Hoa | 6700000.00 |

- **Thuộc tính**: NgaySinh
- **Bộ**: Dòng thứ 3
- **Lực lượng**: Tổng số dòng (5)
- **Ngôi**: Tổng số cột (5)


<!-- page 4 -->

# 1. Mô hình CSDL quan hệ

## Một số khái niệm được dùng tương đương:

| Người sử dụng | Nhà thiết kế | Lập trình viên |
| :--- | :--- | :--- |
| Hàng (row) | Bộ (tuple) | Bản ghi (record) |
| Cột (column) | Thuộc tính (attribute) | Trường (field) |
| Bảng (table) | Quan hệ (Relation) | Bảng |


<!-- page 5 -->

# 1. Mô hình CSDL quan hệ

## **Đặc điểm của quan hệ:**

- Phần tử nằm chỗ giao nhau giữa dòng và cột là duy nhất
- Các phần của 1 cột thuộc miền giá trị
- Các dòng là khác nhau
- Thứ tự các dòng là không quan trọng
- Thứ tự các cột là không quan trọng


<!-- page 6 -->

# 2. Các ràng buộc toàn vẹn trên quan hệ

- **Ràng buộc khóa**
    - Khóa dự tuyển
    - Khóa chính
    - Khóa ngoại
- **Ràng buộc toàn vẹn tham chiếu**
- **Ràng buộc check**


<!-- page 7 -->

# 2. Các ràng buộc toàn vẹn trên quan hệ

- **Ràng buộc (constrains)** là một quy tắc được đặt vào một đối tượng cơ sở dữ liệu (thường là một bảng hoặc một cột) để giới hạn giá trị dữ liệu trên các đối tượng đó.


<!-- page 8 -->

# 2. Các ràng buộc toàn vẹn trên quan hệ

## Ràng buộc khóa:

- Trên một quan hệ R, một thuộc tính hay 1 bộ các thuộc tính nào đó được gọi là khóa nếu nó giúp xác định giá trị của các thuộc tính còn lại trong quan hệ R

| MaNV | Tên NV | Ngày sinh | Quê |
| :--- | :--- | :--- | :--- |
| 01 | Huế | 16/11/1986 | Hải Dương |
| 02 | Hải | 21/11/1986 | Ninh Bình |
| 03 | Bình | 25/11/1996 | Hà Nội |
| ... | .... | ... | .... |

- {MaNV, Tên NV} $\rightarrow$ Ngày sinh
- MaNV $\rightarrow$ Tên NV, Ngày Sinh, Quê


<!-- page 9 -->

# 2. Các ràng buộc toàn vẹn trên quan hệ

## Phân loại khóa:

- **Siêu khóa** (supper key): Là một khóa bất kỳ, nhận giá trị khác biệt giữa các dòng
- **Khóa dự tuyển** (candidate key): Là một siêu khóa có số lượng thuộc tính tối thiểu
- **Khóa chính** (primary key) là một khóa dự tuyển được chỉ định và không chứa null


<!-- page 10 -->

# 2. Các ràng buộc toàn vẹn trên quan hệ

## Khóa chính và khóa ngoại:

Bảng SANPHAM (maSP, moTa, giaNhap, giaBan, maNCC)
**Khóa chính**: maSP
**Khóa ngoại**: maNcc

| maSP | moTa | giaNhap | giaBan | MaNcc |
| :--- | :--- | :--- | :--- | :--- |
| S001 | Sữa TH 180ml | 25000 | 28000 | 232 |
| SC002 | Sữa chua uống vinamilk | 20000 | 24000 | 378 |
| S004 | Sữa thanh trùng TH 1 lít | 30000 | 32000 | 232 |

Bảng NHACC
- **Khóa chính**: maNCC

| maNcc | tenNcc | nguoiLienHe | SoDt |
| :--- | :--- | :--- | :--- |
| 232 | TH TrueMilk | Nguyễn Văn Thành | 0434852189 |
| 378 | Vinamilk | Trần Hải Yên | 0834554389 |
| 457 | Abort Hoa kỳ | Vũ Hạnh Như | 0599903349 |


<!-- page 11 -->

# 2. Các ràng buộc toàn vẹn trên quan hệ

- **Ràng buộc tham chiếu**
    - Ràng buộc tham chiếu được xác định trên 2 bảng: bảng tham chiếu (referencing relation) và bảng được tham chiếu (referenced relation)
- **Ràng buộc NOT NULL**
- **Ràng buộc CHECK**


<!-- page 12 -->

# 3. Các phép toán đại số trên CSDL quan hệ

- **Phép chọn**
- **Phép chiếu**
- **Tích đề các**
- **Phép nối**
- **Phép hợp**
- **Phép giao**
- **Phép trừ**


<!-- page 13 -->

# 3. Các phép toán đại số trên CSDL quan hệ

## Các phép toán đại số quan hệ

- **Chọn**: lấy ra các dòng của quan hệ thỏa mãn điều kiện

| SSN | Name | DNo |
| :--- | :--- | :--- |
| 001 | Hoàng | P001 |
| 002 | Thiện | P002 |
| 003 | Huy | P001 |
| 004 | Thiện | P003 |

$$\sigma_{DNo = P001}(EMP)$$

| SSN | Name | DNo |
| :--- | :--- | :--- |
| 001 | Hoàng | P001 |
| 003 | Huy | P001 |

- **Chiếu**: loại bỏ đi một số thuộc tính

| SSN | Name | DNo |
| :--- | :--- | :--- |
| 001 | Hoàng | P001 |
| 002 | Thiện | P002 |
| 003 | Huy | P001 |
| 004 | Thiện | P003 |

$$\Pi_{name}(EMP)$$

| Name |
| :--- |
| Hoàng |
| Thiện |
| Huy |
| Thiện |


<!-- page 14 -->

# 3. Các phép toán đại số trên CSDL quan hệ

- **Tích Đề Các**

| SSN | Name | DNo |
| :--- | :--- | :--- |
| 001 | Hoàng | P001 |
| 002 | Thiện | P002 |

X

| DNo | DName |
| :--- | :--- |
| P001 | Tổ chức |
| P002 | Kinh doanh |
| P003 | Nhân sự |

| SSN | Name | DNo | DNo | DName |
| :--- | :--- | :--- | :--- | :--- |
| 001 | Hoàng | P001 | P001 | Tổ chức |
| 001 | Hoàng | P001 | P002 | Kinh doanh |
| 001 | Hoàng | P001 | P003 | Nhân sự |
| 002 | Thiện | P002 | P001 | Tổ chức |
| 002 | Thiện | P002 | P002 | Kinh doanh |
| 002 | Thiện | P002 | P003 | Nhân sự |


<!-- page 15 -->

# 3. Các phép toán đại số trên CSDL quan hệ

- **Nối**

| SSN | Name | DNo |
| :--- | :--- | :--- |
| 001 | Hoàng | P001 |
| 002 | Thiện | P002 |
| 003 | Huy | P001 |
| 004 | Thiện | P003 |

| DNo | DName |
| :--- | :--- |
| P001 | Tổ chức |
| P002 | Kinh doanh |
| P003 | Nhân sự |
| P004 | Tiếp thị |

$$\text{EMP} \bowtie \text{DEP}$$
$$\text{(EMP.DNo = DEP.Dno)}$$

| SSN | Name | DNo | DNo | DName |
| :--- | :--- | :--- | :--- | :--- |
| 001 | Hoàng | P001 | P001 | Tổ chức |
| 002 | Thiện | P002 | P002 | Kinh doanh |
| 003 | Huy | P001 | P001 | Tổ chức |
| 004 | Thiện | P003 | P003 | Nhân sự |


<!-- page 16 -->

# 3. Các phép toán đại số trên CSDL quan hệ

## Chia

| SNo | PNo | PName |
| :--- | :--- | :--- |
| n1 | h1 | Đài |
| n1 | h2 | TV |
| n1 | h3 | Tủ lạnh |
| n2 | h3 | Tủ lạnh |
| n2 | h1 | Đài |
| n3 | h1 | Đài |
| n3 | h2 | TV |
| n3 | h3 | Tủ lạnh |
| n4 | h1 | Đài |

$\div$

| PNo | PName |
| :--- | :--- |
| h1 | Đài |
| h2 | TV |
| h3 | tủ lạnh |

$\downarrow$

| SNo |
| :--- |
| n1 |
| n3 |


<!-- page 17 -->

# 3. Các phép toán đại số trên CSDL quan hệ

- **Hợp**: gộp các bộ của 2 quan hệ và bỏ đi những bộ trùng

| SSN | Name | DNo |
| :--- | :--- | :--- |
| 001 | Hoàng | P001 |
| 002 | Thiện | P002 |

$\cup$

| SSN | Name | DNo |
| :--- | :--- | :--- |
| 003 | Huy | P001 |
| 002 | Thiện | P002 |
| 004 | Thiện | P003 |

$\downarrow$

| SSN | Name | DNo |
| :--- | :--- | :--- |
| 001 | Hoàng | P001 |
| 002 | Thiện | P002 |
| 003 | Huy | P001 |
| 004 | Thiện | P003 |

$\rightarrow$ **Chỉ thực hiện được phép hợp nếu 2 quan hệ khả hợp.**


<!-- page 18 -->

# 3. Các phép toán đại số trên CSDL quan hệ

- **Giao**: lấy ra các bộ cùng có mặt ở 2 quan hệ

| SSN | Name | DNo |
| :--- | :--- | :--- |
| 001 | Hoàng | P001 |
| 002 | Thiện | P002 |

$\cap$

| SSN | Name | DNo |
| :--- | :--- | :--- |
| 003 | Huy | P001 |
| 002 | Thiện | P002 |
| 004 | Thiện | P003 |

$\downarrow$

| SSN | Name | DNo |
| :--- | :--- | :--- |
| 002 | Thiện | P002 |

$\rightarrow$ **Chỉ thực hiện được phép giao nếu 2 quan hệ khả hợp.**


<!-- page 19 -->

# 3. Các phép toán đại số trên CSDL quan hệ

- **Trừ**: của 2 quan hệ A và B lấy ra các bộ có trong A mà không có trong B

| SSN | Name | DNo |
| :--- | :--- | :--- |
| 001 | Hoàng | P001 |
| 002 | Thiện | P002 |

$-$

| SSN | Name | DNo |
| :--- | :--- | :--- |
| 003 | Huy | P001 |
| 002 | Thiện | P002 |
| 004 | Thiện | P003 |

$\downarrow$

| SSN | Name | DNo |
| :--- | :--- | :--- |
| 001 | Hoàng | P001 |

$\rightarrow$ Chỉ thực hiện được phép trừ nếu 2 quan hệ **khả hợp**.


<!-- page 20 -->

# 3. Các phép toán đại số trên CSDL quan hệ

- **Cho các quan hệ sau:**
    - $S(S\#, SNAME, STATUS, CITY)$: Các hãng cung cấp
    - $P(P\#, PNAME, COLOR, WEIGHT, CITY)$: Mặt hàng
    - $SP(S\#, P\#, QTY)$: Các mặt hàng đã cung cấp

- **Thực hiện các yêu cầu sau bằng các phép toán đại số quan hệ:**
    1. Tìm số hiệu của những hãng đã cung ứng mặt hàng P2
    2. Tìm số hiệu của những hãng đã cung ứng ít nhất một mặt hàng màu đỏ
    3. Cho biết thông tin các mặt hàng do công ty S1 và S2 đã cung cấp.
    4. Cho biết thông tin của những hãng mà chưa từng cung cấp sản phẩm.


<!-- page 21 -->

# Làm quen với bài toán Quản lý sinh viên (theo lớp niên chế)

### Sinh Vien
| Column Name | Data Type | Allow Nulls |
| :--- | :--- | :--- |
| MaSV | int | □ |
| HDem | varchar(20) | □ |
| Ten | varchar(10) | □ |
| NgSinh | date | ☑ |
| QQuan | varchar(50) | ☑ |
| GTinh | char(3) | ☑ |
| MaL | char(10) | □ |
| EMail | char(25) | ☑ |
| | | □ |

### Lop
| Column Name | Data Type | Allow Nulls |
| :--- | :--- | :--- |
| MaL | char(10) | □ |
| TenL | varchar(30) | ☑ |
| MaKH | char(10) | ☑ |
| | | □ |

### Khoa
| Column Name | Data Type | Allow Nulls |
| :--- | :--- | :--- |
| MaKH | char(10) | □ |
| TenKh | varchar(30) | ☑ |
| Diachi | varchar(20) | ☑ |
| | | □ |

### Ket Qua
| Column Name | Data Type | Allow Nulls |
| :--- | :--- | :--- |
| MaMH | char(10) | □ |
| MaSV | int | □ |
| Diem | float | ☑ |
| KyThi | tinyint | □ |
| | | □ |

### M Hoc
| Column Name | Data Type | Allow Nulls |
| :--- | :--- | :--- |
| MaMH | char(10) | □ |
| TenMH | varchar(30) | ☑ |
| SoTC | int | ☑ |
| MaKH | char(10) | ☑ |
| | | □ |


<!-- page 22 -->

# HỌC VIỆN NGÂN HÀNG
BANKING ACADEMY OF VIETNAM


<!-- page 23 -->

# THANK YOU FOR WATCHING

**Học viện Ngân hàng**
12 P. Chùa Bộc, P. Kim Liên, TP. Hà Nội

**T:** 1900 561 595 **F:** 1900 561 595
**E:** truyenthong@hvnh.edu.vn
**W:** www.hvnh.edu.vn
