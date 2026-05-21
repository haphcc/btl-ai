# Chương 2: Các mô hình truyền thông

## Nội dung chính
- Cơ sở lý thuyết truyền thông mạng.
- Địa chỉ, giao thức và nhu cầu mô hình hóa truyền thông.
- Phương pháp phân tầng và mô hình truyền thông nhiều tầng.
- Mô hình truyền thông 3 tầng.
- Chuẩn hóa mạng, IEEE 802, OSI và TCP/IP.

## Tổng quan
Chương này giải thích vì sao truyền thông mạng cần được chia thành các tầng và chuẩn hóa. Người học cần hiểu vai trò của địa chỉ, giao thức, gói tin, header, mô hình OSI và mô hình TCP/IP trong quá trình các máy tính trao đổi dữ liệu.

## Cơ sở truyền thông mạng

### Địa chỉ và giao thức

**Khái niệm chính:**
- Thiết bị trên mạng cần có địa chỉ phân biệt để gửi và nhận dữ liệu.
- Giao thức (`protocol`) là tập quy tắc quy định cách các thực thể truyền thông trao đổi thông tin.
- Địa chỉ mạng xác định máy hoặc nút mạng; địa chỉ ứng dụng xác định tiến trình/dịch vụ trên máy.

**Giải thích:**
Nếu không có địa chỉ, mạng không biết chuyển dữ liệu đến đâu. Nếu không có giao thức, hai bên không thống nhất được cách đóng gói, gửi, nhận, kiểm tra lỗi và xử lý dữ liệu.

## Nhu cầu có mô hình truyền thông

### Ví dụ truyền file giữa hai máy

**Mô hình / Quy trình / Cấu trúc:**
Khi truyền một file, hệ thống cần thực hiện nhiều việc:
- Biết địa chỉ máy nhận.
- Xác định máy nhận đang sẵn sàng.
- Kiểm tra chương trình nhận file đã sẵn sàng.
- Chuyển đổi cấu trúc file nếu hai hệ thống khác nhau.
- Thông báo địa chỉ cho mạng để dữ liệu được chuyển đến đúng nơi.

**Giải thích:**
Quá trình truyền file có nhiều chức năng độc lập. Nếu tất cả được viết chung trong một khối lớn, hệ thống khó thiết kế, khó sửa và khó chuẩn hóa. Vì vậy truyền thông được chia thành các module/tầng.

### Chia thành module

**Mô hình / Quy trình / Cấu trúc:**
- Module truyền và nhận file: xử lý yêu cầu ứng dụng.
- Module truyền thông: đảm bảo dữ liệu được trao đổi đúng giữa hai hệ thống.
- Module tiếp cận mạng: đưa dữ liệu vào môi trường truyền vật lý.

## Phương pháp phân tầng

### Nguyên tắc phân tầng

**Khái niệm chính:**
- Mỗi tầng đảm nhiệm một nhóm chức năng rõ ràng.
- Tầng dưới cung cấp dịch vụ cho tầng trên.
- Các thực thể cùng tầng trao đổi với nhau theo giao thức cùng tầng.
- Khi gửi dữ liệu, mỗi tầng có thể bổ sung thông tin điều khiển như header.

**Giải thích:**
Phân tầng giúp giảm độ phức tạp. Khi thay đổi công nghệ ở một tầng, các tầng khác có thể ít bị ảnh hưởng nếu giao diện dịch vụ được giữ ổn định.

### Gói tin và header

**Khái niệm chính:**
- Dữ liệu được đóng gói thành packet.
- Header chứa thông tin điều khiển như địa chỉ, số thứ tự gói tin, mã kiểm tra lỗi hoặc thông tin giao thức.
- Bên nhận dùng header để xử lý và khôi phục dữ liệu.

## Mô hình truyền thông 3 tầng

### Các tầng chính

**Mô hình / Quy trình / Cấu trúc:**
| Tầng | Chức năng |
|---|---|
| Tầng ứng dụng | Cung cấp dịch vụ cho chương trình người dùng như truyền file, email. |
| Tầng truyền dữ liệu/vận chuyển | Điều phối trao đổi dữ liệu giữa hai hệ thống, kiểm soát thứ tự và lỗi. |
| Tầng tiếp cận mạng | Truy nhập môi trường truyền, gửi dữ liệu qua mạng vật lý. |

