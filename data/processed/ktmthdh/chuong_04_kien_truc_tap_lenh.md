# Chương 4: Kiến trúc tập lệnh

## Nội dung chính
- Khái niệm tập lệnh, lệnh máy và lệnh hợp ngữ.
- Chu kỳ lệnh và trạng thái thực hiện lệnh.
- Cấu trúc lệnh mã máy: opcode và operands.
- Các kiểu lệnh và kiểu toán hạng.
- Số lượng toán hạng và các kiểu thao tác lệnh.

## Tổng quan
Kiến trúc tập lệnh (`Instruction Set Architecture`) là phần giao diện giữa phần mềm và phần cứng CPU. Chương này trình bày cách lệnh được biểu diễn, các nhóm lệnh thường gặp, toán hạng và chu kỳ thực hiện lệnh.

## Giới thiệu tập lệnh

### Lệnh máy và lệnh hợp ngữ

**Khái niệm chính:**
- Mỗi bộ xử lý có một tập lệnh xác định.
- Lệnh máy là chuỗi bit nhị phân mà CPU hiểu và thực hiện trực tiếp.
- Lệnh hợp ngữ là dạng ký hiệu gợi nhớ của lệnh máy.

**Giải thích:**
Người lập trình khó viết trực tiếp bằng chuỗi bit, vì vậy hợp ngữ dùng các ký hiệu như `MOV`, `ADD`, `LOAD`, `STORE` để biểu diễn lệnh máy ở dạng dễ đọc hơn.

## Chu kỳ lệnh

### Trạng thái thực hiện lệnh

**Sơ đồ / Cấu trúc / Quy trình:**
1. Lấy lệnh từ bộ nhớ.
2. Giải mã lệnh.
3. Xác định địa chỉ toán hạng nếu cần.
4. Lấy toán hạng.
5. Thực hiện thao tác.
6. Ghi kết quả.
7. Kiểm tra ngắt nếu hệ thống có cơ chế ngắt.

**Giải thích:**
Chu kỳ lệnh có thể được mô tả ở dạng không kiểm tra ngắt hoặc có kiểm tra ngắt. Khi có ngắt, CPU có thể tạm dừng luồng lệnh hiện tại để phục vụ sự kiện cần xử lý.

## Cấu trúc lệnh mã máy

### Opcode và operands

**Khái niệm chính:**
- `Opcode` cho biết thao tác cần thực hiện.
- `Operand` là toán hạng, cho biết dữ liệu, thanh ghi hoặc địa chỉ liên quan.

**Quy trình / Mô hình / Ký hiệu:**
| Thành phần | Ý nghĩa |
|---|---|
| Opcode | Mã thao tác, ví dụ cộng, trừ, chuyển dữ liệu. |
| Operand | Dữ liệu, thanh ghi, địa chỉ bộ nhớ hoặc cổng vào/ra. |

**Ví dụ / Minh họa:**
- `ADD R1, R2` có thể hiểu là cộng nội dung thanh ghi `R2` vào `R1`, tùy quy ước tập lệnh.

## Các kiểu lệnh

### Nhóm lệnh chính

**Khái niệm chính:**
- Lệnh xử lý dữ liệu.
- Lệnh lưu trữ dữ liệu.
- Lệnh di chuyển dữ liệu.
- Lệnh điều khiển thứ tự thực hiện lệnh.

### Các kiểu thao tác

**Quy trình / Mô hình / Ký hiệu:**
| Kiểu thao tác | Ví dụ lệnh |
|---|---|
| Chuyển dữ liệu | `MOVE`, `LOAD`, `STORE`, `EXCHANGE`, `PUSH`, `POP` |
| Số học | `ADD`, `SUBTRACT`, `MULTIPLY`, `DIVIDE` |
| Logic | `AND`, `OR`, `NOT`, `XOR` |
| Vào/ra | Đọc/ghi dữ liệu với thiết bị hoặc cổng I/O |
| Điều khiển hệ thống | Thay đổi trạng thái hoặc cấu hình hệ thống |
| Chuyển điều khiển | Nhảy, gọi chương trình con, trở về |

## Toán hạng và số lượng toán hạng

### Kiểu toán hạng

**Khái niệm chính:**
- Toán hạng có thể là số, ký tự, giá trị logic, địa chỉ hoặc thanh ghi.
- Kiểu toán hạng quyết định cách CPU diễn giải chuỗi bit.

### Lệnh theo số toán hạng

**Quy trình / Mô hình / Ký hiệu:**
| Dạng lệnh | Đặc điểm |
|---|---|
| 3 toán hạng | Chỉ rõ hai nguồn và một đích. |
| 2 toán hạng | Một toán hạng thường vừa là nguồn vừa là đích. |
| 1 toán hạng | Toán hạng còn lại thường ngầm định trong CPU. |
| 0 toán hạng | Thường dùng với kiến trúc stack, toán hạng nằm trên ngăn xếp. |

**Lưu ý:**
- Lệnh nhiều toán hạng có thể rõ ràng hơn nhưng mã lệnh dài hơn.
- Lệnh ít toán hạng có thể ngắn hơn nhưng cần quy ước ngầm định.

## Chế độ địa chỉ

### Addressing mode

**Khái niệm chính:**
- Chế độ địa chỉ cho biết cách xác định toán hạng của lệnh.
- Toán hạng có thể nằm trong lệnh, trong thanh ghi, trong bộ nhớ hoặc được xác định gián tiếp.

**Giải thích:**
Chế độ địa chỉ ảnh hưởng đến độ linh hoạt của tập lệnh và số chu kỳ cần để lấy toán hạng.

## Tóm tắt chương
- Tập lệnh là tập các lệnh mà CPU có thể hiểu và thực hiện.
- Lệnh máy là mã nhị phân; lệnh hợp ngữ là ký hiệu gợi nhớ.
- Lệnh thường gồm opcode và operand.
- Các nhóm lệnh chính gồm chuyển dữ liệu, số học, logic, vào/ra và chuyển điều khiển.
- Số lượng toán hạng và chế độ địa chỉ ảnh hưởng đến cách chương trình được viết và thực hiện.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Instruction set | Tập lệnh của bộ xử lý. |
| Machine instruction | Lệnh máy ở dạng nhị phân. |
| Assembly instruction | Lệnh hợp ngữ ở dạng ký hiệu gợi nhớ. |
| Opcode | Mã thao tác trong lệnh. |
| Operand | Toán hạng của lệnh. |
| Addressing mode | Chế độ địa chỉ xác định cách tìm toán hạng. |
| Interrupt | Ngắt, sự kiện làm CPU tạm dừng luồng lệnh hiện tại để xử lý. |

## Câu hỏi ôn tập
1. Tập lệnh của bộ xử lý là gì?
2. Phân biệt lệnh máy và lệnh hợp ngữ.
3. Opcode và operand có vai trò gì?
4. Trình bày các bước cơ bản của chu kỳ lệnh.
5. Nêu các nhóm lệnh thường gặp trong tập lệnh.
6. So sánh lệnh 3 toán hạng, 2 toán hạng, 1 toán hạng và 0 toán hạng.
7. Chế độ địa chỉ dùng để làm gì?
8. Vì sao cần kiểm tra ngắt trong chu kỳ lệnh?
