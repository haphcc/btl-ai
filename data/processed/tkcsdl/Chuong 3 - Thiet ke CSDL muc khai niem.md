HỌC VIỆN NGÂN HÀNG
BANKING ACADEMY OF VIETNAM

# CHƯƠNG 3
# THIẾT KẾ CSDL MỨC KHÁI NIỆM

KHOA CÔNG NGHỆ THÔNG TIN VÀ KINH TẾ SỐ


<!-- page 2 -->

# Vòng đời phát triển CSDL

| Giai đoạn | Nội dung chi tiết |
| :--- | :--- |
| **Khởi tạo** | - Tìm hiểu công ty<br>- Xác định bài toán và các ràng buộc<br>- Xác định mục tiêu |
| **Thiết kế** | - Thiết kế mức khái niệm<br>- Lựa chọn hệ quản trị CSDL<br>- Thiết kế logic<br>- Thiết kế vật lý |
| **Thực thi** | - Cài đặt hệ quản trị CSDL<br>- Tạo CSDL<br>- Chuyển đổi/tạo dữ liệu |
| **Kiểm thử & đánh giá** | - Kiểm thử CSDL<br>- Tối ưu hóa CSDL<br>- Đánh giá CSDL và ứng dụng |
| **Vận hành** | - Chạy CSDL thật |
| **Bảo trì** | - Thực hiện các thay đổi<br>- Nâng cấp CSDL |


<!-- page 3 -->

# Các giai đoạn thiết kế

- **Khái niệm**
    - Mô hình thực thể liên kết (ERM)

- **Logic**
    - Lược đồ quan hệ
    - Chuẩn hóa

- **Vật lý**
    - Bảng và mối quan hệ

3


<!-- page 4 -->

# Thiết kế CSDL mức khái niệm

- **Mục đích:**
    - Tạo ra cấu trúc dữ liệu trừu tượng để thể hiện các đối tượng trong thế giới thực một cách chân thực nhất.

- **Có 2 cách tiếp cận:**
    - Top-down
    - Bottom-up

| Mô hình khái niệm |
| :--- |
| Thực thể | Thực thể |
| Thuộc tính | Thuộc tính | Thuộc tính | Thuộc tính |

*(Ghi chú: Mũi tên hướng xuống biểu thị **Top-down**, mũi tên hướng lên biểu thị **Bottom-up**)*


<!-- page 5 -->

# Thiết kế CSDL mức khái niệm

- Tìm hiểu yêu cầu nghiệp vụ
- Xác định hồ sơ dữ liệu liên quan
- ERD

5


<!-- page 6 -->

# 1. Xác định yêu cầu nghiệp vụ

**Gặp gỡ khách hàng: trả lời các câu hỏi sau**

1. Những nhiệm vụ mà hệ thống hiện tại đang giải quyết là gì, khách hàng muốn cải thiện điều gì?
2. Những thông tin nào khách hàng muốn theo dõi và quản lý?
3. Những yêu cầu báo cáo mà các cấp, đơn vị quản lý khác nhau thường yêu cầu đối với hệ thống này là gì?
4. Ai là người sẽ sử dụng hệ thống và họ cần gì ở hệ thống?
5. Hệ thống này có tích hợp với các hệ thống khác hay không?
6. Hệ thống này có thời gian và kinh phí thực hiện như thế nào?
7. Hệ thống được đánh giá mức độ hoàn thành nhiệm vụ như thế nào?
8. Người dùng cần hỗ trợ và đào tạo như thế nào để sử dụng hệ thống?


<!-- page 7 -->

# 1. Xác định yêu cầu nghiệp vụ

## **Đầu ra**

- Sơ đồ tổ chức
- Biểu đồ ngữ cảnh tương tác dữ liệu giữa các thành phần trong và ngoài tổ chức


<!-- page 8 -->

# 2. Xác định hồ sơ biểu mẫu

