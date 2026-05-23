### BÀI 6

#### C04 LAP TRINH GIAO DIEN TRONG WINDOWS PART1

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

23/05/2026 Chương 4. Lập trình giao diện trong Windows 2/51

1. Lập trình giao diện trong Windows

.NET cung cấp Win Form và các điều khiển khác qua lớp cơ sở trong namespace System. Windows. Forms Đểthi ết kếWindows Application ◼ Tạo một Windows Application trong Visual Studio.NET và thêm System. Windows. Forms và System. Drawing ◼ Tạo một lớp mới để biểu diễn Win Form và dẫn xuất từ System. Windows. Forms. Form ◼ Khởi tạo các điều khiển khác nhau, thiết lập các thuộc tính và thêm tập hợp các điều khiển

23/05/2026 Chương 4. Lập trình giao diện trong Windows 3/51

Tạo ứng dụng Windows Form

23/05/2026 Chương 4. Lập trình giao diện trong Windows 4/51

Windows Form

Form Designer ◼ Thiết kế giao diện đồ họa người sử dụng các điều khiển (control) từ hộp công cụ (Toolbox) Properties window ◼ Thiết lập thuộc tính Solution Explorer ◼ Solution: là tập tất cả các project ◼ Reference: chứa các file assemblies ◼ Assembly Info. cs: chứa thông tin assembly hiện tại ◼ Form. cs: chứa file nguồn

23/05/2026 Chương 4. Lập trình giao diện trong Windows 5/51

23/05/2026 Chương 4. Lập trình giao diện trong Windows 6/51

2. Windows form và các điều khiển

Điều khiển (control) là các thành phần cơ bản trên form Có các thành phần ◼ Thuộc tính (property)  Mô tảđ ối tượng: tên, chiều cao,...

 Có thể xác định khi thiết kế(Design) hoặc thi hành (Runtime) ◼ Phương thức (method)  Cách thức đểth ực hiện một công việc nào đó ◼ Sự kiện (event)  Phản ứng của đối tượng dựa trên sự kiện xảy ra

23/05/2026 Chương 4. Lập trình giao diện trong Windows 7/51

Hộp thông báo - Message Box

Message Box. Show(Nội dung thông báo, Tiêu đề, Kiểu chức năng, Kiểu biểu tượng);

## Nội dung thông

báo được đặt trong nháy kép

Message Box. Show( "Bạn chưa nhập dữ liệu", "Thông báo", Message Box Buttons

## .OK,

Message Box Icon. Inf ormation);

23/05/2026 Chương 4. Lập trình giao diện trong Windows 9/51

Hộp thông báo

 Phương thức Message Box. Show trảvềgi á trị của các nút mà người dùng nhấn Message Box. Show(Nội dung thông báo, Tiêu đề, Kiểu chức năng, Kiểu biểu tượng) = Giá trịtr ảvề  Các giá trịtr ảvề:

◼ System. Windows. Forms. Dialog Result.OK ◼ System. Windows. Forms. Dialog Result. Cancel ◼ System. Windows. Forms. Dialog Result. Abort ◼ System. Windows. Forms. Dialog Result. Retry ◼ System. Windows. Forms. Dialog Result. Ignore ◼ System. Windows. Forms. Dialog Result. Yes ◼ System. Windows. Forms. Dialog Result. No private void btt Thoat_Click(object sender, Event Args e) { if (Message Box. Show("Bạn có muốn thoát khỏi chương trình không?", "Thông báo", Message Box Buttons. Yes No, Message Box Icon. Question) == System. Windows. Forms. Dialog Result. Yes) Application. Exit(); //Thoát chương trình }

23/05/2026 Chương 4. Lập trình giao diện trong Windows 10/51

Các điều khiển

Điều khiển thông thường:

◼ Label, Text Box, Combobox, List Box, Check Box, Ra dio Button, Button Điều khiển đặc biệt:

◼ Tooltip, Help Provider, Error Provider, Progress Bar, List View, Tree View, Date Time Picker, Monthly Calender Điều khiển Menu Điều khiển container:

◼ Group Box, Tab Control, Panel v. v….

23/05/2026 Chương 4. Lập trình giao diện trong Windows 11/51

Form

Các thuộc tính <47&gt;

Thuộc tính Mô tả Name Tên form, bắt đầu bằng frm Is Mdi Container Trạng thái SDI, MDI Back Color Màu nền Background Image Hình nền trên form Accept Button Nút xử lý mặc định - phím Enter Cancel Button Nút xử lý mặc định - Phím Esc Form Border Style Đường viền cho form Enabled True/False: cho phép/không cho phép tác động Font Font chữcho các điều khiển trên form Fore Color Màu cho các điều khiển trên form Icon Icon cho form

23/05/2026 Chương 4. Lập trình giao diện trong Windows 12/51

| Thuộc tính | Mô tả |
| --- | --- |
| Name | Tên form, bắt đầu bằng frm |
| IsMdiContainer | Trạng thái SDI, MDI |
| BackColor | Màu nền |
| BackgroundImage | Hình nền trên form |
| AcceptButton | Nút xử lý mặc định - phím Enter |
| CancelButton | Nút xử lý mặc định - Phím Esc |
| FormBorderStyle | Đường viền cho form |
| Enabled | True/False: cho phép/không cho phép tác động |
| Font | Font chữ cho các điều khiển trên form |
| ForeColor | Màu cho các điều khiển trên form |
| Icon | Icon cho form |

Form

Các thuộc tính

Thuộc tính Mô tả Main Menu Strip Menu chính Context Menu Menu ngữc ảnh Opacity Độtrong suốt (0%-100%) Start Position Vị trí xuất hiện Text Tiêu đề cho form Window State Trạng thái của form khi chạy chương trình: Normal, Maximized, Minimized) Show In Taskbar Hiển thị trên Taskbar Maximize Box True/False: Có/không hiển thị nút phóng lớn Minimize Box True/False: Có/không hiển thị nút thu nhỏ

