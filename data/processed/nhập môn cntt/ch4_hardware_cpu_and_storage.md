# Chapter 4: Hardware: The CPU & Storage

## Nội dung chính
- Microchips, miniaturization và mobility.
- Cách dữ liệu được biểu diễn điện tử.
- Bên trong system unit: power supply, motherboard, microprocessor.
- CPU, control unit, ALU, registers và machine cycle.
- Bộ nhớ (Memory), expansion cards, bus lines và ports.
- Secondary storage: hard disks, optical disks, flash storage.
- Xu hướng phát triển trong xử lý và lưu trữ.

## Tổng quan
Chương này giải thích phần cứng bên trong máy tính, đặc biệt là bộ xử lý trung tâm (Central Processing Unit - CPU), bộ nhớ và thiết bị lưu trữ. Người học sẽ hiểu dữ liệu được biểu diễn bằng tín hiệu điện tử, cách CPU thực hiện lệnh và vì sao lưu trữ thứ cấp cần thiết để giữ chương trình, dữ liệu lâu dài.

## Unit 4A: Processing: The System Unit, Microprocessors, & Memory

### 4.1 Microchips, Miniaturization, & Mobility

**Khái niệm chính:**
- Microchip là nền tảng của máy tính hiện đại.
- Miniaturization là xu hướng thu nhỏ linh kiện điện tử.
- Mobility là khả năng dùng thiết bị tính toán khi di chuyển.

**Giải thích:**
Sự phát triển của chip giúp máy tính nhỏ hơn, nhanh hơn và tiết kiệm năng lượng hơn. Nhờ thu nhỏ linh kiện, thiết bị như laptop, tablet và smartphone có thể mang theo dễ dàng nhưng vẫn có năng lực xử lý mạnh.

**Thuật ngữ cần nhớ:**
- `Microchip`: chip điện tử chứa mạch tích hợp.
- `Miniaturization`: quá trình thu nhỏ linh kiện và thiết bị.
- `Mobility`: tính di động của thiết bị.
- `System unit`: khối chứa các thành phần xử lý chính.

**Ví dụ / ứng dụng:**
- Smartphone có system unit dạng cầm tay, còn laptop có màn hình gắn với system unit dạng vỏ sò.

### 4.2 Representing Data Electronically

**Khái niệm chính:**
- Máy tính biểu diễn dữ liệu bằng tín hiệu điện tử.
- Dữ liệu số dùng bit, byte và hệ nhị phân.
- Mọi loại dữ liệu như văn bản, ảnh, âm thanh, video đều được mã hóa thành số.

**Giải thích:**
Máy tính hoạt động với hai trạng thái điện tử, thường biểu diễn là 0 và 1. Một bit là đơn vị nhỏ nhất. Nhiều bit kết hợp thành byte và các đơn vị lớn hơn để biểu diễn ký tự, số, hình ảnh hoặc âm thanh.

| Đơn vị | Giải thích |
|---|---|
| `Bit` | Đơn vị dữ liệu nhỏ nhất, 0 hoặc 1 |
| `Byte` | Nhóm bit, thường dùng biểu diễn ký tự |
| `Binary system` | Hệ nhị phân dùng hai ký hiệu 0 và 1 |
| `Coding scheme` | Quy tắc mã hóa ký tự hoặc dữ liệu |

**Thuật ngữ cần nhớ:**
- `Bit`: chữ số nhị phân.
- `Byte`: đơn vị dữ liệu gồm nhiều bit.
- `Binary`: hệ biểu diễn dữ liệu bằng 0 và 1.

**Ví dụ / ứng dụng:**
- Một bức ảnh kỹ thuật số được lưu bằng các giá trị số mô tả màu sắc của từng điểm ảnh.

### 4.3 Inside the System Unit

**Khái niệm chính:**
- System unit chứa các thành phần xử lý chính.
- Power supply cung cấp điện.
- Motherboard là bảng mạch chính.
- Microprocessor chứa CPU.

**Giải thích:**
System unit là phần thân chính của máy tính để bàn hoặc phần chứa linh kiện chính trong laptop và smartphone. Bên trong có nguồn điện, bo mạch chủ, bộ xử lý, bộ nhớ, bus, cổng kết nối và khe mở rộng.

| Thành phần | Vai trò |
|---|---|
| `Power supply` | Chuyển và cung cấp điện cho hệ thống |
| `Motherboard` | Bảng mạch chính kết nối các thành phần |
| `Microprocessor` | Chip chứa CPU |
| `GPU` | Bộ xử lý đồ họa chuyên xử lý hình ảnh |