## Đầu ra

- Tập hợp các biểu mẫu của tất cả các nghiệp vụ trong hệ thống (Mẫu báo cáo, chứng từ, đơn đề nghị,...)
- Màn hình chụp thông tin yêu cầu nhập liệu của hệ thống hiện tại,
- Danh sách những thông tin/biểu mẫu muốn bổ sung


<!-- page 9 -->

# 3. Xây dựng ERD

## **Thực hiện đồng thời**

- Danh mục hồ sơ
- Nội dung hồ sơ

- Chọn lọc thông tin
- Xác định thực thể và thuộc tính
- Xác định mối quan hệ và thuộc tính
- Vẽ sơ đồ thực thể liên kết
- Chuẩn hóa, thu gọn
- ERM


<!-- page 10 -->

# 3. Xây dựng ERD

- **Bước 1**: **Chọn lọc thông tin** $\rightarrow$ **Từ điển dữ liệu**
    - Quy tắc:
        - **Chính xác hóa**
        - **Chọn lọc**
- **Bước 2**: **Xác định thực thể**
    - Quy tắc:
        - **Tìm thuộc tính tên gọi** $\rightarrow$ **thực thể**
        - **Xác định thuộc tính định danh và thuộc tính còn lại**
- **Bước 3**: **Xác định mối quan hệ**
    - Quy tắc:
        - **Xác định mối quan hệ tương tác**
        - **Xác định mối quan hệ ràng buộc**


<!-- page 11 -->

# 3. Xây dựng ERD

- **Bước 4: Vẽ sơ đồ**
    - Vẽ thực thể
    - Vẽ mối quan hệ
    - Sắp xếp lại cho cân đối, dễ nhìn
    - Bổ sung thuộc tính, gạch chân thuộc tính định danh
    - Xác định bản số
- **Bước 5: Chuẩn hóa**
    - Mục đích:
        - Loại bỏ thuộc tính lặp, nhóm lặp, ... và đảm bảo quy tắc nghiệp vụ
    - Rút gọn mô hình, nếu có thể
    - Xác định lại bản số


<!-- page 12 -->

# 3. Xây dựng ERD

**DEMO**

12


<!-- page 13 -->

# Ví dụ

Một cửa hàng kinh doanh thực phẩm. Để có hàng bán cho khách, cửa hàng nhập hàng từ các nhà cung cấp và sau đó nhân viên sẽ bán hàng cho khách tại cửa hàng. Yêu cầu thiết kế một cơ sở dữ liệu giúp cửa hàng quản lý được thông tin hàng hóa nhập và xuất. Thông tin về hàng hóa được dựa trên hai hóa đơn nhập và xuất như sau:

13


<!-- page 14 -->

# PHIẾU NHẬP HÀNG
Số: xxxxxx

**Nhà cung cấp:** ....................................................................................
**Địa chỉ:** .................................................................................................
**Ngày:** ...................................................................................................

| STT | Tên hàng | ĐVT | Số lượng | Đơn giá | Thành tiền |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ...... | ...... | ...... | ...... | ...... | ...... |
| ...... | ...... | ...... | ...... | ...... | ...... |

**Tổng tiền hàng** ....................

# HÓA ĐƠN BÁN HÀNG
Số: xxxxxx

**Khách hàng:** ....................................................................................
**Địa chỉ:** .................................................................................................
**Ngày:** ...................................................................................................
**Nhân viên bán hàng:** .......................................................................

| STT | Tên hàng | ĐVT | Số lượng | Đơn giá | Thành tiền |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ...... | ...... | ...... | ...... | ...... | ...... |
| ...... | ...... | ...... | ...... | ...... | ...... |

**Tổng tiền hàng** ....................
**Thuế VAT** ....................
**Tổng cộng** ....................


<!-- page 15 -->

# Xác định yêu cầu nghiệp vụ

