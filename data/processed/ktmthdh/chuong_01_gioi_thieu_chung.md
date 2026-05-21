# Chương 1: Giới thiệu chung

## Nội dung chính
- Mục đích, yêu cầu của môn Kiến trúc máy tính.
- Khái niệm kiến trúc máy tính và tổ chức máy tính.
- Máy tính, mô hình cơ bản và mô hình phân lớp của máy tính.
- Phân loại máy tính theo truyền thống và theo cách nhìn hiện đại.
- Chức năng, cấu trúc và hoạt động cơ bản của máy tính.

## Tổng quan
Chương này cung cấp cái nhìn tổng quát về kiến trúc máy tính. Nội dung giúp người học hiểu máy tính được nhìn nhận như một hệ thống gồm phần cứng, phần mềm, bộ xử lý, bộ nhớ, hệ thống vào/ra và bus liên kết hệ thống.

## Mục đích và yêu cầu môn học

### Vai trò của môn học

**Khái niệm chính:**
- Kiến trúc máy tính giúp hiểu cách máy tính được tổ chức và hoạt động ở mức hệ thống.
- Người học cần nắm được chức năng các khối cơ bản và mối liên hệ giữa chúng.
- Kiến thức này là nền tảng cho hệ điều hành, vi xử lý, mạng máy tính và lập trình hệ thống.

**Giải thích:**
Thay vì chỉ sử dụng máy tính như một công cụ, môn học xem xét máy tính từ bên trong: dữ liệu được biểu diễn thế nào, lệnh được thực hiện ra sao, bộ nhớ và thiết bị vào/ra phối hợp với CPU như thế nào.

## Kiến trúc máy tính và tổ chức máy tính

### Kiến trúc máy tính

**Khái niệm chính:**
- Kiến trúc máy tính (`computer architecture`) mô tả các thuộc tính của hệ thống nhìn thấy được đối với người lập trình.
- Các thuộc tính này thường gồm tập lệnh, kiểu dữ liệu, chế độ địa chỉ, thanh ghi và cơ chế vào/ra.

**Giải thích:**
Kiến trúc trả lời câu hỏi máy tính cung cấp những khả năng gì cho chương trình. Ví dụ, một bộ xử lý hỗ trợ những lệnh nào và chương trình có thể truy cập những thanh ghi nào.

### Tổ chức máy tính

**Khái niệm chính:**
- Tổ chức máy tính (`computer organization`) mô tả cách hiện thực các đặc trưng kiến trúc bằng phần cứng.
- Nội dung thường gồm tín hiệu điều khiển, bus, mạch nhớ, ALU và cách nối ghép các thành phần.

**Lưu ý:**
- Cùng một kiến trúc có thể có nhiều tổ chức phần cứng khác nhau.
- Kiến trúc gần với góc nhìn lập trình; tổ chức gần với góc nhìn thiết kế phần cứng.

## Máy tính và phân loại máy tính

### Khái niệm máy tính

**Khái niệm chính:**
- Máy tính là hệ thống điện tử có khả năng nhận dữ liệu, xử lý dữ liệu theo chương trình, lưu trữ dữ liệu và xuất kết quả.
- Chương trình và dữ liệu được lưu trữ trong bộ nhớ dưới dạng nhị phân.

### Phân loại truyền thống

**Quy trình / Mô hình / Ký hiệu:**
| Loại máy tính | Đặc điểm khái quát |
|---|---|
| Bộ vi điều khiển | Hệ thống nhỏ, thường dùng trong thiết bị nhúng. |
| Máy vi tính | Máy tính cá nhân, phục vụ người dùng đơn lẻ. |
| Máy tính nhỏ | Hệ thống trung gian, phục vụ nhóm người dùng hoặc tổ chức nhỏ. |
| Mainframe | Máy tính lớn, xử lý khối lượng dữ liệu và giao dịch lớn. |
| Siêu máy tính | Hệ thống hiệu năng rất cao, dùng cho tính toán khoa học/kỹ thuật. |

### Phân loại hiện đại

**Khái niệm chính:**
- `Desktop computer`: máy tính để bàn phục vụ cá nhân.
- `Server`: máy chủ cung cấp dịch vụ cho nhiều máy khác.
- `Embedded computer`: máy tính nhúng trong thiết bị chuyên dụng.

## Mô hình cơ bản của máy tính

### Các thành phần chính

**Khái niệm chính:**
- Bộ xử lý (`processor`, `CPU`).
- Hệ thống nhớ (`memory`).
- Hệ thống vào/ra (`I/O system`).
- Bus liên kết hệ thống (`system bus`).