**Thuật ngữ cần nhớ:**
- `Motherboard`: bo mạch chủ.
- `Microprocessor`: bộ vi xử lý.
- `GPU`: bộ xử lý đồ họa.
- `System unit`: bộ phận chứa linh kiện xử lý.

**Ví dụ / ứng dụng:**
- Card đồ họa rời hoặc GPU tích hợp giúp xử lý đồ họa, video và trò chơi.

### 4.4 The Central Processing Unit & the Machine Cycle

**Khái niệm chính:**
- CPU là “bộ não” của máy tính.
- CPU gồm control unit và arithmetic/logic unit (ALU).
- Machine cycle là chu trình CPU thực hiện lệnh.

**Giải thích:**
CPU điều khiển và xử lý dữ liệu. Control unit đọc và giải mã lệnh, điều phối tín hiệu đến các bộ phận khác. ALU thực hiện phép toán số học và logic. Mỗi lệnh được thực hiện qua một chu trình gồm lấy lệnh, giải mã, thực thi và lưu kết quả.

**Chu trình máy (Machine Cycle):**
1. Fetch: lấy lệnh từ bộ nhớ.
2. Decode: giải mã lệnh.
3. Execute: thực thi lệnh.
4. Store: lưu kết quả.

**Thuật ngữ cần nhớ:**
- `CPU`: bộ xử lý trung tâm.
- `Control unit`: bộ điều khiển.
- `ALU`: bộ số học/logic.
- `Register`: vùng nhớ tốc độ cao bên trong CPU.
- `Machine cycle`: chu trình xử lý một lệnh.

**Ví dụ / ứng dụng:**
- Khi tính `2 + 3`, CPU lấy lệnh, giải mã phép cộng, ALU tính toán và lưu kết quả.

### 4.5 Memory

**Khái niệm chính:**
- Memory lưu chương trình và dữ liệu đang được xử lý.
- RAM là bộ nhớ tạm thời, mất dữ liệu khi tắt máy.
- ROM là bộ nhớ tương đối cố định.
- Cache giúp tăng tốc truy cập dữ liệu.

**Giải thích:**
Bộ nhớ chính khác với thiết bị lưu trữ lâu dài. Khi chương trình đang chạy, dữ liệu được đưa vào RAM để CPU truy cập nhanh. Cache là bộ nhớ rất nhanh giúp CPU giảm thời gian chờ. ROM chứa thông tin quan trọng ít thay đổi.

| Loại bộ nhớ | Đặc điểm |
|---|---|
| `RAM` | Bộ nhớ truy cập ngẫu nhiên, tạm thời |
| `ROM` | Bộ nhớ chỉ đọc, tương đối cố định |
| `Cache` | Bộ nhớ tốc độ cao hỗ trợ CPU |
| `Flash memory` | Bộ nhớ không mất dữ liệu khi tắt nguồn |

**Thuật ngữ cần nhớ:**
- `Volatile memory`: bộ nhớ mất dữ liệu khi tắt nguồn.
- `Nonvolatile memory`: bộ nhớ không mất dữ liệu khi tắt nguồn.
- `Cache`: bộ nhớ đệm tốc độ cao.

**Ví dụ / ứng dụng:**
- Mở nhiều chương trình cùng lúc cần nhiều RAM hơn.

### 4.6 Expansion Cards, Bus Lines, & Ports

**Khái niệm chính:**
- Expansion cards mở rộng chức năng máy tính.
- Bus lines truyền dữ liệu giữa các thành phần.
- Ports là cổng kết nối thiết bị ngoại vi.

**Giải thích:**
Máy tính có thể được mở rộng bằng card âm thanh, card mạng, card đồ họa hoặc thiết bị khác. Bus là đường truyền bên trong máy tính. Port như USB cho phép kết nối chuột, bàn phím, ổ ngoài hoặc điện thoại.

**Thuật ngữ cần nhớ:**
- `Expansion card`: card mở rộng.
- `Bus`: đường truyền dữ liệu.
- `Port`: cổng kết nối.
- `USB`: chuẩn kết nối phổ biến cho thiết bị ngoại vi.

**Ví dụ / ứng dụng:**
- Cắm ổ USB vào cổng USB để sao chép dữ liệu.

## Unit 4B: Secondary Storage