- **Sơ đồ chức**
    - Chủ cửa hàng
    - Nhân viên

- **Biểu đồ ngữ cảnh trao đổi dữ liệu**

| Đối tượng/Thành phần |
| :--- |
| Chủ cửa hàng |
| Báo cáo |
| Nhân viên |
| Phiếu xuất |
| Phiếu nhập |
| Nhà cung cấp |
| Khách hàng |

15


<!-- page 16 -->

# Xác định biểu mẫu

## Nhập hàng

| PHIẾU NHẬP HÀNG | | | | | |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | | | | Số: xxxxxx | |
| **Nhà cung cấp:** | | | | | |
| .................................................................................................................................... | | | | | |
| **Địa chỉ:** | | | | | |
| .................................................................................................................................... | | | | | |
| **Ngày:** ........................................................................................................................ | | | | | |
| **STT** | **Tên hàng** | **ĐVT** | **Số lượng** | **Đơn giá** | **Thành tiền** |
| ...... | ...... | ...... | ...... | ...... | ...... |
| ...... | ...... | ...... | ...... | ...... | ...... |

## Xuất hàng

| HÓA ĐƠN BÁN HÀNG | | | | | |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | | | | Số: xxxxxx | |
| **Họ và tên khách hàng:**.......................................................................................... | | | | | |
| **Địa chỉ:**....................................................................................................................... | | | | | |
| **Ngày :**......................................................................................................................... | | | | | |
| **Nhân viên bán hàng:**................................................................................................ | | | | | |
| **STT** | **Tên hàng** | **ĐVT** | **Số lượng** | **Đơn giá** | **Thành tiền** |
| ...... | ...... | ...... | ...... | ...... | ...... |
| ...... | ...... | ...... | ...... | ...... | ...... |
| **Tổng tiền hàng** | | | | | ...... |
| **Thuế VAT** | | | | | ...... |
| **Tổng cộng** | | | | | ...... |

16


<!-- page 17 -->

# ERD cho PHIẾU NHẬP HÀNG

## Bước 1: chọn lọc thông tin

| Từ trong HSDL | Từ rõ nghĩa | Viết tắt |
| :--- | :--- | :--- |
| Số | Mã đơn nhập hàng | MaDNH |
| Nhà cung cấp | **Tên nhà cung cấp** | TenNCC |
| Địa chỉ | Địa chỉ nhà cung cấp | DiaChi |
| Ngày | Ngày nhập | NgayDat |
| Tên hàng | **Tên hàng** | TenHang |
| Đơn vị | Đơn vị tính | DonVi |
| Đơn giá | Đơn giá nhập | DonGia |
| Số lượng | Số lượng nhập | SoLuong |
| Thành tiền | Thành tiền | ThanhTien |

- **NHÀ CUNG CẤP**
- **HÀNG**


<!-- page 18 -->

# ERD cho PHIẾU NHẬP HÀNG

## Bước 2: Xác định thực thể, thuộc tính

- NHÀ CUNG CẤP (**MaNCC**, TenNCC, DiaChi)
- HÀNG (**MaH**, TenHang, DonVi)

| Từ trong HSDL | Từ rõ nghĩa | Viết tắt |
| :--- | :--- | :--- |
| Số | Mã đơn đặt hàng | MaDDH |
| Nhà Cung Cấp | Tên Nhà cung cấp | TenNCC |
| Địa chỉ | Địa chỉ | DiaChi |
| Ngày đặt | Ngày đặt | NgayDat |
| Tên hàng | Tên hàng | TenH |
| Đơn vị | Đơn vị | DonVi |
| Đơn giá | **Đơn giá nhập** | **Gianhap** |
| Số lượng | Số lượng nhập | SoLuong |
| Thành tiền | **Thành tiền** | **ThanhTien** |


<!-- page 19 -->

# ERD cho PHIẾU NHẬP HÀNG

