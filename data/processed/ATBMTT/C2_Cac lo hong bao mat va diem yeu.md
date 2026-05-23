# CHƯƠNG II
## CÁC LỖ HỔNG BẢO MẬT & ĐIỂM YẾU HỆ THỐNG

# Nội dung

## 2.1 Tổng quan về bảo mật và điểm yếu
## 2.2 Các dạng lỗ hổng trong HDH và ƯD
## 2.3 Quản lý, khắc phục và tăng cường
## 2.4 Một số công cụ rà quét

## 2.1. Tổng quan về lỗ hổng và điểm yếu

- **Mối đe dọa:**
- **Các điểm yếu:**
- **Lỗ hổng bảo mật:**
- **Tấn công:**

$$Tấn công = Mối đe dọa + Lỗ hổng$$

# 2.2. Các dạng lỗ hổng trong HDH và UD

## 2.2.1 Các dạng mối đe dọa

- **Phần mềm độc hại:**
- **Kẻ tấn công ở bên trong**
- **Kẻ tấn công ở bên ngoài:**
- **Hư hỏng phần cứng và phần mềm**
- **Mất trộm các thiết bị:**
- **Tai họa thiên nhiên**
- **Gián điệp công nghệ:**
- **Khủng bố phá hoại**

### 2.2.2 Các loại tấn công

- **Theo mục đích thực hiện**
- **Giả mạo**: Đánh lừa người dùng thông thường
- **Chặn bắt**: Liên quan đến việc nghe lén trên đường truyền và chuyển hướng thông tin để sử dụng trái phép
- **Ngắt quãng**: làm chậm kênh đường truyền hoặc quá tải hệ thống nhằm ngăn cản việc truy cập dịch vụ
- **Sửa đổi**: Sửa đổi thông tin trên đường truyền hoặc sửa đổi dữ liệu file

## 2.2.2 Các loại tấn công

### Theo hình thức thực hiện

- Tấn công chủ động:
- Tấn công thụ động:

### 2.2.3 Các dạng lỗ hổng
- Trong hệ điều hành
    - Lỗ hổng xác thực và quản lý định danh: **Mật khẩu; cơ chế xác thực lỗi thời; tài khoản không còn sử dụng**
    - Lỗ hổng phân quyền và kiểm soát truy cập: **Sai cấu hình quyền file, thư mục, registry**
    - Lỗ hổng kernel, driver và hệ thống lõi
    - Lỗ hổng quản lý bộ nhớ

### 2.2.3 Các dạng lỗ hổng
- **Trong hệ điều hành**
    - Lỗ hổng dịch vụ hệ thống & network stack
    - Lỗ hổng cấu hình HDH
    - Lỗ hổng cập nhật, vá lỗi
    - Lỗ hổng ghi log và giám sát

### 2.2.3 Các dạng lỗ hổng

**Trong Ứng dụng**
- Lỗ hổng xác thực
- Lỗ hổng phân quyền
- Lỗ hổng xử lý đầu vào/đầu ra
- Lỗ hổng quản lý phiên
- Lỗ hổng xử lý file
- Lỗ hổng mã hóa và bảo vệ dữ liệu
- Lỗ hổng cấu hình ứng dụng
- Lỗ hổng thư viện và bên thứ ba

## 2.3.1 Nguyên tắc tổng thể

- **Quản lý theo vòng đời rủi ro**
    - Nhận diện -> Đánh giá -> Xử lý -> Giám sát -> Cải tiến
    - Áp dụng Risk-base Security
- **Phòng thủ nhiều lớp**
    - Con người – Quy trình – Công nghệ
    - Không phụ thuộc một biện pháp đơn lẻ

## 2.3.2 Quản lý khắc phục tăng cường theo nhóm lỗ hổng

- **Xác thực & quản lý định danh (IAM):**

- Xây dựng chính sách IAM tập trung
- Chuẩn hóa quy trình cấp – thu hồi – thay đổi quyền
- Phân tách tài khoản người dùng và quản trị
- Chính sách mật khẩu mạnh
- Vô hiệu hóa tài khoản không sử dụng, loại bỏ tài khoản mặc định

### Phân quyền & kiểm soát truy cập:

- Rà soát quyền định kỳ, loại bỏ quyền dư thừa
- Không chạy dịch vụ với quyền Root/Admin
- Kiểm soát truy cập ở cả frontend và backend

- **Lỗ hổng Kernel, bộ nhớ, thực thi mã:**
    - Kiểm soát driver, kernel module
    - Vá lỗi kịp thời
    - Chặn unsigned driver

### Cấu hình hệ điều hành & dịch vụ:

- Quản lý cấu hình tập trung
- Tắt dịch vụ/ cổng không cần thiết
- Vô hiệu giao thức yếu (Telnet)
- Cấu hình firewall nội bộ

### Quản lý vá lỗi & cập nhật:

- **Phân loại dữ liệu theo mức độ quan trọng**
- **Kiểm tra tương thích trước khi vá**

- **Mã hóa & bảo vệ dữ liệu:**

- Phân loại dữ liệu
- Mã hóa dữ liệu nhạy cảm
- Loại bỏ các thông tin bí mật (hardcoded secrets)

- **Logging, giám sát:**
    - **Chuẩn hóa log**
    - **Ghi log đầy đủ:** danh tính, quyền được phép làm, hoạt động quản trị, các giao dịch thực hiện
    - **Bảo vệ log khỏi chỉnh sửa**

### Bên thứ ba & chuỗi cung ứng:

- **Đánh giá mức độ an toàn của nhà cung cấp**
- **Vá thư viện lỗi thời**
- **Kiểm soát quyền truy cập của đối tác**

## 2.4.1 Công cụ rà quét lỗ hổng, điểm yếu hệ thống

### Công cụ rà quét lỗ hổng bảo mật: Microsoft Baseline Security Analyzer

Microsoft Baseline Security Analyzer -- Webpage Dialog

1 security updates are missing. 3 service packs or update rollups are missing.

Result Details for Windows

Security Updates
Items marked with [X] are confirmed missing. Items marked with [Star] are confirmed missing and are not approved by your system administrator.

| Score | ID | Description | Maximum Severity | Download |
| :--- | :--- | :--- | :--- | :--- |
| [X] | MS09-002 | Cumulative Security Update for Internet Explorer 7 for Windows XP (KB961260) | Critical | [Download Icon] |

Update Rollups and Service Packs
Items marked with [!] are confirmed missing.

| Score | ID | Description | Download |
| :--- | :--- | :--- | :--- |
| [!] | 890830 | Windows Malicious Software Removal Tool - February 2009 (KB890830) | [Download Icon] |
| [!] | 951847 | Microsoft .NET Framework 3.5 Service Pack 1 and .NET Framework 3.5 Family Update (KB951847) x86 | [Download Icon] |
| [!] | 960715 | Update Rollup for ActiveX Killbits for Windows XP (KB960715) | [Download Icon] |

## 2.4.1 Công cụ rà quét lỗ hổng, điểm yếu hệ thống
### Công cụ rà quét lỗ hổng ứng dụng Web: Acunetix Web Vulnerability Scanner

**Acunetix Web Vulnerability Scanner (UGHacker Edition)**

- **File** **Actions** **Tools** **Configuration** **Help**
- **New Scan**
- **Tools Explorer**
- **Web Vulnerability Scanner**
    - **Web Scanner**
    - **Tools**
        - Site Crawler
        - Target Finder
        - Subdomain Scanner
        - Blind SQL Injector
        - HTTP Editor
        - HTTP Sniffer
        - HTTP Fuzzer
        - Authentication Tester
        - Compare Results
    - **Web Services**
        - Web Services Scanner
        - Web Services Editor
    - **Configuration**