23/05/2026 Chương 4. Lập trình giao diện trong Windows 13/51

| Thuộc tính | Mô tả |
| --- | --- |
| MainMenuStrip | Menu chính |
| ContextMenu | Menu ngữ cảnh |
| Opacity | Độ trong suốt (0%-100%) |
| StartPosition | Vị trí xuất hiện |
| Text | Tiêu đề cho form |
| WindowState | Trạng thái của form khi chạy chương trình: Normal,
Maximized, Minimized) |
| ShowInTaskbar | Hiển thị trên Taskbar |
| MaximizeBox | True/False: Có/không hiển thị nút phóng lớn |
| MinimizeBox | True/False: Có/không hiển thị nút thu nhỏ |

Form

Các sự kiện ◼ Nhấn đểhi ển thịdanh sách các sự kiện ◼ Nháy đúp chuột vào tên sự kiện để vào cửa sổ viết mã lệnh

Sự kiện Mô tả Load Khi form được nạp vào bộ nhớ, thường dùng khởi tạo giá trị và trạng thái cho các biến, điều khiển trên form Click Người dùng nhấn chuột Form Closed Khi người dùng nhấn nút Close x Form Closing Khi người dùng nhấn nút close x (trước sự kiện Form Closed)

23/05/2026 Chương 4. Lập trình giao diện trong Windows 14/51

| Sự kiện | Mô tả |
| --- | --- |
| Load | Khi form được nạp vào bộ nhớ, thường dùng khởi tạo giá
trị và trạng thái cho các biến, điều khiển trên form |
| Click | Người dùng nhấn chuột |
| FormClosed | Khi người dùng nhấn nút Close x |
| FormClosing | Khi người dùng nhấn nút close x (trước sự kiện
FormClosed) |

Form

Các phương thức

Phương thức Mô tả Close Đóng form Hide Ẩn form Show Hiển thị form chế độ thông thường (modeless) Show Dialog Hiển thị form như hộp thoại (model)

23/05/2026 Chương 4. Lập trình giao diện trong Windows 15/51

| Phương thức | Mô tả |
| --- | --- |
| Close | Đóng form |
| Hide | Ẩn form |
| Show | Hiển thị form chế độ thông thường (modeless) |
| ShowDialog | Hiển thị form như hộp thoại (model) |

Textbox

Thuộc tính

Thuộc tính Mô tả Name Tên, bắt đầu bằng txt Back Color Màu nền Enabled True/False: bật/tắt textbox Font Font chữ Fore Color Màu chữ Locked True/false: khoá/không khoá Max Length Chiều dài tối đa (0-32767) Multiline True: cho phép nhiều dòng Password Char Hiển thịk í tựn ày thay cho kí tựnh ập vào Read Only Chỉđ ọc

23/05/2026 Chương 4. Lập trình giao diện trong Windows 16/51

| Thuộc tính | Mô tả |
| --- | --- |
| Name | Tên, bắt đầu bằng txt |
| BackColor | Màu nền |
| Enabled | True/False: bật/tắt textbox |
| Font | Font chữ |
| ForeColor | Màu chữ |
| Locked | True/false: khoá/không khoá |
| MaxLength | Chiều dài tối đa (0-32767) |
| Multiline | True: cho phép nhiều dòng |
| PasswordChar | Hiển thị kí tự này thay cho kí tự nhập vào |
| ReadOnly | Chỉ đọc |

Textbox

Thuộc tính

Thuộc tính Mô tả Scroll Bars Thanh cuốn ngang, dọc (có hiệu lực khi Multiline = true, thanh cuốn ngang có hiệu lực khi Word Wrap=False) Tab Index Thứt ựtruy cập của hộp văn bản khi người dùng bấm phím Tab, thứt ựđầu tiên là 0.

Text Chứa nội dung của hộp văn bản.