### 4.7 Secondary Storage

**Khái niệm chính:**
- Secondary storage lưu chương trình và dữ liệu lâu dài.
- Dữ liệu vẫn còn sau khi tắt máy.
- Các loại phổ biến gồm hard disk, optical disc, flash drive và solid-state drive.

**Giải thích:**
RAM chỉ lưu dữ liệu tạm thời, vì vậy máy tính cần thiết bị lưu trữ thứ cấp để giữ hệ điều hành, phần mềm, tài liệu, ảnh, video và dữ liệu người dùng. Ổ cứng truyền thống dùng đĩa từ, SSD dùng bộ nhớ flash, optical disc dùng công nghệ quang.

| Thiết bị | Đặc điểm |
|---|---|
| `Hard disk` | Lưu trữ từ tính, dung lượng lớn |
| `Optical disc` | CD, DVD, Blu-ray, đọc ghi bằng laser |
| `Flash drive` | Nhỏ gọn, dùng bộ nhớ flash |
| `SSD` | Ổ trạng thái rắn, nhanh hơn ổ cứng cơ |
| `Memory card` | Thẻ nhớ cho camera, điện thoại, thiết bị di động |

**Thuật ngữ cần nhớ:**
- `Secondary storage`: lưu trữ thứ cấp, lưu lâu dài.
- `Hard disk`: ổ cứng.
- `Solid-state drive`: ổ SSD.
- `Optical storage`: lưu trữ quang.

**Ví dụ / ứng dụng:**
- Ổ cứng trong máy tính lưu hệ điều hành và phần mềm.
- USB flash drive dùng để mang dữ liệu giữa các máy.

### 4.8 Future Developments in Processing and Storage

**Khái niệm chính:**
- Xử lý và lưu trữ tiếp tục phát triển theo hướng nhanh hơn, nhỏ hơn và dung lượng lớn hơn.
- Các công nghệ mới giúp tăng hiệu năng và giảm tiêu thụ năng lượng.

**Giải thích:**
Nhu cầu dữ liệu ngày càng lớn làm tăng yêu cầu về CPU, bộ nhớ và lưu trữ. Thiết bị tương lai cần xử lý nhiều dữ liệu hơn, hỗ trợ đa phương tiện, trí tuệ nhân tạo và kết nối di động.

**Thuật ngữ cần nhớ:**
- `Processing power`: năng lực xử lý.
- `Storage capacity`: dung lượng lưu trữ.
- `Mobility`: khả năng di động.

**Ví dụ / ứng dụng:**
- Thiết bị di động ngày càng có bộ nhớ lớn và bộ xử lý mạnh hơn để chạy ứng dụng phức tạp.

## Tóm tắt chương
- Dữ liệu trong máy tính được biểu diễn bằng bit và byte.
- System unit chứa power supply, motherboard, microprocessor, memory và các cổng kết nối.
- CPU gồm control unit và ALU, thực hiện lệnh theo machine cycle.
- Memory dùng cho dữ liệu đang xử lý; secondary storage dùng lưu lâu dài.
- Expansion cards, bus lines và ports giúp kết nối, mở rộng hệ thống.
- Xu hướng phần cứng là thu nhỏ, tăng tốc, tăng dung lượng và tăng tính di động.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Microchip | Chip chứa mạch tích hợp |
| System Unit | Khối chứa các thành phần xử lý chính |
| CPU | Bộ xử lý trung tâm |
| Control Unit | Bộ điều khiển trong CPU |
| ALU | Bộ số học và logic |
| Machine Cycle | Chu trình CPU xử lý lệnh |
| RAM | Bộ nhớ tạm thời |
| ROM | Bộ nhớ chỉ đọc |
| Cache | Bộ nhớ đệm tốc độ cao |
| Bus | Đường truyền dữ liệu nội bộ |
| Port | Cổng kết nối thiết bị |
| Secondary Storage | Thiết bị lưu trữ lâu dài |

## Câu hỏi ôn tập
1. Microchip có vai trò gì trong máy tính hiện đại?
2. Bit và byte khác nhau như thế nào?
3. Motherboard có chức năng gì?
4. CPU gồm những bộ phận chính nào?
5. Hãy mô tả bốn bước của machine cycle.
6. RAM khác secondary storage như thế nào?
7. Expansion card dùng để làm gì?
8. Nêu ba loại thiết bị lưu trữ thứ cấp.
9. Vì sao xu hướng miniaturization quan trọng?
