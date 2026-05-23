### BÀI 7

#### C04 LAP TRINH GIAO DIEN TRONG WINDOWS PART2

## HỌC VIỆN NGÂN HÀNG

## KHOA CÔNG NGHỆ THÔNG TIN VÀ KINH TẾ SỐ

## Chương 4

## LẬP TRÌNH GIAO DIỆN

## TRONG WINDOWS

## Nội dung

1 Giới thiệu về lập trình giao diện trong Windows

2 Làm việc với Windows form và các điều khiển

3 Các hộp thoại thông dụng

4 Thực đơn và ứng dụng nhiều biểu mẫu

23/05/2026 Chương 4. Lập trình giao diện trong Windows 2/26

3. Các hộp thoại thông dụng

Nằm trong System. IO Gồm 5 hộp thoại thông dụng ◼ Open File: Mởfile ◼ Save File: Lưu file ◼ Font: Font chữ ◼ Color: Màu sắc ◼ Print: Inấn

23/05/2026 Chương 4. Lập trình giao diện trong Windows 3/26

Hộp thoại Open File

Cho phép lựa chọn một/nhiều file đểm ở

Thuộc tính Mô tả File Name Tên (đường dẫn) của tập tin đã chọn.

Filter Danh sách các bộl ọc tập tin

Ví dụ: “Text|*. txt|Icons|*. ico|All files|*.*” Filter Index Bộ lọc tập tin mặc định, giảsửcó 3 bộl ọc (*. com), (*. exe) và (*. ico) nếu Filter Index = 2 thì hộp thoại sẽhi ển thịs ẵn bộl ọc (*. exe) Initial Directory Xác định thư mục mặc định cho hộp thoại Multiselect True/False: cho phép/không cho phép chọn nhiều file File Names Tên và đường dẫn của các tập tin đã chọn.

Title Xác định tiêu đềcủa hộp hội thoại.

Open File Mở nội dung File đã được chọn (Read Only).

23/05/2026 Chương 4. Lập trình giao diện trong Windows 4/26

| Thuộc tính | Mô tả |
| --- | --- |
| FileName | Tên (đường dẫn) của tập tin đã chọn. |
| Filter | Danh sách các bộ lọc tập tin
Ví dụ: “Text|*. txt|Icons|*. ico|All files|*.*” |
| FilterIndex | Bộ lọc tập tin mặc định, giả sử có 3 bộ lọc (*.com), (*.exe)
và (*. ico) nếu FilterIndex = 2 thì hộp thoại sẽ hiển thị sẵn
bộ lọc (*. exe) |
| InitialDirectory | Xác định thư mục mặc định cho hộp thoại |
| Multiselect | True/False: cho phép/không cho phép chọn nhiều file |
| FileNames | Tên và đường dẫn của các tập tin đã chọn. |
| Title | Xác định tiêu đề của hộp hội thoại. |
| OpenFile | Mở nội dung File đã được chọn (ReadOnly). |

Type: Picture Box, name: Pic Anh

Type: Button, name:btn Open

private void btn Open_Click(object sender, Event Args e) { Open File Dialog dlg Open = new Open File Dialog();

dlg Open. Filter = "Bitmap(*. bmp)|*. bmp|Gif(*. gif) |*. gif|All files(*.*)|*.*";

dlg Open. Initial Directory = "D:\\Baigiang";

dlg Open. Filter Index = 2;

dlg Open. Title = "Cho n hinh anh de hien thi";

if (dlg Open. Show Dialog() == Dialog Result.OK) pic Anh. Image = Image. From File(dlg Open. File Name);

else Message Box. Show("You clicked Cancel", "Open Dialog", Message Box Buttons.OK, Message Box Icon. Information);

}

23/05/2026 Chương 4. Lập trình giao diện trong Windows 5/26

Hộp thoại Save File

Cho phép lưu file

Thuộc tính Mô tả File Name Tên (đường dẫn) của tập tin đã chọn.

Filter Danh sách các bộl ọc tập tin

Ví dụ: “Text|*. txt|Icons|*. ico|All files|*.*” Filter Index Bộ lọc tập tin mặc định, giảsửcó 3 bộl ọc (*. com), (*. exe) và (*. ico) nếu Filter Index = 2 thì hộp thoại sẽhi ển thịs ẵn bộl ọc (*. exe) Initial Directory Xác định thư mục mặc định cho hộp thoại Title Xác định tiêu đềcủa hộp hội thoại.

