### BÀI 8

#### C05 LAP TRINH CO SO DU LIEU

## TRANG 1

= Chueng s -

## LẬP TRINH CƠ SỞDỮLIEU

## TRANG 2

## Nội dung

1 Tổng quan về ADO.NET

2 Kết nối cơ sở dữ liệu bằng ADO.NET

3 Xây dựng ứng dụng minh hoạ

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 2/46

## TRANG 3

1. Tổng quan về ADO.NET

❑ADO.NET và.NET framework ❑ADO.NET là gì?

❑Kiến trúc ADO.NET ❑Các đối tượng trong ADO.NET

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 3/46

## TRANG 4

ADO.NET và.NET framework

Microsoft.NET Framework

Web Services User Interface

Data and XML

## ADO.NET XML......

Base Classes

Common Language Runtime

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 4/46

## TRANG 5

ADO.NET là gì?

ADO.NET là tập hợp các lớp, interface, cấu trúc, kiểu dữ liệu định sẵn đểquản lý việc truy xuất với dữ liệu Ứng dụng

ADO.NET Managed Provider

OLE DB Provider SQL Server Database Database

SQL Managed Provider ADO Managed Provider

using System. Data; using System. Data;

using System. Data. SQLClient; using System. Data. Ole DB;

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 5/46

| Ứng dụng |  |  |
| --- | --- | --- |
| ADO.NET Managed Provider |  |  |
| OLE DB Provider
SQL Server
Database
Database
SQL Managed Provider ADO Managed Provider |  |  |
| SQL Server
Database
SQL Managed Provider |  | OLE DB Provider
Database
ADO Managed Provider |

## TRANG 6

Kiến trúc ADO.NET

1. Connection 3. DataReader 5. Dataset

2. Command 4. DataAdapter

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 6/46

## TRANG 7

2. Kết nối CSDL bằng ADO.NET

Connection Command Data Reader Data Adaper Dataset

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 7/46

## TRANG 8

2.1. Connection

Thiết lập và quản lý kết nối với CSDL Có 2 loại:

◼ Sql Connection ◼ Ole Db Connection Thuộc tính quan trọng:

◼ Connection String Phương thức quan trọng:

◼ Open() ◼ Close() Chú ý:

◼ Luôn đóng Connection sau khi sử dụng

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 8/46

## TRANG 9

2.1. Connection (tiếp)

Ví dụ:

Sql Connection con; //Đối tượng để kết nối con = new Sql Connection(); //Khởi tạo con. Connection String = @"Data Source= .\SQLEXPRESS;Attach Db Filename=“ +Application.Startup Path+ @"\QLSV.mdf;

Integrated Security=True;Connect Timeout=30;User Instance=True";

con. Open(); //Mở kết nối

Tạo Connect String chính xác và nhanh nhất?

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 9/46

## TRANG 10

2.2. Command Thực hiện các thao tác với CSDL ◼ DDL, DML, gọi thủt ục, ….

Có 2 loại:

◼ Sql Command ◼ Ole Db Command Thuộc tính quan trọng:

◼ Connection ◼ Command Text Phương thức quan trọng:

◼ Execute Non Query() (thực hiện lệnh: INSERT, UPDATE, DELETE) ◼ Execute Scalar() (thực hiện lệnh SELECT trảvề1 giá trị) ◼ Execute Reader() (thực hiện lệnh SELECT trảvềmột hay nhiều bản ghi) 23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 10/46

## TRANG 11

2.2. Command (tiếp)

Ví dụ:

Sql Command cmd = new Sql Command();

cmd. Connection = con;

cmd. Command Text = “UPDATE Nhan Vien set Luong = Luong + 100000 WHERE Ma NV = 01”;

cmd. Execute Non Query();

… con. Close();

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 11/46

## TRANG 12

2.3. Data Reader

Có dạng con trỏ, dùng đểhandle dữ liệu trả về từCSDL Đặc điểm:

◼ Con trỏkh ông thểl ùi ◼ Thường handle dữ liệu trảvềt ừph ương thức Execute Reader() của Command Có 2 loại:

◼ Sql Data Reader ◼ Ole Db Reader Khuy ến cáo:

◼ Đối với các form chỉSELECT dữ liệu, NÊN DÙNG Data Reader đểcó tốc độx ửl ý nhanh hơn

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 12/46

## TRANG 13

2.3. Data Reader (tiếp)

Ví dụ:

Sql Command cmd = new Sql Command();