- **Bước 3: Xác định quan hệ**
    - NHẬP: bao gồm các thuộc tính còn lại trong từ điển

- **Bước 4: Vẽ ERD - 1**

(Sơ đồ ERD bao gồm các thực thể và thuộc tính sau):

- **HÀNG** (Thực thể):
    - MaH
    - TenH
    - DonVi

- **NHÀ CUNG CẤP** (Thực thể):
    - MaNCC
    - TenNCC
    - DiaChi

- **Nhập** (Mối quan hệ):
    - MaHDN
    - SoLuong
    - Ngay
    - ThanhTien
    - GiaNhap
    - TongTien


<!-- page 20 -->

# ERD cho HÓA ĐƠN BÁN HÀNG

| Từ trong HS | Từ rõ nghĩa | Từ viết tắt |
| :--- | :--- | :--- |
| Số | Số hóa đơn xuất | SoHDX |
| Họ và tên khách hàng | **Tên khách hàng** | Ten KH |
| Địa chỉ | Địa chỉ | DiaChi |
| Ngày | Ngày bán | Ngay |
| Nhân viên | **Tên Nhân viên bán** | TenNV |
| Tên hàng | **Tên hàng** | TenHang |
| Đơn vị | Đơn vị | DVT |
| Đơn giá | Đơn giá bán | GiaBan |
| Thành tiền | Thành tiền | ThanhTien |
| Tổng tiền hàng | Tổng tiền hàng | TongTienH |
| Thuế VAT | Thuế VAT | VAT |
| Tổng cộng | Tổng cộng | TongCong |

- **KHÁCH HÀNG**
- **NHÂN VIÊN**
- **HÀNG**

20


<!-- page 21 -->

# ERD cho HÓA ĐƠN BÁN HÀNG

## Bước 2: Xác định thực thể

- **KHÁCH HÀNG**(**MaKH**, TenKH, DiaChi)
- **NHÂN VIÊN**(**MaNV**, TenNV, DiaChi)
- **HÀNG**(**MaH**, TenHang, DVT)

| Từ trong HS | Từ rõ nghĩa | Từ viết tắt |
| :--- | :--- | :--- |
| Số | Số hóa đơn xuất | SoHDX |
| Họ và tên khách hàng | Tên khách hàng | Ten KH |
| Địa chỉ | Địa chỉ | DiaChi |
| Ngày | Ngày bán | NgayBan |
| Nhân viên | Tên nhân viên | TenNV |
| Tên hàng | Tên hàng | TenHang |
| Đơn vị | Đơn vị | DVT |
| Đơn giá | Đơn giá bán | DonGiaBan |
| Thành tiền | Thành tiền | ThanhTien |
| Tổng tiền hàng | Tổng tiền hàng | TongTien |
| Thuế VAT | Thuế VAT | VAT |
| Tổng cộng | Tổng cộng | TongCong |
| Số lượng | Số lượng | SoLuong |

21


<!-- page 22 -->

# ERD cho HÓA ĐƠN BÁN HÀNG

- **Bước 3: Xác định quan hệ**
    - **BÁN**: bao gồm các thuộc tính còn lại trong từ điển
- **Bước 4: Vẽ ERD-2**

| Thực thể/Quan hệ | Thuộc tính |
| :--- | :--- |
| **HÀNG** | TenH, MaH, DVT |
| **Bán** | SoHDB, GiaBan, TongCong, NgayBan, VAT, SoLuong, ThanhTien, TongTien |
| **KHÁCH HÀNG** | MaKH, DiaChi, TenKH |
| **NHÂN VIÊN** | MaNV, TenNV, DiaChi |

22


<!-- page 23 -->

# Tch hp

## S  thc th lin kt (ERD)

Cc thc th v thuc tnh:

- **HNG**
    - MaH
    - ThanhTien
    - TenH
    - DVT
    - SoHDB
    - GiaBan