**Scan Results**
- **Scan Thread 1 (http://.../)**
    - **Web Alerts (98)**
        - Blind SQL Injection (1)
        - SQL injection (1)
        - Application error message (2)
        - HTML form without CSRF protection (11)
        - User credentials are sent in clear text (1)
        - File upload (3)
        - OPTIONS method is enabled (1)
        - Broken links (71)
        - GHDB: Achievo web-based project management tool (1)
        - Password type input with autocomplete enabled (6)

**Report** | **Start URL:** http://www.rcm.

## 2.4.2 Công cụ quét cổng dịch vụ

- **Cổng 80/443 mở: Dịch vụ web đang hoạt động**
- **Cổng 25 mở: Dịch vụ gửi/nhận mail đang hoạt động**
- **Cổng 53 mở: Dịch vụ tên miền DNS đang hoạt động**

---

**Zenmap**

| Target: 192.168.198.135 | Profile: Intense scan | Scan | Cancel |
| :--- | :--- | :--- | :--- |

**Command:** nmap -T4 -A -v 192.168.198.135

**Nmap Output**

NSE: Script scanning 192.168.198.135.
Initiating NSE at 08:51
Completed NSE at 08:51, 0.16s elapsed
Nmap scan report for 192.168.198.135
Host is up (0.00s latency).
Not shown: 998 closed ports
PORT STATE SERVICE VERSION
22/tcp open ssh OpenSSH 5.3p1 Debian 3ubuntu6 (protocol 2.0)
| ssh-hostkey: 1024 5a:4d:0b:32:5b:7a:de:32:9e:46:76:0c:22:40:cf:0c (DSA)
| _2048 fc:26:6a:bb:45:01:3e:9c:ad:a2:eb:df:fa:27:4e:79 (RSA)
80/tcp open http nginx 0.7.65
| _http-methods: No Allow or Public header in OPTIONS response (status code 405)
| _http-title: Welcome to nginx!
MAC Address: 00:0C:29:BA:90:DC (VMware)

## 2.4.3 Công cụ nghe trộm

*Local Area Connection [Wireshark 1.10.8 (v1.10.8-2-g52a5244 from master-1.10)]

| No. | Time | Source | Destination | Protocol | Length | Info |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 101 | 5.60613800 | 10.10.10.100 | 10.10.10.1 | TCP | 1514 | [TCP segment of a reassembled PDU] |
| 102 | 5.60613900 | 10.10.10.100 | 10.10.10.1 | HTTP | 436 | HTTP/1.1 401 Unauthorized (text/html) |
| 103 | 5.60615900 | 10.10.10.1 | 10.10.10.100 | TCP | 54 | warmspotMgmt > http [ACK] seq=296 ack=184 |
| 111 | 5.78797200 | 10.10.10.100 | 10.10.10.1 | TCP | 60 | [TCP Dup ACK 102#1] http > warmspotMgmt [ |
| 413 | 21.4221450 | 10.10.10.1 | 10.10.10.100 | HTTP | 388 | GET /protected HTTP/1.1 |
| 414 | 21.4232770 | 10.10.10.100 | 10.10.10.1 | TCP | 1514 | [TCP segment of a reassembled PDU] |
| 415 | 21.4232780 | 10.10.10.100 | 10.10.10.1 | HTTP | 319 | HTTP/1.1 401 Unauthorized (text/html) |
| 416 | 21.4233150 | 10.10.10.1 | 10.10.10.100 | TCP | 54 | warmspotMgmt > http [ACK] seq=630 ack=356 |
| 422 | 21.6107570 | 10.10.10.100 | 10.10.10.1 | TCP | 60 | [TCP Dup ACK 415#1] http > warmspotMgmt [ |

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n
Accept-Language: en-US,en;q=0.5\r\n
Accept-Encoding: gzip, deflate\r\n
Connection: keep-alive\r\n
**Authorization: Basic am9lomjsb2dncw==\r\n**
**credentials: joe:bloggs**
\r\n
[Full request URI: http://10.10.10.100/protected]
[HTTP request 2/2]
[Prev request in frame: 100]

0140 65 0d 0a 43 6f 6e 65 65 65 65 65 65 65 65 65 65 e..Conne ction: k 0150 65 65 70 2d 61 6c 6c 6c 65 0d 0a 41 75 74 68 6f eep-aliv e..Autho 0160 72 69 7a 61 74 69 6f 6e 20 3a 20 42 61 73 69 63 rization : Basic
0170 61 6d 39 6c 6f 6d 4a 73 62 32 64 6e 63 77 3d 3d am9lomJs b2dncw==
0180 0d 0a 0d 0a ..

HTTP Authorization header (http.authorizati... Packets: 542 · Displayed: 13 (2.4%) · Droppe... Profile: Default

## Công cụ Wireshark

## 2.4. Một số công cụ rà quét

### 2.4.3 Công cụ ghi bàn phím

**Modul Keylogger**

KeyGrabber

# Thank You !