cmd. Connection = con;

cmd. Command Text = “SELECT Ma SV, Hoten FROM tbl Sinhvien”;

Sql Data Reader rd = cmd. Execute Reader();

while (rd. Read()) { txt Ma SV. Text = rd[0]. To String();

txt Hoten. Text= rd[1]. To String();

} con. Close();

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 13/46

## TRANG 14

2.4. Data Adapter

Là cầu nối giữa CSDL và Dataset

Các thuộc tính quan trọng:

◼ Select Command ◼ Update Command ◼ Insert Command ◼ Delete Command Các phương thức quan trọng:

◼ Fill() ◼ Update() Có cơ chết ựđộng đóng Connection

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 14/46

## TRANG 15

2.4. Data Adapter (tiếp)

Ví dụ- Hiển thị dữ liệu:

string sql;

sql = "SELECT * from tbl Chat Lieu";

//Đối tượng Data Adapter Sql Data Adapter My Data = new Sql Data Adapter(sql,con);

tbl Chat Lieu= new Data Table(); //Khởi tạo bảng //Đổ dữ liệu từData Adapter vào bảng My Data. Fill(tbl Chat Lieu);

data Grid View Chat Lieu. Data Source = tbl Chat Lieu;

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 15/46

## TRANG 16

2.5. Dataset

Là đối tượng lưu dữ liệu trảvềt ừCSDL

Dataset Data Adapter DB

Relations, Constraint

Dataset Database

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 16/46

## TRANG 17

3. Xây dựng ứng dụng minh hoạ

Bài toán Xây dựng ứng dụng quản lý sinh viên đơn giản ◼ Cho phép đọc dữ liệu từcsdl sinh viên ◼ Thực hiện các thao tác: Thêm, sửa, xoá ◼ Cơ sở dữ liệu: gồm bảng SINHVIEN(Ma SV, Hoten, Ngaysinh, Khoa, Lop, Diachi) Các bước thực hiện ◼ Bước 1: Tạo cơ sở dữ liệu ◼ Bước 2: Thiết kếgiao diện ◼ Bước 3: Thực hiện kết nối cơ sở dữ liệu ◼ Bước 4: Xử lý các sự kiện

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 17/46

## TRANG 18

3. Xây dựng ứng dụng minh hoạ

Bước 1: Tạo cơ sở dữ liệu ◼ Tạo ứng dụng mới ◼ Tạo cơ sở dữ liệu  Ởkhung Solution Explorer, nháy phải chuột lên tên ứng dụng, chọn Add →New Item…  Chọn Data →Service-based Database (hoặc SQL Database trong Visual Studio)  Tạo bảng tbl Sinhvien

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 18/46

## TRANG 19

3. Xây dựng ứng dụng minh hoạ

Bước 2: Thiết kếgiao diện ◼ Các đối tượng:

 Textbox:

◼ txt Ma SV ◼ txt Hoten ◼ txt Khoa ◼ txt Lop ◼ txt Diachi  Maskedtextbox ◼ txt Ngaysinh  Data Grid View ◼ Data Grid View  Buttons ◼ btn Moi, btn Sua, btn Xoa, btn Luu, btn Huy, btn Thoat

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 19/46

## TRANG 20

3. Xây dựng ứng dụng minh hoạ

Bước 3: Thực hiện kết nối cơ sở dữ liệu Sql Connection con; //Đối tượng để kết nối Data Table tbl Sinhvien; //Đối tượng lưu bảng sinh viên public void Connect() //Kết nối { con = new Sql Connection(); //Khởi tạo đối tượng con. Connection String = @"Data Source=.\SQLEXPRESS;

Attach Db Filename="+Application.Startup Path+ @"\QLSV.mdf;

Integrated Security=True;Connect Timeout=30; User Instance=True";

con. Open(); //Mởkết nối } public void Disconnect() //Ngắt kết nối { if (con. State == Connection State. Open) //nếu đang mở { con. Close(); //đóng con. Dispose(); //huỷ } }

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 20/46

## TRANG 21

3. Xây dựng ứng dụng minh hoạ

Bước 4: Xử lý các sự kiện ◼ Hiển thịthông tin trong Data Grid View

public void Load Data Grid View() { string sql;

sql = "SELECT * from tbl Sinh Vien";

Sql Data Adapter My Data = new Sql Data Adapter(sql,con);

//Đối tượng Data Adapter tbl Sinhvien = new Data Table(); //Khởi tạo bảng My Data. Fill(tbl Sinhvien); //Đổ dữ liệu từ Data Adapter vào bảng data Grid View. Data Source = tbl Sinhvien;

}

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 21/46