Text Align Căn lề Visible True/False: ẩn/hiện Word Wrap Word Wrap = True: dòng văn bản được tựđộng cuộn xuống dòng khi gặp lềb ên phải của hộp Text Box, ngược lại thì nhận giá trịFalse. Chỉcó hiệu lực khi Multiline = True.

23/05/2026 Chương 4. Lập trình giao diện trong Windows 17/51

| Thuộc tính | Mô tả |
| --- | --- |
| ScrollBars | Thanh cuốn ngang, dọc (có hiệu lực khi Multiline =
true, thanh cuốn ngang có hiệu lực khi
WordWrap=False) |
| TabIndex | Thứ tự truy cập của hộp văn bản khi người dùng bấm
phím Tab, thứ tự đầu tiên là 0. |
| Text | Chứa nội dung của hộp văn bản. |
| TextAlign | Căn lề |
| Visible | True/False: ẩn/hiện |
| WordWrap | WordWrap = True: dòng văn bản được tự động cuộn
xuống dòng khi gặp lề bên phải của hộp TextBox, ngược lại thì nhận giá trị False. Chỉ có hiệu lực khi
Multiline = True. |

Textbox

Sự kiện

Sự kiện Mô tả Text Changed Có sựthay đổi trong hộp văn bản Click Nháy chuột Double Click Nháy đúp chuột Got Focus Khi chuyển tiêu điểm tới hộp văn bản.

Key Press Trảvềk ý tự(trừ các ký tựđ ặc biệt như phím Delete, Home, Ctrl, F1…) mà người sử dụng gõ vào hộp văn bản thông qua thuộc tính Key Char.

Key Do wn Trảvềm ã ASCII của tất cả các ký tựm à người sử dụng gõ vào hộp văn bản thông qua thuộc tính Key Code.

Lost Focus Được kích hoạt khi hộp văn bản mất tiêu điểm.

Mouse Move Di chuyển qua hộp văn bản Mouse Leave Di chuyển ra khỏi hộp văn bản

23/05/2026 Chương 4. Lập trình giao diện trong Windows 18/51

| Sự kiện | Mô tả |
| --- | --- |
| TextChanged | Có sự thay đổi trong hộp văn bản |
| Click | Nháy chuột |
| DoubleClick | Nháy đúp chuột |
| GotFocus | Khi chuyển tiêu điểm tới hộp văn bản. |
| KeyPress | Trả về ký tự (trừ các ký tự đặc biệt như phím Delete,
Home, Ctrl, F1…) mà người sử dụng gõ vào hộp văn bản
thông qua thuộc tính KeyChar. |
| KeyDown | Trả về mã ASCII của tất cả các ký tự mà người sử dụng
gõ vào hộp văn bản thông qua thuộc tính KeyCode. |
| LostFocus | Được kích hoạt khi hộp văn bản mất tiêu điểm. |
| MouseMove | Di chuyển qua hộp văn bản |
| MouseLeave | Di chuyển ra khỏi hộp văn bản |

Textbox

Phương thức

Phương thức Mô tả Append Text Cộng dồn chuỗi Clear Xoá nội dung trên Textbox Copy Sao chép Cut Cắt Paste Dán Undo Quay về trạng thái cũ Get Char Index From Position Lấy kí tựtại vịtr í Select Chọn

23/05/2026 Chương 4. Lập trình giao diện trong Windows 19/51

| Phương thức | Mô tả |
| --- | --- |
| AppendText | Cộng dồn chuỗi |
| Clear | Xoá nội dung trên Textbox |
| Copy | Sao chép |
| Cut | Cắt |
| Paste | Dán |
| Undo | Quay về trạng thái cũ |
| GetCharIndexFromPosition | Lấy kí tự tại vị trí |
| Select | Chọn |

Textbox

23/05/2026 Chương 4. Lập trình giao diện trong Windows 20/51

Textbox - Ví dụ

◼ Hiển thịm ã ASCII của kí tựb ất kì nhập vào Textbox1 private void text Box1_Key Do wn(object sender, Key Event Args e) { int a;

a = Convert.ToInt32(e. Key Code);

Message Box. Show(a. To String());

} ◼ Chỉ cho phép nhập số 0-9, dấu -, chấm., phím del (mã ASCII 13) và backspace (mã ASCII 8) private void text Box1_Key Press(object sender, Key Press Event Args e) { if (((e. Key Char >= '0') && (e. Key Char <= '9')) || (e. Key Char == '-') || (e. Key Char == '.') || (Convert.ToInt32(e. Key Char) == 8)

|| (Convert.ToInt32(e.KeyChar) == 13))

e. Handled = false;

else e. Handled = true;

}

23/05/2026 Chương 4. Lập trình giao diện trong Windows 21/51

Masked Textbox

23/05/2026 Chương 4. Lập trình giao diện trong Windows 22/51

Label - nhãn

Label:

◼ Trình bày, chú giải tiêu đề ◼ Có hai loại Label và Link Label ◼ Name: bắt đầu bằng lbl