Add Extension True/False: tựđộng thêm phần mởr ộng hiện hành vào tên tệp mà người dùng chọn nếu người dùng không chỉr õ

## phần mởrộng của tên tệp.

Default Ext Phần mởr ộng mặc định cho tên tệp, nếu người dùng không chỉr õ phần mởr ộng của tên tệp

23/05/2026 Chương 4. Lập trình giao diện trong Windows 6/26

| Thuộc tính | Mô tả |
| --- | --- |
| FileName | Tên (đường dẫn) của tập tin đã chọn. |
| Filter | Danh sách các bộ lọc tập tin
Ví dụ: “Text|*. txt|Icons|*. ico|All files|*.*” |
| FilterIndex | Bộ lọc tập tin mặc định, giả sử có 3 bộ lọc (*.com), (*.exe)
và (*. ico) nếu FilterIndex = 2 thì hộp thoại sẽ hiển thị sẵn
bộ lọc (*. exe) |
| InitialDirectory | Xác định thư mục mặc định cho hộp thoại |
| Title | Xác định tiêu đề của hộp hội thoại. |
| AddExtension | True/False: tự động thêm phần mở rộng hiện hành vào
tên tệp mà người dùng chọn nếu người dùng không chỉ rõ
phần mở rộng của tên tệp. |
| DefaultExt | Phần mở rộng mặc định cho tên tệp, nếu người dùng
không chỉ rõ phần mở rộng của tên tệp |

Luồng File - File Stream

Luồng ghi dữ liệu - Stream Writer ◼ Mởlu ồng đểghi file Stream Writer Tenluong = new Stream Writer(Tenfile);

◼ Ghi từng dòng Stream Writer Tenluong = new Stream Writer(Tenfile);

◼ Ghi toàn bộn ội dùng vào file Tenluong. Write(“Noidung”);

23/05/2026 Chương 4. Lập trình giao diện trong Windows 7/26

Luồng file - File Stream

Luồng đọc dữ liệu - Stream Reader ◼Mởlu ồng đểđ ọc file:

Stream Reader Tenluong = new Stream Reader(Tenfile);

◼Đọc từng dòng dữ liệu của file: ta dùng vòng lặp với số lần lặp không xác định đểđ ọc từng dòng dữ liệu, nếu đọc thành công thì trảvềchu ỗi chứa dữ liệu đọc được, nếu đến cuối file thì trảvềNothing.

Noidung = Tenluong. Read Line();

◼Đọc tất cả dữ liệu của file lưu vào một biến:

Noidung = Tenluong. Read To End();

◼Đóng luồng:

Tenluong. Close();

23/05/2026 Chương 4. Lập trình giao diện trong Windows 8/26

private void btn Save_Click(object sender, Event Args e) { Save File Dialog dlg Save = new Save File Dialog();

dlg Save. Filter = "Text file(*. txt)|*. txt |Word Do cument(*. do c) |*. do c| All files(*.*)|*.*";

dlg Save. Initial Directory = "D:\\Baigiang";

dlg Save. Filter Index = 2;

dlg Save. Title = "Cho n file de luu";

dlg Save. Add Extension = true;

dlg Save. Default Ext = ". do c";

if (dlg Save. Show Dialog() == Dialog Result.OK) { Stream Writer File;

File = new Stream Writer(dlg Save. File Name);

try { File. Write(txt Save. Text);

} catch(System. Exception) { Message Box. Show("Lỗi ghi file");

} File. Close();

} } 23/05/2026 Chương 4. Lập trình giao diện trong Windows 9/26

Hộp thoại Font

Cho phép chọn font chữ

Thuộc tính Mô tả Font Font chữđược chọn trong hộp thoại Font.

Show Color True/False: cho phép/không cho phép hiển thịh ộp thoại Color.

Color Màu được chọn trong hộp thoại Font.

23/05/2026 Chương 4. Lập trình giao diện trong Windows 10/26

| Thuộc tính | Mô tả |
| --- | --- |
| Font | Font chữ được chọn trong hộp thoại Font. |
| ShowColor | True/False: cho phép/không cho phép hiển thị hộp thoại
Color. |
| Color | Màu được chọn trong hộp thoại Font. |

Hộp thoại Color

Hiển thịb ảng màu