## TRANG 22

3. Xây dựng ứng dụng minh hoạ

Bước 4: Xử lý các sự kiện ◼ Thực hiện lệnh SQL public void Run SQL(string sql) //Thực hiện một câu lệnh SQL { Sql Command cmd = new Sql Command(); //Đối tượng để thực hiện lệnh cmd. Command Text = sql;

cmd. Connection = con;

try { cmd. Execute Non Query(); //Thực hiện câu lệnh } catch (Exception ex) { Message Box. Show(ex. To String());

} }

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 22/46

## TRANG 23

3. Xây dựng ứng dụng minh hoạ

Bước 4: Xử lý các sự kiện ◼ Nhấn nút Sửa private void btn Sua_Click(object sender, Event Args e) { string sql;

sql = "UPDATE tbl Sinh Vien SET Hoten=N'" + txt Hoten. Text + "',Ngaysinh='" + txt Ngaysinh. Text + "',Khoa=N'" + txt Khoa. Text + "',Lop=N'" + txt Lop. Text + "',Diachi=N'" + txt Diachi. Text+ "' WHERE Ma SV='" + txt Ma SV. Text +"'";

Run SQL(sql); //thực hiện lệnh sql Load Data Grid View(); //hiển thịl ại thông tin lên Data Grid View }

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 23/46

## TRANG 24

3. Xây dựng ứng dụng minh hoạ

Bước 4: Xử lý các sự kiện ◼ Nhấn nút Lưu private void btn Luu_Click(object sender, Event Args e) { string sql;

sql = "SELECT Ma SV FROM tbl Sinh Vien WHERE Ma SV=N'" + txt Ma SV. Text + "'";

Sql Data Adapter My Data = new Sql Data Adapter(sql, con);

Data Table table = new Data Table();

My Data. Fill(table);

if (table. Rows. Count > 0) { Message Box. Show("Mã sinh viên này đã tồn tại");

return; } //Thực hiện chèn thêm mới sql = "INSERT INTO tbl Sinh Vien VALUES (N'" + txt Ma SV. Text + "',N'" + txt Hoten. Text + "','" + txt Ngaysinh. Text + "',N'" + txt Khoa. Text + "',N'" + txt Lop. Text + "',N'" + txt Diachi. Text + "')";

Run SQL(sql);

Load Data Grid View();

}

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 24/46

## TRANG 25

3. Xây dựng ứng dụng minh hoạ

Bước 4: Xử lý các sự kiện ◼ Nhấn nút Xoá private void btn Xoa_Click(object sender, Event Args e) { string sql;

if (Message Box. Show("Bạn có muốn xóa không?", "Thông báo", Message Box Buttons.OKCancel, Message Box Icon. Question) == Dialog Result.OK) { sql = "DELETE tbl Sinh Vien WHERE Ma SV=N'" + txt Ma SV. Text + "'";

Run SQL(sql);

Load Data Grid View();

Reset Value();

} } 23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 25/46

## TRANG 26

## Bài tập về nhà

Bài toán:

◼ Xây dựng chương trình quản lý cửa hàng Bán hàng lưu niệm Yêu cầu:

◼ Bước 1: Tạo cơ sở dữ liệu ◼ Bước 2: Thiết kếgiao diện

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 26/46

## TRANG 27

## Bài tập về nhà

Bước 1: Tạo cơ sở dữ liệu ◼ Tên tập tin: Quanlybanhang. mdf ◼ Các bảng  Bảng tbl Chatlieu (chất liệu)

 Bảng tbl Khach (khách)

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 27/46

## TRANG 28

Bước 1: Tạo cơ sở dữ liệu ◼ Tên tập tin: Quanlybanhang. mdf ◼ Các bảng  Bảng tbl Hang (hàng)

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 28/46

## TRANG 29

Bước 1: Tạo cơ sở dữ liệu ◼ Tên tập tin: Quanlybanhang. mdf ◼ Các bảng  Bảng tbl Nhanvien (nhân viên)

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 29/46

## TRANG 30

Bước 1: Tạo cơ sở dữ liệu ◼ Tên tập tin: Quanlybanhang. mdf ◼ Các bảng  Bảng tbl HDBan (hoá đơn bán)

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 30/46

## TRANG 31

Bước 1: Tạo cơ sở dữ liệu ◼ Tên tập tin: Quanlybanhang. mdf ◼ Các bảng  Bảng tbl Chitiet HDBan (chi tiết hoá đơn bán)

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 31/46

## TRANG 32

Bước 1: Tạo cơ sở dữ liệu ◼ Quan hệgi ữa các bảng (Relationship)

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 32/46

## TRANG 33

Bước 2: Thiết kếgiao diện ◼ Form chính  Tên form: frm Main

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 33/46

## TRANG 34

Bước 2: Thiết kếgiao diện ◼ Form chính  Tên form: frm Main  Menu: các thuộc tính Name và Text:

Name Text Name Text mnu File Tập tin mnu Timkiem Tìm kiếm mnu Thoat Thoát mnu Find Hoadon Hoá đơn mnu Danhmuc Danh mục mnu Find Hang Hàng mnu Chatlieu Chất liệu mnu Find Khachhang Khách hàng mnu Nhanvien Nhân viên mnu Baocao Báo cáo mnu Khachhang Khách hàng mnu BCHangton Hàng tồn mnu Hanghoa Hàng hoá mnu BCDoanhthu Do anh thu mnu Hoadon Hoá đơn mnu Trogiup Trợ giúp mnu Hoadonban Hoá đơn bán mnu Hientrogiup Trợ giúp mnu Vainet Vài nét

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 34/46

| Name | Text | Name | Text |
| --- | --- | --- | --- |
| mnuFile
mnuThoat
mnuDanhmuc
mnuChatlieu
mnuNhanvien
mnuKhachhang
mnuHanghoa
mnuHoadon
mnuHoadonban | Tập tin
Thoát
Danh mục
Chất liệu
Nhân viên
Khách hàng
Hàng hoá
Hoá đơn
Hoá đơn bán | mnuTimkiem
mnuFindHoadon
mnuFindHang
mnuFindKhachhang
mnuBaocao
mnuBCHangton
mnuBCDoanhthu
mnuTrogiup
mnuHientrogiup
mnuVainet | Tìm kiếm
Hoá đơn
Hàng
Khách hàng
Báo cáo
Hàng tồn
Do anh thu
Trợ giúp
Trợ giúp
Vài nét |

## TRANG 35

Bước 2: Thiết kếgiao diện ◼ Form Danh mục chất liệu  Tên form: frm DMChatlieu

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 35/46

## TRANG 36

Bước 2: Thiết kếgiao diện ◼ Form Danh mục chất liệu  Các thành phần trên form

Điều khiển Name Text

Text Box txt Machatlieu txt Tenchatlieu Button btn Them Thêm btn Xoa Xoá btn Sua Sửa btn Luu Lưu btn Boqua Bỏqua btn Do ng Đóng Data Grid View Data Grid View

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 36/46

| Điều khiển | Name | Text |
| --- | --- | --- |
| TextBox | txtMachatlieu |  |
|  | txtTenchatlieu |  |
| Button | btnThem | Thêm |
|  | btnXoa | Xoá |
|  | btnSua | Sửa |
|  | btnLuu | Lưu |
|  | btnBoqua | Bỏ qua |
|  | btnDong | Đóng |
| DataGridView | DataGridView |  |

## TRANG 37

Bước 2: Thiết kếgiao diện ◼ Form Danh mục nhân viên  Tên form: frm DMNhanvien

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 37/46

## TRANG 38

Bước 2: Thiết kếgiao diện ◼ Form Danh mục nhân viên  Các thành phần trên form

Điều khiển Name Text

Text Box txt Manhanvien txt Tennhanvien txt Diachi Button btn Them, btn Xoa, btn Sua, btn Luu, btn Boqua, btn Do ng Check Box chk Gioitinh Nam Masked Text Box msk Dienthoai Mask: Phone Number msk Ngaysinh Mask: Short Date Data Grid View Data Grid View

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 38/46

| Điều khiển | Name | Text |
| --- | --- | --- |
| TextBox | txtManhanvien |  |
|  | txtTennhanvien |  |
|  | txtDiachi |  |
| Button | btnThem, btnXoa, btnSua, btnLuu, btnBoqua,
btnDong |  |
| CheckBox | chkGioitinh | Nam |
| MaskedTextBox | mskDienthoai | Mask: Phone Number |
|  | mskNgaysinh | Mask: Short Date |
| DataGridView | DataGridView |  |

## TRANG 39

Bước 2: Thiết kếgiao diện ◼ Form Danh mục khách hàng  Tên form: frm DMKhachhang

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 39/46

## TRANG 40

◼ Form Danh mục khách hàng  Các thành phần trên form

Điều khiển Name Text

Text Box txt Makhach txt Tenkhach txt Diachi Button btn Them, btn Xoa, btn Sua, btn Luu, btn Boqua, btn Do ng Check Box chk Gioitinh Nam Masked Text Box msk Dienthoai Mask: Phone Number

Data Grid View Data Grid View

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 40/46

| Điều khiển | Name | Text |
| --- | --- | --- |
| TextBox | txtMakhach |  |
|  | txtTenkhach |  |
|  | txtDiachi |  |
| Button | btnThem, btnXoa, btnSua, btnLuu, btnBoqua,
btnDong |  |
| CheckBox | chkGioitinh | Nam |
| MaskedTextBox | mskDienthoai | Mask: Phone Number |
| DataGridView | DataGridView |  |

## TRANG 41

◼ Form Danh mục hàng hoá  Tên form: frm DMHang

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 41/46

## TRANG 42

◼ Form Danh mục hàng hoá  Các thành phần trên form

Điều khiển Name

Text Box txt Mahang, txt Tenhang, txt Soluong, txt Do ngianhap, txt Do ngiaban, txt Anh, txt Ghichu

Combo Box cbo Machatlieu

Picture Box pic Anh

Data Grid View Data Grid View

Button btn Them, btn Xoa, btn Sua, btn Luu, btn Boqua, btn Timkiem, btn Hienthi, btn Do ng, btn Open.

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 42/46

| Điều khiển | Name |  |
| --- | --- | --- |
| TextBox | txtMahang, txtTenhang, txtSoluong,
txtDongianhap, txtDongiaban, txtAnh, txtGhichu |  |
| ComboBox | cboMachatlieu |  |
| PictureBox | picAnh |  |
| DataGridView | DataGridView |  |
| Button | btnThem, btnXoa, btnSua, btnLuu, btnBoqua,
btnTimkiem, btnHienthi, btnDong, btnOpen. |  |

## TRANG 43

◼ Form Hoá đơn bán hàng  Tên form: frm Hoadon Ban

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 43/46

## TRANG 44

◼ Form Hoá đơn bán  Các thành phần trên form

Điều khiển Name Text

Label lbl Bangchu Bằng chữ:

Text Box txt Ma HDBan, txt Ngayban, txt Tennhanvien,txt Tenkhach, txt Diachi, txt Dienthoai, txt Tongtien, txt Tenhang, txt Do ngiaban, txt Soluong, txt Giamgia, txt Thanhtien.

Combo Box cbo Manhanvien, cbo Makhach, cbo Mahang, cbo Ma HDBan.

Data Grid View Data Grid View Button btn Ngay, btn Themmoi, btn Luu, btn Xoa, btn Inhoadon, btn Do ng, btn Timkiem

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 44/46

| Điều khiển | Name | Text |
| --- | --- | --- |
| Label | lblBangchu | Bằng chữ: |
| TextBox | txtMaHDBan, txtNgayban, txtTennhanvien,txtTenkhach,
txtDiachi, txtDienthoai, txtTongtien, txtTenhang,
txtDongiaban, txtSoluong, txtGiamgia, txtThanhtien. |  |
| ComboBox | cboManhanvien, cboMakhach, cboMahang,
cboMaHDBan. |  |
| DataGridView | DataGridView |  |
| Button | btnNgay, btnThemmoi, btnLuu, btnXoa, btnInhoadon,
btnDong, btnTimkiem |  |

## TRANG 45

◼ Form Tìm kiếm hoá đơn  Tên form: frm Tim HDBan

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 45/46

## TRANG 46

◼ Form Tìm kiếm hoá đơn  Các thành phần trên form

Điều khiển Name

Text Box txt Ma HDBan, txt Thang, txt Nam, txt Manhanvien,

txt Makhach, txt Tongtien.

Data Grid View Data Grid View

Button btn Timkiem, btn Timlai, btn Do ng

23/05/2026 Chương 5. Lập trình cơ sở dữ liệu 46/46

| Điều khiển | Name |
| --- | --- |
| TextBox | txtMaHDBan, txtThang, txtNam,
txtManhanvien,
txtMakhach, txtTongtien. |
| DataGridView | DataGridView |
| Button | btnTimkiem, btnTimlai, btnDong |