- **NH CUNG CP**
    - MaNCC
    - TenNCC
    - DiaChi

- **NHN VIN**
    - MaNV
    - TenNV
    - DiaChi

- **KHCH HNG**
    - MaKH
    - DiaChi
    - TenKH

Cc mi quan h v thuc tnh lin kt:

- **Nhp** (gia HNG v NH CUNG CP)
    - MaHDN
    - SoLuong
    - Ngay
    - TongTien
    - GiaNhap

- **Bn** (gia HNG, KHCH HNG v NHN VIN)
    - NgayBan
    - SoLuong
    - ThanhTien
    - TongTien
    - TongCong
    - VAT


<!-- page 24 -->

# Một số vấn đề cần lưu ý

**Sau khi phác thảo xong ERM phải chú ý tới những thông tin mà hệ thống có thể cung cấp theo nhu cầu của người dùng**

- Giá hiện tại của một mặt hàng bất kỳ?
- Số lượng hàng tồn kho
- Thống kê khách hàng theo tỉnh/huyện


<!-- page 25 -->

# Trả lời

- **Giá hiện tại của một mặt hàng bất kỳ?**
    - Thể hiện ở thuộc tính nào,
    - Nó có sẵn sàng với bản thiết kế hiện tại
    → Thêm thuộc tính giá cho thực thể Hàng

- **Số lượng hàng tồn kho = tổng (số lượng nhập) – Tổng (số lượng bán)**
    - Mỗi lần cần tính toán rất lâu
    → Thêm thuộc tính hàng tồn kho, tự động tăng giảm theo số lượng nhập/xuất

25


<!-- page 26 -->

# Trả lời

- **Thống kê khách hàng theo Tỉnh/Huyện**
→ **Địa chỉ phải là thuộc tính tổ hợp:**
**DiaChi (Tỉnh/thành, Phường/Xã, Chi tiết)**

26


<!-- page 27 -->

# S  ER khi iu chnh

## Cc thc th v thuc tnh

- **HNG**
    - MaH
    - TenH
    - GiaH
    - SLTon
    - DVT
    - GiaBan
    - SoHDB

- **NH CUNG CP**
    - MaNCC
    - TenNCC
    - DiaChi

- **NHN VIN**
    - MaNV
    - TenNV
    - DiaChi

- **KHCH HNG**
    - MaKH
    - TenKH
    - DiaChi
        - Tinh
        - Phuong
    - ChiTiet

## Cc mi quan h v thuc tnh lin kt

- **Nhp** (gia HNG v NH CUNG CP)
    - MaHDN
    - SoLuong
    - Ngay
    - ThanhTien (thuc tnh dn xut)
    - TongTien (thuc tnh dn xut)
    - GiaNhap

- **Bn** (gia HNG, KHCH HNG v NHN VIN)
    - NgayBan
    - SoLuong
    - ThanhTien (thuc tnh dn xut)
    - TongTien (thuc tnh dn xut)
    - TongCong (thuc tnh dn xut)
    - VAT


<!-- page 28 -->

# REVIEW CASE STUDY

29


<!-- page 29 -->

# Case study quản lý kho

- **1. Xác định yêu cầu nghiệp vụ**
    - Sơ đồ tổ chức
    - Ngữ cảnh trao đổi dữ liệu
- **2. Hồ sơ dữ liệu**
- **3. Xây dựng ERM**
    - Từ điển dữ liệu
    - Danh sách thực thể
    - Danh sách mối quan hệ
    - ERM


<!-- page 30 -->

# Case study quản lý kho

## 1. Xác định yêu cầu nghiệp vụ

- Sơ đồ tổ chức

**Ban lãnh đạo**

- **Khối Kho**
    - **Kho vật tư** -> Thủ kho
    - **Kho Nhiên liệu** -> Thủ kho
    - **Kho sản phẩm..** -> Thủ Kho