Thuộc tính Mô tả Color Màu được chọn trong hộp thoại Color.

Full Open Hiển thịto àn bộh ộp thoại Color.

Solid Color Only Không hiển thịph ần Define Custom Colors.

23/05/2026 Chương 4. Lập trình giao diện trong Windows 11/26

| Thuộc tính | Mô tả |
| --- | --- |
| Color | Màu được chọn trong hộp thoại Color. |
| FullOpen | Hiển thị toàn bộ hộp thoại Color. |
| SolidColorOnly | Không hiển thị phần Define Custom Colors. |

4. Thực đơn và ứng dụng nhiều biểu mẫu

Thực đơn (menu) ◼ Điều khiển Menu Strip ◼ Cho phép  Thiết kếthanh thực đơn  Lựa chọn kiểu thực đơn  Phím tắt

23/05/2026 Chương 4. Lập trình giao diện trong Windows 12/26

Thực đơn - Menu

Thuộc tính Mô tả Name Mọi mục menu đều phải có tên, bắt đầu bằng mnu Enabled True/False: bật/tắt Image Thiết lập hình ảnh biểu tượng Shortcut Key Phím tắt s Text Tạo tiêu đềcủa các mục menu. Nếu đặt ký tự& trước một chữc ái trong thuộc tính Text thì khi chạy chương trình người dùng có thểb ấm tổh ợp phím Alt + Chữc ái đó để kích hoạt menu. Ví dụ: &File sẽcho phép bấm Alt+F để kích hoạt menu File.

Nếu Text được xác lập là một dấu trừ(-) C# sẽhi ển thị một đường thẳng ngăn cách giữa các khoản mục menu.

Visible True/False: hiển thị/không hiển thị Tool Tip Text Dòng mách nước cho các mục menu

23/05/2026 Chương 4. Lập trình giao diện trong Windows 13/26

| Thuộc tính | Mô tả |
| --- | --- |
| Name | Mọi mục menu đều phải có tên, bắt đầu bằng mnu |
| Enabled | True/False: bật/tắt |
| Image | Thiết lập hình ảnh biểu tượng |
| ShortcutKey
s | Phím tắt |
| Text | Tạo tiêu đề của các mục menu. Nếu đặt ký tự & trước một
chữ cái trong thuộc tính Text thì khi chạy chương trình người dùng có thể bấm tổ hợp phím Alt + Chữ cái đó để kích hoạt menu. Ví dụ: &File sẽ cho phép bấm Alt+F để kích hoạt menu File.
Nếu Text được xác lập là một dấu trừ (-) C# sẽ hiển thị
một đường thẳng ngăn cách giữa các khoản mục menu. |
| Visible | True/False: hiển thị/không hiển thị |
| ToolTipText | Dòng mách nước cho các mục menu |

Menu ngữ cảnh - Context Menu Strip

Cho phép tạo menu ngữc ảnh ◼ Gán menu ngữc ảnh cho các điều khiển khác qua thuộc tính Context Menu Strip ◼ Tên bắt đầu bằng cmnu ◼ Thuộc tính tương tựnh ư Menu Strip

23/05/2026 Chương 4. Lập trình giao diện trong Windows 14/26

Ứng dụng nhiều biểu mẫu

Thêm biểu mẫu ◼ Project →Add Windows Form… ◼ Nháy phải tên project ở Solution Explorer →Add →Windows Form ◼ Ctrl + Shift + A Chọn biểu mẫu khởi động ◼ Trong file program. cs  Application. Run(new Tên_form_kh ởi_động());

 Ví dụ: Application. Run(new frm Main());

23/05/2026 Chương 4. Lập trình giao diện trong Windows 15/26

Ứng dụng nhiều biểu mẫu

Gọi biểu mẫu ◼ Giảsửcó 2 form: Form1 và Form2, trong đó Form1 cần gọi From2 ◼ Cách 1: Dùng phương thức Show Form2 frm = new Form2();

frm. Show();

◼ Cách 2: Dùng phương thức Show Dialog Form2 frm = new Form2();

Frm. Show Dialog();

Đóng biểu mẫu ◼ Phương thức: Hide, Close

23/05/2026 Chương 4. Lập trình giao diện trong Windows 16/26

## Bài tập về nhà

Thiết kếgiao diện cho hệth ống trong bài tập lớn

23/05/2026 Chương 4. Lập trình giao diện trong Windows 17/26