23/05/2026 Chương 4. Lập trình giao diện trong Windows 23/51

Button - nút nhấn

Dùng chuột nhấn đểthao tác Có thểshow Icon trên button

23/05/2026 Chương 4. Lập trình giao diện trong Windows 24/51

Button

Thuộc tính

Thuộc tính Mô tả Name Tên, bắt đầu bằng btn Back Color Màu nền Background Image Ảnh nền Enabled True/False: bật/tắt nút lệnh Font Font chữ Fore Color Màu chữ Image Ảnh trên nút Locked True/False: khoá/không khoá dịch chuyển vịtr í nút Tab Index Thứt ựtruy cập (khi nhấn Tab) Text Tiêu đền út (Thêm dấu & trước kí tựđ ặt phím nóng) Visible True/False: Hiện/Ẩn nút lệnh

23/05/2026 Chương 4. Lập trình giao diện trong Windows 25/51

| Thuộc tính | Mô tả |
| --- | --- |
| Name | Tên, bắt đầu bằng btn |
| BackColor | Màu nền |
| BackgroundImage | Ảnh nền |
| Enabled | True/False: bật/tắt nút lệnh |
| Font | Font chữ |
| ForeColor | Màu chữ |
| Image | Ảnh trên nút |
| Locked | True/False: khoá/không khoá dịch chuyển vị trí nút |
| TabIndex | Thứ tự truy cập (khi nhấn Tab) |
| Text | Tiêu đề nút (Thêm dấu & trước kí tự đặt phím nóng) |
| Visible | True/False: Hiện/Ẩn nút lệnh |

Button

Sự kiện

Sự kiện Mô tả Click Nhấn nút Got Focus Chuyển tiêu điểm tới nút Lost Focus Mất tiêu điểm Mouse Do wn Đặt chuột vào nút Mouse Up Đưa chuột ra khỏi nút Mouse Move Di chuyển chuột trên nút Mouse Leave Dời chuyển ra khỏi nút

23/05/2026 Chương 4. Lập trình giao diện trong Windows 26/51

| Sự kiện | Mô tả |
| --- | --- |
| Click | Nhấn nút |
| GotFocus | Chuyển tiêu điểm tới nút |
| LostFocus | Mất tiêu điểm |
| MouseDown | Đặt chuột vào nút |
| MouseUp | Đưa chuột ra khỏi nút |
| MouseMove | Di chuyển chuột trên nút |
| MouseLeave | Dời chuyển ra khỏi nút |

Group Box - nhóm

Chứa các điều khiển khác, tạo thành các vùng làm việc độc lập trên form

Thuộc tính Mô tả Name Tên nhóm, bắt đầu bằng grb Back Color Thiết lập mầu nền cho nhóm, nếu Back Color = Transparent thì nhóm sẽcó mầu nền giống với mầu nền của Form.

Tab Index Thứt ựtruy cập của nhóm khi người dùng bấm phím Tab.

Text Thiết lập tiêu đềcủa nhóm.

Visible Visible = True: hiển thịnh óm, Visible = False: ẩn nhóm.

23/05/2026 Chương 4. Lập trình giao diện trong Windows 27/51

| Thuộc tính | Mô tả |
| --- | --- |
| Name | Tên nhóm, bắt đầu bằng grb |
| BackColor | Thiết lập mầu nền cho nhóm, nếu BackColor =
Transparent thì nhóm sẽ có mầu nền giống với
mầu nền của Form. |
| TabIndex | Thứ tự truy cập của nhóm khi người dùng bấm
phím Tab. |
| Text | Thiết lập tiêu đề của nhóm. |
| Visible | Visible = True: hiển thị nhóm, Visible = False: ẩn
nhóm. |

Checkbox - Hộp đánh dấu

Cho phép không chọn/chọn một/chọn nhiều khả năng

Thuộc tính Mô tả Name Tên, bắt đầu bằng chk Checked True/false: checkbox đã được chọn/không được chọn Check State Checked: được chọn

Unchecked: không được chọn

Indeterminate: chưa xác định

23/05/2026 Chương 4. Lập trình giao diện trong Windows 28/51

| Thuộc tính | Mô tả |
| --- | --- |
| Name | Tên, bắt đầu bằng chk |
| Checked | True/false: checkbox đã được chọn/không được chọn |
| CheckState | Checked: được chọn
Unchecked: không được chọn
Indeterminate: chưa xác định |

Checkbox - Hộp đánh dấu

Sự kiện

Sư kiện Mô tả Click Nhấn chuột vào checkbox Got Focus Chuyển tiêu điểm vào checkbox Lost Focus Mất tiêu điểm Checked Changed Checkbox thay đổi trạng thái

23/05/2026 Chương 4. Lập trình giao diện trong Windows 29/51