- **Phòng chức năng**
    - **Phòng kinh doanh** -> Quản lý kho
    - **Phòng cung ứng** -> Quản lý kho
    - **Phòng ...** -> Quản lý kho


<!-- page 31 -->

# 1. xác định yêu cầu nghiệp vụ

- Sơ đồ ngữ cảnh trao đổi dữ liệu

*quản lý kho*

- **Thủ kho**: Phiếu Xuất/Nhập
- **Đại lý**: Phiếu Xuất
- **Phân xưởng**: Phiếu Xuất/Nhập
- **Nhà cung cấp**: Phiếu Nhập
- **Kế toán**: Phiếu Xuất/Nhập
- **Lãnh đạo**: Báo cáo
- **Người quản lý kho** (trung tâm)


<!-- page 32 -->

# Danh mục hồ sơ dữ liệu

- **Quản lý nhập kho**
    - Thẻ kho (B) Phiếu nhập kho (C)
- **Quản lý xuất kho**
    - Phiếu xuất kho (D)
    - Danh sách đại lý (E)
- **Quản lý hàng tồn**
    - Báo cáo tồn kho (A)
    - Bảng cân đối kho (F)


<!-- page 33 -->

# Xây dựng ERD

- **Xây dựng từ điển dữ liệu**

34


<!-- page 34 -->

# Xây dựng ERD

## Xác định các thực thể

- Kho (MaKho, TenKho)
- VatTu/Hang (MaH, TenH, đơn vị, đơn giá, Số lượng tồn)
- DaiLy (MaDL, TenDL, DiaChi, SoHopDong, NgayKy, DaiDien, SoCMND)
- NhanVien (MaNV, TenNV, Chức vụ)
- ThuKho (MaNV, TenNV, Chức vụ = Thủ kho)
- QuanLyKho (MaNV, TenNV, Chức vụ = Quản lý kho)
- ** Vì có quá nhiều đối tượng tham gia vào nghiệp vụ nhập/xuất hàng $\rightarrow$ tạo thực thể trung gian PhieuNhap/PhieuXuat làm cho sơ đồ trở nên đơn giản
    - PhieuNhap (Số phiếu, ngày, người nhận)
    - PhieuXuat (Số phiếu, ngày, người giao)


<!-- page 35 -->

# Xác định mối quan hệ

- PhieuNhap <nhập> VatTu/Hang (1:n)
- PhieuNhap <của> NhaCC (n:1)
- NhanVien <kiểm tra> PhieuNhap (1:n)
- ThuKho <xác nhận> PhieuNhap (1:n)
- VatTu/Hang <nhap> NhaCC (n:n)
- DaiLy <có> PhieuXuat (1:n)
- NhanVien <viết> PhieuXuat (1:n)
- KeToan <xác nhận> PhieuXuat (1:n)
- ThuKho <xuất cho> PhieuXuat (1:n)
- Hang <trong> PhieuXuat (1:n)


<!-- page 36 -->

# Nhận xét

- **Chúng ta thấy: nhân viên có thể làm nhiều chức vụ, thủ kho, kế toán, quản lý kho đều là trường hợp đặc biệt của nhân viên**
→ **Có thể gộp nhưng ko nên gộp ở ERM**, nên gộp ở thiết kế logic, dưới khung nhìn của người phát triển hệ thống, bổ sung thêm các ràng buộc
- **Nên thêm thực thể Phòng ban để dễ quản lý nhân viên viên**
    - PhongBan(Mã Phòng, tên phòng)
    - NhanVien <thuộc> Phòng (n:1)
- **VatTu/Hang nên bổ sung thêm thuộc tính loại hàng tăng tốc độ nhập liệu, dễ phục vụ số liệu thống kê.**


<!-- page 37 -->

# ERD hoàn thiện của hệ thống nhập kho

- **Sinh viên tự thực hiện**
- **Công cụ để vẽ ERD: https://app.diagrams.net/**