**Lưu ý:**
- Mô hình 3 tầng là cách nhìn đơn giản, giúp hiểu nền tảng trước khi học OSI hoặc TCP/IP.

## Chuẩn hóa mạng

### Nhu cầu chuẩn hóa

**Khái niệm chính:**
- Chuẩn hóa giúp thiết bị và phần mềm của nhiều nhà sản xuất có thể làm việc với nhau.
- Các tổ chức chuẩn hóa tiêu biểu gồm ISO và CCITT.

### IEEE 802

**Mô hình / Quy trình / Cấu trúc:**
| Chuẩn | Nội dung khái quát |
|---|---|
| IEEE 802 | Họ chuẩn cho mạng LAN/MAN. |
| IEEE 802.2 | Logical Link Control. |
| IEEE 802.3 | Ethernet. |
| IEEE 802.5 | Token Ring. |
| IEEE 802.11 | Mạng LAN không dây. |

## Mô hình OSI

### Bảy tầng OSI

**Mô hình / Quy trình / Cấu trúc:**
| Tầng | Tên | Chức năng chính |
|---|---|---|
| 7 | Application | Cung cấp dịch vụ mạng cho ứng dụng. |
| 6 | Presentation | Biểu diễn, mã hóa, nén dữ liệu. |
| 5 | Session | Thiết lập, quản lý phiên truyền thông. |
| 4 | Transport | Truyền dữ liệu đầu cuối, kiểm soát lỗi/luồng. |
| 3 | Network | Định tuyến và địa chỉ logic. |
| 2 | Data Link | Truyền frame trên liên kết, kiểm soát lỗi liên kết. |
| 1 | Physical | Truyền bit trên môi trường vật lý. |

**Giải thích:**
OSI là mô hình tham chiếu giúp mô tả chức năng truyền thông theo tầng. OSI có thể hỗ trợ giao thức có liên kết và không liên kết.

## Mô hình TCP/IP

### Các tầng TCP/IP

**Mô hình / Quy trình / Cấu trúc:**
| Tầng TCP/IP | Vai trò |
|---|---|
| Application | Dịch vụ ứng dụng như HTTP, FTP, SMTP. |
| Transport | TCP/UDP, truyền dữ liệu đầu cuối. |
| Internet | IP, định tuyến qua liên mạng. |
| Network Access | Truy cập mạng vật lý như Ethernet, Wi-Fi. |

**Lưu ý:**
- TCP/IP là nền tảng hoạt động của Internet.
- OSI thiên về mô hình tham chiếu; TCP/IP là họ giao thức triển khai thực tế rộng rãi.

## Tóm tắt chương
- Truyền thông mạng cần địa chỉ và giao thức.
- Phân tầng giúp giảm độ phức tạp và hỗ trợ chuẩn hóa.
- Dữ liệu được đóng gói với header thành packet.
- OSI gồm 7 tầng; TCP/IP là mô hình giao thức nền tảng của Internet.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Protocol | Giao thức truyền thông. |
| Layer | Tầng trong mô hình truyền thông. |
| Packet | Gói dữ liệu truyền qua mạng. |
| Header | Phần thông tin điều khiển được gắn vào dữ liệu. |
| OSI | Mô hình tham chiếu 7 tầng của ISO. |
| TCP/IP | Họ giao thức nền tảng của Internet. |
| IEEE 802 | Họ chuẩn cho mạng LAN/MAN. |
| Data Link | Tầng liên kết dữ liệu. |

## Câu hỏi ôn tập
1. Vì sao truyền thông mạng cần có địa chỉ?
2. Giao thức mạng là gì?
3. Trong ví dụ truyền file, hệ thống cần thực hiện những công việc nào?
4. Phương pháp phân tầng có lợi ích gì?
5. Header trong gói tin dùng để làm gì?
6. Nêu chức năng của ba tầng trong mô hình truyền thông 3 tầng.
7. Trình bày 7 tầng của mô hình OSI.
8. So sánh khái quát OSI và TCP/IP.