| Sư kiện | Mô tả |
| --- | --- |
| Click | Nhấn chuột vào checkbox |
| GotFocus | Chuyển tiêu điểm vào checkbox |
| LostFocus | Mất tiêu điểm |
| CheckedChanged | Checkbox thay đổi trạng thái |

Ra dio Button - Nút tuỳ chọn

Cho phép người dùng chọn một trong nhiều lựa chọn Thuộc tính

Thuộc tính Mô tả Name Tên, bắt đầu bằng rdo Checked True/false: ra diobutton đã được chọn/ không được chọn Enable True/False: bật/tắt nút tuỳch ọn Visible True/False: Hiện/Ẩn nút

23/05/2026 Chương 4. Lập trình giao diện trong Windows 30/51

| Thuộc tính | Mô tả |
| --- | --- |
| Name | Tên, bắt đầu bằng rdo |
| Checked | True/false: ra diobutton đã được chọn/ không được
chọn |
| Enable | True/False: bật/tắt nút tuỳ chọn |
| Visible | True/False: Hiện/Ẩn nút |

Ra dio Button - Nút tuỳ chọn

Sự kiện

Sư kiện Mô tả Click Nhấn chuột vào nút tuỳch ọn Got Focus Chuyển tiêu điểm vào nút tuỳch ọn Lost Focus Mất tiêu điểm Checked Changed Nút tuỳch ọn thay đổi trạng thái Chú ý ◼ Ra dio Button kết hợp với Group Box

23/05/2026 Chương 4. Lập trình giao diện trong Windows 31/51

| Sư kiện | Mô tả |
| --- | --- |
| Click | Nhấn chuột vào nút tuỳ chọn |
| GotFocus | Chuyển tiêu điểm vào nút tuỳ chọn |
| LostFocus | Mất tiêu điểm |
| CheckedChanged | Nút tuỳ chọn thay đổi trạng thái |

Listbox - Hộp danh sách

Cung cấp danh sách cho phép lựa chọn Hiển thịthanh cuộn nếu vượt quá vùng thểhiện Sự kiện:

Sự kiện Mô tả Click Nháy chuột vào danh sách Double Click Nháy đúp chuột Got Focus Chuyển tiêu điểm tới Lost Focus Mất tiêu điểm Selected Index Changed Thay đổi trạng thái lựa chọn các dòng dữ liệu trong listbox

23/05/2026 Chương 4. Lập trình giao diện trong Windows 32/51

| Sự kiện | Mô tả |
| --- | --- |
| Click | Nháy chuột vào danh sách |
| DoubleClick | Nháy đúp chuột |
| GotFocus | Chuyển tiêu điểm tới |
| LostFocus | Mất tiêu điểm |
| SelectedIndexChanged | Thay đổi trạng thái lựa chọn các dòng dữ liệu
trong listbox |

Listbox - Hộp danh sách

Thuộc tính Mô tả Name Tên hộp List Box, bắt đầu bằng lst Data Source Nguồn dữ liệu cho List Box Multi Column True/False: Nhiều cột Column Width Độr ộng cho mỗi cột trong List Box.

Items Danh sách khởi tạo các phần tử Selected Index Trảvềsốth ứt ựcủa phần tửđang được chọn trong danh sách, phần tửđầu tiên có Selected Index = 0, nếu không có phần tửn ào được chọn thì Selected Index = -1 Selection Mode Chếđộl ựa chọn các phần tử trong hộp danh sách khi thực thi chương trình. None,One,Multi Simple (lựa chọn nhiều phần tửri êng biệt), Multi Extended (chọn một khối các phần từli ền nhau) Selected Items Trảvềtập các phần tửđang được chọn.

Sorted True/False:sắp xếp hay không

23/05/2026 Chương 4. Lập trình giao diện trong Windows 33/51

| Thuộc tính | Mô tả |
| --- | --- |
| Name | Tên hộp ListBox, bắt đầu bằng lst |
| DataSource | Nguồn dữ liệu cho ListBox |
| MultiColumn | True/False: Nhiều cột |
| ColumnWidth | Độ rộng cho mỗi cột trong ListBox. |
| Items | Danh sách khởi tạo các phần tử |
| SelectedIndex | Trả về số thứ tự của phần tử đang được chọn trong
danh sách, phần tử đầu tiên có SelectedIndex = 0, nếu
không có phần tử nào được chọn thì SelectedIndex = -1 |
| SelectionMode | Chế độ lựa chọn các phần tử trong hộp danh sách khi
thực thi chương trình. None,One,MultiSimple (lựa chọn
nhiều phần tử riêng biệt), MultiExtended (chọn một khối
các phần từ liền nhau) |
| SelectedItems | Trả về tập các phần tử đang được chọn. |
| Sorted | True/False:sắp xếp hay không |

Listbox - Hộp danh sách

Phương thức ◼ List Name. Items. Add(Item); //thêm phần tử ◼ List Name. Items. Remove(Item); //xoá phần tử ◼ List Name. Items. Remove At(Index); //xoá tại chỉsố index ◼ List Name. Items. Clear(); //xoá danh sách Ví dụ:

lst Que. Items. Add(“Ha Noi”);

23/05/2026 Chương 4. Lập trình giao diện trong Windows 34/51

Combo Box - Hộp lựa chọn

Cho phép lựa chọn một mục dữ liệu trong hộp danh sách thảxu ống

Thuộc tính Mô tả Name Tên hộp Combo Box, bắt đầu bằng cbo Data Source Nguồn dữ liệu cho Combo Box Drop Do wn Style Các kiểu. Drop Do wn: cho phép chọn và nhập dữ liệu, Simple: Hiển thịto àn bộdanh sách các mục, cho phép nhập. Drop Do wn List: Chỉ cho phép lựa chọn các phần tử trong hộp thảxu ống Items Khởi tạo các giá trịkhi thiết kế Selected Index Số thứt ựcác phần tửđang được chọn

23/05/2026 Chương 4. Lập trình giao diện trong Windows 35/51

| Thuộc tính | Mô tả |
| --- | --- |
| Name | Tên hộp ComboBox, bắt đầu bằng cbo |
| DataSource | Nguồn dữ liệu cho ComboBox |
| DropDownStyle | Các kiểu. DropDown: cho phép chọn và nhập dữ liệu,
Simple: Hiển thị toàn bộ danh sách các mục, cho phép nhập. DropDownList: Chỉ cho phép lựa chọn các phần tử
trong hộp thả xuống |
| Items | Khởi tạo các giá trị khi thiết kế |
| SelectedIndex | Số thứ tự các phần tử đang được chọn |

Combo Box - Hộp lựa chọn

Sự kiện

Sự kiện Mô tả Click Nháy chuột vào danh sách Double Click Nháy đúp chuột Got Focus Chuyển tiêu điểm tới Lost Focus Mất tiêu điểm Selected Index Changed Thay đổi trạng thái lựa chọn các dòng dữ liệu trong Combo Box Text Changed Có sựthay đổi văn bản của Combo Box Drop Do wn Chỉx ảy ra đối với hộp Combo Drop Do wn và Drop Do wn List, sự kiện này được gọi ngay sau khi người dùng nhấp mũi tên đểth ảh ộp danh sách xuống (phím tắt Alt+), sự kiện này chủy ếu được sử dụng đểnh ập dữ liệu cho các phần tử của hộp Combo.

23/05/2026 Chương 4. Lập trình giao diện trong Windows 36/51

|  | Sự kiện | Mô tả |  |
| --- | --- | --- | --- |
|  | Click | Nháy chuột vào danh sách |  |
|  | DoubleClick | Nháy đúp chuột |  |
|  | GotFocus | Chuyển tiêu điểm tới |  |
|  | LostFocus | Mất tiêu điểm |  |
|  | SelectedIndexChanged | Thay đổi trạng thái lựa chọn các dòng dữ liệu
trong ComboBox |  |
|  | TextChanged | Có sự thay đổi văn bản của ComboBox |  |
|  | DropDown | Chỉ xảy ra đối với hộp Combo DropDown và
DropDownList, sự kiện này được gọi ngay sau khi người dùng nhấp mũi tên để thả hộp danh sách xuống (phím tắt Alt+), sự kiện này chủ yếu được sử dụng để nhập dữ liệu cho các phần tử
của hộp Combo. |  |

Combo Box - Hộp lựa chọn

Phương thức ◼ Combo Name. Items. Add(Item); //Thêm ◼ Combo Name. Items. Remove(Item); //xoá ◼ Combo Name. Items. Remove At(Index); //xoá tại vị trí index ◼ Combo Name. Items. Clear(); //xoá tất cả Ví dụ: nhập dữ liệu cho hộp cbo Que private void cbo Que_Drop Do wn(object sender, Event Args e) { cbo Que. Items. Clear();

cbo Que. Items. Add("Hà Nội");

cbo Que. Items. Add("Nam Định");

cbo Que. Items. Add("Đà Lạt");

}

23/05/2026 Chương 4. Lập trình giao diện trong Windows 37/51

Checked List Box

Gần giống như List Box, có thêm checkbox ở đầu dòng Đặt tên bắt đầu bằng clb Có thuộc tính, sự kiện tương tựnh ư List Box Bổ sung thêm ◼ Thuộc tính: Checked Items: tập các phần tửđược check ◼ Sự kiện: Item Check: người dùng nháy đúp chuột

23/05/2026 Chương 4. Lập trình giao diện trong Windows 38/51

Numeric Up Do wn

Lựa chọn một giá trịsốtrong một khoảng giá trịvới bước nhảy xác định

Thuộc tính Mô tả Name Tên, bắt đầu bởi tiếp đầu ngữnud Increment Bước nhảy Maximum Cận trên Minimum Cận dưới Value Giá trịhiện tại

Sự kiện Mô tả Value Changed Thay đổi giá trị của điều khiển

