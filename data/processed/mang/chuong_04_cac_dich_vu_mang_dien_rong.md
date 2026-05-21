# Chương 4: Các dịch vụ mạng diện rộng

## Nội dung chính
- Khái niệm và đặc trưng của mạng WAN.
- Thiết bị và kết nối trong WAN.
- Routing, flow control và congestion control.
- Các công nghệ WAN: leased line, PSTN, ISDN, X.25, Frame Relay, ATM, SMDS.
- Chuyển mạch kênh và chuyển mạch gói.

## Tổng quan
Mạng diện rộng WAN (`Wide Area Network`) kết nối các mạng và thiết bị trên phạm vi địa lý lớn. Chương này trình bày đặc trưng WAN, các thiết bị, công nghệ truyền thông diện rộng và hai mô hình chuyển mạch quan trọng: chuyển mạch kênh và chuyển mạch gói.

## Khái niệm mạng WAN

### Đặc trưng cơ bản

**Khái niệm chính:**
- Kết nối trên phạm vi địa lý lớn.
- Mạng không thuần nhất, có thể gồm nhiều công nghệ và nhà cung cấp.
- Tỷ lệ lỗi thường lớn hơn LAN.
- Tốc độ thường thấp hơn LAN.
- Có thể qua mạng chuyển mạch và dùng địa chỉ toàn cầu.
- Cấu trúc thường có tính phân cấp.

**Giải thích:**
WAN dùng để kết nối các chi nhánh, mạng cục bộ hoặc người dùng ở xa. Vì đi qua hạ tầng truyền thông rộng lớn, WAN cần cơ chế định tuyến, kiểm soát luồng và kiểm soát tắc nghẽn.

## Kết nối và thiết bị WAN

### Kết nối điểm - điểm

**Khái niệm chính:**
- Kết nối điểm - điểm nối hai đầu truyền thông trực tiếp hoặc logic.
- Có thể là kết nối giữa mạng truyền thông với thiết bị đầu cuối hoặc giữa các nút truyền thông.

### Thiết bị WAN

**Mô hình / Quy trình / Cấu trúc:**
| Thiết bị | Vai trò |
|---|---|
| WAN Switch | Chuyển mạch lưu lượng trong mạng WAN. |
| CSU/DSU | Thiết bị đầu cuối kênh dữ liệu, nối thiết bị khách hàng với đường thuê bao số. |
| DTE | Thiết bị đầu cuối dữ liệu. |
| Access Server | Cung cấp truy cập từ xa vào mạng. |
| ISDN Terminal Adapter | Thiết bị kết nối đầu cuối ISDN. |

## Điều khiển trong WAN

### Routing

**Khái niệm chính:**
- Routing là quá trình chọn đường đi cho gói dữ liệu từ nguồn đến đích.
- Trong WAN, routing đặc biệt quan trọng vì dữ liệu có thể đi qua nhiều mạng trung gian.

### Flow control và congestion control

**Khái niệm chính:**
- `Flow control`: kiểm soát luồng để bên gửi không gửi quá khả năng nhận.
- `Congestion control`: kiểm soát tắc nghẽn để tránh quá tải mạng.

**Lưu ý:**
- Hai cơ chế này giúp mạng hoạt động ổn định hơn khi lưu lượng lớn.

## Các công nghệ WAN

### Công nghệ thường gặp

**Mô hình / Quy trình / Cấu trúc:**
| Công nghệ | Đặc điểm khái quát |
|---|---|
| Leased line T1/E1 | Đường thuê riêng tốc độ cố định. |
| Fractional T1/E1 | Thuê một phần dung lượng T1/E1. |
| PSTN | Mạng điện thoại công cộng. |
| ISDN | Mạng số tích hợp dịch vụ. |
| Switch 56 | Dịch vụ chuyển mạch số 56 Kbps. |
| X.25 | Công nghệ chuyển mạch gói truyền thống. |
| Frame Relay | Dịch vụ chuyển mạch gói tốc độ cao hơn X.25. |
| ATM | Truyền dữ liệu bằng cell kích thước cố định. |
| SMDS | Dịch vụ dữ liệu chuyển mạch tốc độ cao. |

## Chuyển mạch kênh

### Circuit switching

**Khái niệm chính:**
- Thiết lập một đường truyền dành riêng giữa hai đầu trước khi truyền dữ liệu.
- Đường có tốc độ không đổi qua mạng.
- Thường dựa trên kỹ thuật ghép kênh theo thời gian (`TDM`).

**Giải thích:**
Chuyển mạch kênh phù hợp với truyền thông yêu cầu kết nối liên tục, nhưng có thể lãng phí tài nguyên nếu đường truyền được giữ trong khi không có dữ liệu.

### Chuyển mạch tương tự và số

**Khái niệm chính:**
- Chuyển mạch tương tự dùng tín hiệu analog.
- Chuyển mạch số dùng tín hiệu digital.
- PSTN là ví dụ quen thuộc trong mạng điện thoại công cộng.

## Chuyển mạch gói

### Packet switching

**Khái niệm chính:**
- Dữ liệu được chia thành các gói.
- Gói đi qua nhiều nút mạng để đến đích.
- Tài nguyên mạng được chia sẻ giữa nhiều luồng dữ liệu.

**Mô hình / Quy trình / Cấu trúc:**
| Phương thức | Đặc điểm |
|---|---|
| Datagram | Mỗi gói có thể đi đường khác nhau, xử lý độc lập. |
| Virtual circuit | Thiết lập đường logic trước, các gói đi theo đường đã xác định. |

**Lưu ý:**
- Chuyển mạch gói tiết kiệm tài nguyên hơn khi lưu lượng dữ liệu không liên tục.

## Tóm tắt chương
- WAN kết nối trên phạm vi địa lý lớn và thường không thuần nhất.
- WAN cần thiết bị và cơ chế như routing, flow control, congestion control.
- Các dịch vụ WAN gồm leased line, PSTN, ISDN, X.25, Frame Relay, ATM.
- Chuyển mạch kênh thiết lập đường dành riêng; chuyển mạch gói chia dữ liệu thành gói để truyền.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| WAN | Mạng diện rộng. |
| Routing | Định tuyến, chọn đường đi cho dữ liệu. |
| Flow control | Kiểm soát luồng truyền dữ liệu. |
| Congestion control | Kiểm soát tắc nghẽn mạng. |
| Circuit switching | Chuyển mạch kênh. |
| Packet switching | Chuyển mạch gói. |
| Datagram | Gói được xử lý độc lập, có thể đi đường khác nhau. |
| Virtual circuit | Đường logic xác định trước trong mạng chuyển mạch gói. |
| ISDN | Mạng số tích hợp dịch vụ. |

## Câu hỏi ôn tập
1. WAN là gì?
2. Nêu các đặc trưng cơ bản của mạng WAN.
3. Kết nối điểm - điểm trong WAN là gì?
4. CSU/DSU và WAN Switch có vai trò gì?
5. Routing khác gì với flow control?
6. Kể tên một số công nghệ WAN.
7. Chuyển mạch kênh hoạt động như thế nào?
8. Phân biệt datagram và virtual circuit trong chuyển mạch gói.
