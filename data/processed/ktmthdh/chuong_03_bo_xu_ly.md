# Chương 3: Bộ xử lý

## Nội dung chính
- Cấu trúc chung và chức năng của CPU.
- Nguyên tắc CPU hoạt động theo chương trình lưu trong bộ nhớ.
- Các thành phần chính: Control Unit, ALU và Registers.
- Nhiệm vụ của CPU trong chu kỳ thực hiện lệnh.
- CPU với bus hệ thống và lịch sử phát triển bộ xử lý Intel.

## Tổng quan
Bộ xử lý trung tâm (`CPU`) là thành phần điều khiển hoạt động của hệ thống và xử lý dữ liệu. Chương này mô tả cấu trúc bên trong CPU, các khối chức năng và cách CPU thực hiện chương trình thông qua chu kỳ lệnh.

## Cấu trúc chung của bộ xử lý

### Chức năng của CPU

**Khái niệm chính:**
- Điều khiển hoạt động của toàn hệ thống.
- Xử lý dữ liệu bằng các phép toán số học và logic.
- Trao đổi dữ liệu với bộ nhớ và thiết bị vào/ra thông qua bus.

**Giải thích:**
CPU không làm việc độc lập. Nó nhận lệnh và dữ liệu từ bộ nhớ, phát tín hiệu điều khiển tới các khối khác, thực hiện tính toán và ghi kết quả về nơi cần thiết.

### Cấu trúc cơ bản

**Sơ đồ / Cấu trúc / Quy trình:**
| Thành phần | Chức năng |
|---|---|
| Control Unit | Điều khiển hoạt động của CPU và hệ thống. |
| ALU | Thực hiện phép toán số học và logic. |
| Registers | Lưu thông tin tạm thời trong quá trình xử lý. |

## Nguyên tắc hoạt động của CPU

### Chương trình lưu trong bộ nhớ

**Khái niệm chính:**
- CPU hoạt động theo chương trình đã lưu sẵn trong bộ nhớ.
- Chương trình gồm chuỗi lệnh máy.
- CPU lấy từng lệnh, giải mã và thực hiện.

**Quy trình / Mô hình / Ký hiệu:**
1. `Fetch Instructions`: nhận/lấy lệnh từ bộ nhớ.
2. `Interpret Instructions`: giải mã lệnh.
3. `Fetch Data`: nhận dữ liệu nếu lệnh yêu cầu.
4. `Process Data`: xử lý dữ liệu.
5. `Write Data`: ghi kết quả.

## Các thanh ghi quan trọng

### Program Counter và Instruction Register

**Khái niệm chính:**
- `PC` (`Program Counter`) chứa địa chỉ lệnh tiếp theo cần lấy.
- `IR` (`Instruction Register`) chứa lệnh hiện đang được giải mã hoặc thực hiện.

**Giải thích:**
PC giúp CPU biết phải lấy lệnh ở đâu trong bộ nhớ. Sau khi lệnh được lấy, nó được đưa vào IR để khối điều khiển giải mã và phát tín hiệu điều khiển tương ứng.

### Tập thanh ghi

**Khái niệm chính:**
- Thanh ghi lưu dữ liệu tạm thời, địa chỉ, trạng thái hoặc kết quả trung gian.
- Thanh ghi có tốc độ rất cao vì nằm bên trong CPU.

**Lưu ý:**
- Số lượng và kiểu thanh ghi là một phần quan trọng của kiến trúc bộ xử lý.

## Control Unit và ALU

### Control Unit

**Khái niệm chính:**
- Control Unit giải mã lệnh và phát tín hiệu điều khiển.
- Nó điều phối hoạt động của ALU, thanh ghi, bộ nhớ và vào/ra.

### ALU

**Khái niệm chính:**
- ALU là khối số học - logic.
- ALU thực hiện phép cộng, trừ, so sánh, AND, OR, NOT và các thao tác logic khác.

**Giải thích:**
Khi một lệnh yêu cầu tính toán, dữ liệu được đưa từ thanh ghi vào ALU. Sau khi xử lý, kết quả thường được ghi về thanh ghi hoặc bộ nhớ.

## CPU và bus hệ thống

### Trao đổi với bên ngoài CPU

**Sơ đồ / Cấu trúc / Quy trình:**
- Bus địa chỉ: CPU đưa địa chỉ ô nhớ hoặc cổng vào/ra.
- Bus dữ liệu: CPU trao đổi dữ liệu với bộ nhớ hoặc thiết bị.
- Bus điều khiển: CPU phát tín hiệu đọc, ghi, ngắt và đồng bộ.

**Lưu ý:**
- Độ rộng bus ảnh hưởng đến khả năng địa chỉ hóa và tốc độ trao đổi dữ liệu.

## Lịch sử phát triển bộ xử lý Intel

### Một số mốc tiêu biểu

**Khái niệm chính:**
- 8080: bộ vi xử lý 8 bit thế hệ đầu.
- 8086 và 8088: nền tảng cho kiến trúc x86.
- 80286, 80386, 80486: mở rộng khả năng xử lý và quản lý bộ nhớ.
- Pentium, Pentium Pro, Pentium II, Pentium III, Pentium 4: các thế hệ hiệu năng cao hơn.
- Itanium: dòng xử lý theo hướng kiến trúc khác phục vụ tính toán hiệu năng cao.

**Lưu ý:**
- Danh sách này trong slide dùng để minh họa quá trình phát triển năng lực của CPU qua các thế hệ.

## Tóm tắt chương
- CPU điều khiển hoạt động hệ thống và xử lý dữ liệu.
- CPU gồm Control Unit, ALU và tập thanh ghi.
- CPU thực hiện lệnh qua các bước lấy lệnh, giải mã, lấy dữ liệu, xử lý và ghi kết quả.
- PC chứa địa chỉ lệnh tiếp theo; IR chứa lệnh hiện hành.
- Bus hệ thống giúp CPU trao đổi địa chỉ, dữ liệu và tín hiệu điều khiển.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| CPU | Bộ xử lý trung tâm. |
| Control Unit | Khối điều khiển trong CPU. |
| ALU | Khối số học - logic. |
| Register | Thanh ghi lưu thông tin tạm thời trong CPU. |
| Program Counter | Thanh ghi chứa địa chỉ lệnh tiếp theo. |
| Instruction Register | Thanh ghi chứa lệnh đang được xử lý. |
| Fetch | Giai đoạn lấy lệnh hoặc dữ liệu. |
| Decode | Giai đoạn giải mã lệnh. |

## Câu hỏi ôn tập
1. CPU có những chức năng chính nào?
2. Nêu các thành phần cơ bản trong cấu trúc CPU.
3. Control Unit có nhiệm vụ gì?
4. ALU thực hiện những loại phép toán nào?
5. PC và IR khác nhau như thế nào?
6. Trình bày các bước cơ bản CPU thực hiện một lệnh.
7. CPU trao đổi với bộ nhớ qua những loại bus nào?
8. Kể tên một số thế hệ bộ xử lý Intel được nêu trong chương.