**Sơ đồ / Cấu trúc / Quy trình:**
- CPU điều khiển hoạt động và xử lý dữ liệu.
- Bộ nhớ lưu chương trình và dữ liệu.
- Hệ thống vào/ra trao đổi dữ liệu với môi trường bên ngoài.
- Bus truyền địa chỉ, dữ liệu và tín hiệu điều khiển giữa các khối.

### Mô hình phân lớp

**Khái niệm chính:**
- Máy tính có thể được nhìn theo nhiều lớp từ phần cứng đến phần mềm.
- Lớp thấp hơn cung cấp dịch vụ cho lớp cao hơn.

**Giải thích:**
Ở mức thấp là mạch điện và phần cứng số. Trên đó là vi kiến trúc, tập lệnh, hệ điều hành và chương trình ứng dụng. Cách nhìn phân lớp giúp giảm độ phức tạp khi nghiên cứu hệ thống.

## Chức năng và cấu trúc máy tính

### Chức năng cơ bản

**Khái niệm chính:**
- Xử lý dữ liệu.
- Lưu trữ dữ liệu.
- Trao đổi dữ liệu.
- Điều khiển hoạt động.

**Giải thích:**
Mọi hoạt động của máy tính đều có thể quy về bốn chức năng này. CPU thực hiện xử lý và điều khiển; bộ nhớ thực hiện lưu trữ; hệ thống vào/ra thực hiện trao đổi với bên ngoài.

### Bus hệ thống

**Khái niệm chính:**
- Bus địa chỉ truyền địa chỉ ô nhớ hoặc cổng vào/ra.
- Bus dữ liệu truyền dữ liệu giữa các thành phần.
- Bus điều khiển truyền tín hiệu điều khiển, đọc/ghi và đồng bộ.

**Ví dụ / Minh họa:**
- Nếu bus địa chỉ có `N` bit, không gian địa chỉ tối đa là $2^N$ địa chỉ.
- Với bus địa chỉ 32 bit, không gian địa chỉ là $2^{32}$ byte, tương đương 4 GB.

## Hoạt động cơ bản của máy tính

### Chu trình xử lý

**Sơ đồ / Cấu trúc / Quy trình:**
1. CPU lấy lệnh từ bộ nhớ.
2. CPU giải mã lệnh.
3. CPU lấy dữ liệu nếu lệnh yêu cầu.
4. ALU hoặc khối chức năng thực hiện xử lý.
5. Kết quả được ghi vào thanh ghi, bộ nhớ hoặc thiết bị vào/ra.

**Lưu ý:**
- Nguyên lý quan trọng là máy tính hoạt động theo chương trình lưu sẵn trong bộ nhớ.

## Tóm tắt chương
- Kiến trúc máy tính mô tả các đặc trưng nhìn thấy bởi người lập trình.
- Tổ chức máy tính mô tả cách hiện thực các đặc trưng đó bằng phần cứng.
- Máy tính gồm CPU, bộ nhớ, hệ thống vào/ra và bus hệ thống.
- Các chức năng cơ bản gồm xử lý, lưu trữ, trao đổi dữ liệu và điều khiển.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Computer architecture | Kiến trúc máy tính, mô tả đặc trưng hệ thống nhìn từ góc độ lập trình. |
| Computer organization | Tổ chức máy tính, mô tả cách hiện thực phần cứng. |
| CPU | Bộ xử lý trung tâm, điều khiển và xử lý dữ liệu. |
| ALU | Khối số học - logic trong CPU. |
| Control Unit | Khối điều khiển phát tín hiệu điều khiển hoạt động hệ thống. |
| Register | Thanh ghi, bộ nhớ rất nhanh bên trong CPU. |
| Bus | Đường truyền dùng để trao đổi địa chỉ, dữ liệu và tín hiệu điều khiển. |

## Câu hỏi ôn tập
1. Phân biệt kiến trúc máy tính và tổ chức máy tính.
2. Máy tính có những chức năng cơ bản nào?
3. Nêu các thành phần chính trong mô hình cơ bản của máy tính.
4. Bus địa chỉ, bus dữ liệu và bus điều khiển khác nhau như thế nào?
5. Phân biệt desktop computer, server và embedded computer.
6. Vì sao nói máy tính hoạt động theo chương trình lưu sẵn trong bộ nhớ?
7. Nếu bus địa chỉ có 32 bit thì không gian địa chỉ tối đa là bao nhiêu?
