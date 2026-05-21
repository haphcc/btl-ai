# Chương 5: Mạng Internet

## Nội dung chính
- Lịch sử hình thành Internet từ ARPANET.
- World Wide Web, URL và HTTP.
- Giao thức FTP và truyền tệp.
- Thư điện tử trên Internet.
- VoIP và một số dịch vụ Internet.

## Tổng quan
Chương này trình bày Internet từ góc nhìn lịch sử và dịch vụ. Nội dung tập trung vào ARPANET, TCP/IP, World Wide Web, HTTP, FTP, Email và VoIP - các dịch vụ tiêu biểu hoạt động trên nền Internet.

## Lịch sử Internet

### ARPANET và TCP/IP

**Khái niệm chính:**
- ARPANET là tiền thân quan trọng của Internet.
- ARPA kết nối các địa điểm nghiên cứu đầu tiên như Stanford Research Institute, UCLA, UC Santa Barbara và University of Utah.
- ARPANET bắt đầu năm 1969.
- TCP/IP dần thay thế các giao thức cũ như NCP.
- ARPANET ngừng hoạt động khoảng năm 1990, nhưng Internet tiếp tục phát triển mạnh.

**Ví dụ / Minh họa:**
- Ethernet được phát triển tại Xerox PARC.
- TCP/IP được tích hợp trong UNIX, góp phần phổ biến Internet.
- NSFNET đóng vai trò quan trọng trong mở rộng mạng nghiên cứu.

## World Wide Web

### WWW và URL

**Khái niệm chính:**
- World Wide Web bắt đầu năm 1989 tại CERN.
- Web gồm các trang web và đối tượng web.
- URL xác định vị trí đối tượng web.

**Mô hình / Quy trình / Cấu trúc:**
URL thường gồm:
- Tên máy chủ.
- Đường dẫn đến đối tượng.

### HTTP

**Khái niệm chính:**
- HTTP là giao thức tầng ứng dụng.
- Trình duyệt (`browser`) là client.
- Web server phục vụ yêu cầu từ client.
- HTTP hoạt động trên kết nối TCP.

**Mô hình / Quy trình / Cấu trúc:**
1. Browser mở kết nối TCP đến web server.
2. Browser gửi HTTP request.
3. Web server xử lý yêu cầu.
4. Web server gửi HTTP response.
5. Browser hiển thị nội dung nhận được.

## FTP

### File Transfer Protocol

**Khái niệm chính:**
- FTP dùng để truyền file giữa các máy.
- Người dùng thường cần user name và password.
- FTP server cung cấp dịch vụ lưu trữ và truyền file.
- FTP dùng kết nối điều khiển và kết nối dữ liệu.

**Mô hình / Quy trình / Cấu trúc:**
- Cổng 21: kết nối điều khiển.
- Cổng 20: kết nối dữ liệu trong chế độ truyền thống.
- Lệnh `put`: đưa file lên server.
- Lệnh `get`: tải file từ server.

## Email

### Thành phần hệ thống email

**Khái niệm chính:**
- `User Agent`: chương trình người dùng dùng để soạn, đọc, gửi email.
- `Mail Server`: máy chủ thư lưu và chuyển thư.
- `Mailbox`: hộp thư của người dùng.
- `SMTP`: giao thức gửi/chuyển thư.

**Mô hình / Quy trình / Cấu trúc:**
1. Người gửi soạn thư bằng User Agent.
2. Thư được gửi đến Mail Server của người gửi.
3. SMTP chuyển thư đến Mail Server của người nhận.
4. Thư được lưu trong mailbox.
5. Người nhận dùng User Agent để đọc thư.

## VoIP

### Voice over Internet Protocol

**Khái niệm chính:**
- VoIP truyền thoại qua mạng IP.
- Dựa trên chuyển mạch gói thay vì chuyển mạch kênh truyền thống.
- Các chức năng gồm tạo/quản lý cuộc gọi, nén/giải nén tín hiệu, truyền tín hiệu và chuyển đổi tín hiệu.

**Lưu ý:**
- Chất lượng VoIP phụ thuộc vào độ trễ, mất gói, băng thông và cơ chế điều khiển cuộc gọi.

## Tóm tắt chương
- Internet phát triển từ ARPANET và họ giao thức TCP/IP.
- WWW sử dụng URL để định vị tài nguyên và HTTP để trao đổi nội dung web.
- FTP hỗ trợ truyền file bằng kết nối điều khiển và dữ liệu.
- Email dựa trên User Agent, Mail Server, Mailbox và SMTP.
- VoIP truyền âm thanh qua mạng IP bằng chuyển mạch gói.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| ARPANET | Mạng tiền thân quan trọng của Internet. |
| TCP/IP | Họ giao thức nền tảng của Internet. |
| WWW | World Wide Web, hệ thống tài nguyên web trên Internet. |
| URL | Địa chỉ xác định tài nguyên web. |
| HTTP | Giao thức truyền siêu văn bản. |
| FTP | Giao thức truyền tệp. |
| SMTP | Giao thức gửi/chuyển thư điện tử. |
| VoIP | Truyền thoại qua giao thức Internet. |

## Câu hỏi ôn tập
1. ARPANET có vai trò gì trong lịch sử Internet?
2. Kể tên bốn địa điểm đầu tiên của ARPANET theo nội dung chương.
3. WWW bắt đầu ở đâu và vào khoảng năm nào?
4. URL gồm những phần chính nào?
5. Trình bày quy trình HTTP request/response.
6. FTP dùng cổng 21 và 20 cho mục đích gì?
7. Hệ thống email gồm những thành phần nào?
8. VoIP khác gì với điện thoại chuyển mạch kênh truyền thống?