23/05/2026 Chương 4. Lập trình giao diện trong Windows 39/51

| Thuộc tính | Mô tả |
| --- | --- |
| Name | Tên, bắt đầu bởi tiếp đầu ngữ nud |
| Increment | Bước nhảy |
| Maximum | Cận trên |
| Minimum | Cận dưới |
| Value | Giá trị hiện tại |

| Sự kiện | Mô tả |
| --- | --- |
| ValueChanged | Thay đổi giá trị của điều khiển |

Thanh cuộn HScroll Bar và VScroll Bar

Thanh cuộn ngang: HScroll Bar và thanh cuộn dọc VScroll Bar Thuộc tính Mô tả Name Tên thanh cuộn, bắt đầu bởi hsb và vsb.

Minimum Giá trịnh ỏnh ất Maximum Giá trịl ớn nhất Value Giá trị Large Change Mức độthay đổi giá trịkhi cuộn chuột Small Change Mức độthay đổi khi nhấn nút mũi tên trên thanh cuộn (mặc định 1)

Sự kiện Mô tả Value Changed Thay đổi giá trị của điều khiển Scroll Cuộn thanh

23/05/2026 Chương 4. Lập trình giao diện trong Windows 40/51

| Thuộc tính | Mô tả |
| --- | --- |
| Name | Tên thanh cuộn, bắt đầu bởi hsb và vsb. |
| Minimum | Giá trị nhỏ nhất |
| Maximum | Giá trị lớn nhất |
| Value | Giá trị |
| LargeChange | Mức độ thay đổi giá trị khi cuộn chuột |
| SmallChange | Mức độ thay đổi khi nhấn nút mũi tên trên thanh
cuộn (mặc định 1) |

| Sự kiện | Mô tả |
| --- | --- |
| ValueChanged | Thay đổi giá trị của điều khiển |
| Scroll | Cuộn thanh |

Tooltip - dòng chú thích

Tooltip ◼ Điều khiển Tooltip hiển thịthông tin chú thich khi đưa chuột qua

23/05/2026 Chương 4. Lập trình giao diện trong Windows 41/51

Timer - Bộ đếm thời gian

Cho thực thi hành động sau khoảng thời gian

Thuộc tính Mô tả Name Tên điều khiển Timer, bắt đầu bởi tiếp đầu ngữtmr Interval = n là chu kỳth ực hiện sự kiện Tick của điều khiển Timer.

n là số nguyên, được tính bằng mili giây và có giá trị&gt;0 Enabled True/False: cho phép/không cho phép hoạt động

Sự kiện Mô tả Tick Kích hoạt sau mỗi chu kỳInterval Phương thức ◼ Start: kích hoạt (tương tựEnable = True) ◼ Stop: dừng (tương tựEnable = False)

23/05/2026 Chương 4. Lập trình giao diện trong Windows 42/51

| Thuộc tính | Mô tả |
| --- | --- |
| Name | Tên điều khiển Timer, bắt đầu bởi tiếp đầu ngữ tmr |
| Interval | = n là chu kỳ thực hiện sự kiện Tick của điều khiển
Timer.
n là số nguyên, được tính bằng mili giây và có giá trị >0 |
| Enabled | True/False: cho phép/không cho phép hoạt động |

| Sự kiện | Mô tả |
| --- | --- |
| Tick | Kích hoạt sau mỗi chu kỳ Interval |

Rich Text Box

Cho phép tạo/hiển thịcác tập văn bản Rich Text (*. rtf) ◼ Name: bắt đầu bằng rtb Phương thức:

◼ Load File: nạp nội dung ◼ Save File: lưu file

23/05/2026 Chương 4. Lập trình giao diện trong Windows 43/51

Date Time Picker

Cho phép chọn thời gian dưới dạng lịch

Thuộc tính Mô tả Name Tên điều khiển Date Time Picker, bắt đầu bởi dtp Format Định dạng kiểu hiển thịcủa thời gian, Ngày tháng thường chọn giá trịShort Values Gá trịhiện thời

23/05/2026 Chương 4. Lập trình giao diện trong Windows 44/51

| Thuộc tính | Mô tả |
| --- | --- |
| Name | Tên điều khiển DateTimePicker, bắt đầu bởi dtp |
| Format | Định dạng kiểu hiển thị của thời gian, Ngày tháng
thường chọn giá trị Short |
| Values | Gá trị hiện thời |

Windows Media Player

Cho phép nghe nhạc/xem film (tương tựWindows Media Player của Windows) ◼ Đưa công cụvào Tool Box: Nháy phải lên Tool Box, chọn Cho ose Items…, trong mục COM Components chọn Windows Media Player ◼ Bổ sung dòng using WMPLib; //Đểl àm việc với các hàm của Windows Media Player

23/05/2026 Chương 4. Lập trình giao diện trong Windows 45/51

## Bài tập về nhà

Bài 1.

◼ Giao diện:

◼ Yêu cầu:

 Tạo dòng Tool Tip “Nhập số nguyên” cho 2 hộp văn bản ‘Nhập a’ và ‘Nhập b’.

 Chỉ cho phép người dùng nhập số vào hai hộp văn bản.

 Nút Tổng: kiểm tra người dùng phải nhập dữ liệu cho cả hai số a và b, tính tổng các số từa đến b nếu a < b, hoặc tính tổng các số từb đến a nếu b < a, rồi hiển thịkết quả vào nhãn ởph ía dưới.

 Nút Làm lại: xóa các dữ liệu cũ ởcác điều khiển, sau đó đặt con trỏvào hộp văn bản Nhập a.

 Nút Thoát: thoát khỏi chương trình

23/05/2026 Chương 4. Lập trình giao diện trong Windows 46/51

Bài 2.

◼ Giao diện

◼ Yêu cầu:

 Nhập số nguyên dương n, tạo n số nguyên ngẫu nhiên có giá trị từ 1 tới 100 (sử dụng lớp ngẫu nhiên Ra ndom và phương thức Next(n,m) để sinh số ngẫu nhiên trong khoảng n đếm m)

23/05/2026 Chương 4. Lập trình giao diện trong Windows 47/51

◼ Yêu cầu  Chỉ cho phép người dùng nhập số vào hộp văn bản Nhập n.

 Nút Nhập: kiểm tra người dùng phải nhập giá trịcho n, sau đó tạo n số ngẫu nhiên và hiển thịcác số ngẫu nhiên đó ởnh ãn Dẫy số.

 Nút Tính tổng: tính tổng n số ngẫu nhiên và hiển thịkết quảởnh ãn Tổng dẫy số.

 Nút Sắp xếp: sắp xếp n số ngẫu nhiên theo thứt ựt ăng dần và hiển thịkết quảởnh ãn Sắp xếp.

 Nút Làm lại: xóa các dữ liệu cũ ởcác điều khiển, sau đó đặt con trỏvào hộp văn bản Nhập n.

 Nút Thoát: thoát khỏi chương trình

23/05/2026 Chương 4. Lập trình giao diện trong Windows 48/51

Bài 3.

◼ Giao diện

◼ Yêu cầu;

 Chỉđược phép nhập giá trịsốcho Đơn giá và Số lượng, không cho phép nhập dữ liệu vào ô Tổng tiền.

 Nếu Giảm giá được chọn thì hiển thị2 điều khiển giảm giá 5% và 10%, ngược lại không hiển thị2 điều khiển này

23/05/2026 Chương 4. Lập trình giao diện trong Windows 49/51

Giao diện

Yêu cầu:

◼ Chỉ cho phép người dùng chọn 1 trong 4 chuyên ngành: CNTT, HTTTQL, Ngân hàng, Tài chính ◼ Điểm trung bình chỉnh ập số ◼ Nhấn nút nhập hiển thịthông tin cá nhân và xếp

23/05/2026 Chương 4. Lập trình giao diện trong Windows 50/51 loại

◼ Xây dựng các lớp đểth ực hiện xử lý nghiệp vụ như sau  Sinh viên:

◼ Thuộc tính: Ma SV, Ho Ten, Ngay Sinh ◼ Phương thức khởi tạo ◼ string get Infor() trảvềthông tin đầy đủcủa các thuộc tính  Sinh viên chuyên ngành kếth ừa lớp Sinh viên ◼ Bổxung thêm thuộc tính chuyên ngành, điểm trung bình ◼ Bổxung phương thức xếp loại ▪ Điểm trung bình >=5 →xếp loại trung bình ▪ Điểm trung bình >= 7 →xếp loại khá ▪ Điểm trung bình >=8 →xếp loại giỏi ◼ Ghi đè phương thức get Infor() trảvềthông tin các thuộc tính và xếp loại

23/05/2026 Chương 4. Lập trình giao diện trong Windows 51/51

Bài 4.

◼ Giao diện (Máy tính bỏt úi)

◼ Yêu cầu  Người dùng nhấn các nút từ0 đến 9 đểnh ập số  Nhấn các nút + - * / đểl ựa chọn phép toán (khi nhấn xong các nút này thì xoá trắng hộp văn bản)  Nút C đểxo á trắng hộp văn bản  Nút = để tính toán

23/05/2026 Chương 4. Lập trình giao diện trong Windows 52/51

Bài 5. Giải phương trình bậc 2 ◼ Giao diện

◼ Yêu cầu:

 Dùng điều khiển Numeric Up Do wn đểch ọn giá trịcho a, b, c (trong [-100, 100])  Nút Giải PTBH đểth ực hiện giải

23/05/2026 Chương 4. Lập trình giao diện trong Windows 53/51

Bài 6: Sử dụng panel, splitcontainer:

https://www. youtube. com/watch?v=1p LZxy9ZK1M

23/05/2026 Chương 4. Lập trình giao diện trong Windows 54/51
