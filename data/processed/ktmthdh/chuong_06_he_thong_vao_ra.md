# Chương 6: Hệ thống vào/ra

## Nội dung chính
- Tổng quan về hệ thống vào/ra.
- Thiết bị ngoại vi và module vào/ra.
- Chức năng, thành phần của module vào/ra.
- Địa chỉ hóa cổng vào/ra: isolated I/O và memory-mapped I/O.
- Các phương pháp điều khiển vào/ra: programmed I/O, interrupt-driven I/O và DMA.

## Tổng quan
Hệ thống vào/ra (`I/O system`) cho phép máy tính trao đổi thông tin với thế giới bên ngoài. Chương này trình bày thiết bị ngoại vi, module vào/ra, cách địa chỉ hóa cổng và các phương pháp điều khiển vào/ra.

## Tổng quan hệ thống vào/ra

### Chức năng

**Khái niệm chính:**
- Trao đổi thông tin giữa máy tính và môi trường bên ngoài.
- Thao tác cơ bản gồm input và output.
- Hệ thống vào/ra giúp CPU, bộ nhớ và thiết bị ngoại vi phối hợp với nhau.

**Giải thích:**
CPU và bộ nhớ hoạt động với tốc độ và định dạng dữ liệu khác thiết bị ngoại vi. Vì vậy cần module vào/ra để làm trung gian điều khiển và chuyển đổi.

## Thiết bị ngoại vi

### Phân loại thiết bị ngoại vi

**Khái niệm chính:**
- Thiết bị giao tiếp người - máy: bàn phím, màn hình, chuột, máy in.
- Thiết bị giao tiếp máy - máy: thiết bị điều khiển, cảm biến, bộ truyền dữ liệu.
- Thiết bị truyền thông: thiết bị mạng, modem, giao diện truyền thông.

### Thành phần cơ bản

**Sơ đồ / Cấu trúc / Quy trình:**
| Thành phần | Chức năng |
|---|---|
| Transducer | Chuyển đổi tín hiệu vật lý thành tín hiệu điện hoặc ngược lại. |
| Control logic | Điều khiển hoạt động của thiết bị. |
| Buffer | Đệm dữ liệu khi trao đổi với hệ thống. |

**Lưu ý:**
- Thiết bị ngoại vi thường chậm hơn CPU nhiều lần, nên cần cơ chế đệm và điều khiển phù hợp.

## Module vào/ra

### Vì sao cần module vào/ra

**Khái niệm chính:**
- Nối ghép CPU và hệ thống nhớ với thiết bị ngoại vi.
- Che giấu khác biệt về tốc độ, định dạng dữ liệu và tín hiệu điều khiển.
- Hỗ trợ điều khiển, truyền dữ liệu và phát hiện lỗi.

### Chức năng module vào/ra

**Khái niệm chính:**
- Điều khiển và định thời gian.
- Trao đổi thông tin với CPU.
- Trao đổi thông tin với thiết bị ngoại vi.
- Đệm dữ liệu.
- Phát hiện lỗi.

### Thành phần module vào/ra

**Sơ đồ / Cấu trúc / Quy trình:**
| Thành phần | Chức năng |
|---|---|
| Thanh ghi dữ liệu | Chứa dữ liệu trao đổi. |
| Cổng vào/ra | Điểm giao tiếp được CPU truy cập. |
| Thanh ghi điều khiển/trạng thái | Chứa lệnh điều khiển và trạng thái thiết bị. |
| Logic điều khiển | Điều phối hoạt động truyền dữ liệu. |

## Địa chỉ hóa cổng vào/ra

### Isolated I/O

**Khái niệm chính:**
- Vào/ra cách biệt dùng không gian địa chỉ riêng cho cổng I/O.
- CPU dùng lệnh vào/ra riêng để truy cập cổng.

**Giải thích:**
Phương pháp này tách không gian bộ nhớ và không gian vào/ra, giúp phân biệt rõ truy cập bộ nhớ và truy cập thiết bị.

### Memory-mapped I/O

**Khái niệm chính:**
- Vào/ra theo bản đồ bộ nhớ ánh xạ cổng I/O vào không gian địa chỉ bộ nhớ.
- CPU truy cập thiết bị bằng lệnh đọc/ghi bộ nhớ thông thường.

**Quy trình / Mô hình / Ký hiệu:**
| Phương pháp | Đặc điểm |
|---|---|
| Isolated I/O | Không gian địa chỉ I/O riêng, dùng lệnh I/O riêng. |
| Memory-mapped I/O | Cổng I/O nằm trong không gian địa chỉ bộ nhớ. |

## Phương pháp điều khiển vào/ra

### Programmed I/O

**Khái niệm chính:**
- CPU trực tiếp điều khiển quá trình vào/ra bằng chương trình.
- CPU kiểm tra trạng thái thiết bị và truyền dữ liệu.

**Lưu ý:**
- Cách này đơn giản nhưng làm CPU phải chờ thiết bị, hiệu quả thấp khi thiết bị chậm.

### Interrupt-driven I/O

**Khái niệm chính:**
- Thiết bị phát ngắt khi cần CPU phục vụ.
- CPU chỉ xử lý vào/ra khi có sự kiện ngắt.

**Giải thích:**
Ngắt giúp CPU không phải liên tục kiểm tra trạng thái thiết bị. Khi thiết bị sẵn sàng, nó gửi tín hiệu để CPU chuyển sang chương trình phục vụ ngắt.

### DMA

**Khái niệm chính:**
- `DMA` (`Direct Memory Access`) cho phép module DMA truyền dữ liệu trực tiếp giữa thiết bị và bộ nhớ.
- CPU chỉ khởi tạo truyền dữ liệu và nhận thông báo khi hoàn tất.

**Sơ đồ / Cấu trúc / Quy trình:**
1. CPU cấu hình địa chỉ bộ nhớ, thiết bị và lượng dữ liệu.
2. Bộ điều khiển DMA thực hiện truyền dữ liệu.
3. Khi hoàn tất, DMA báo cho CPU, thường bằng ngắt.

**Lưu ý:**
- DMA phù hợp với truyền khối dữ liệu lớn vì giảm tải cho CPU.

## Tóm tắt chương
- Hệ thống vào/ra giúp máy tính trao đổi dữ liệu với bên ngoài.
- Thiết bị ngoại vi cần module vào/ra để nối ghép với CPU và bộ nhớ.
- Module vào/ra có thanh ghi dữ liệu, thanh ghi điều khiển/trạng thái và logic điều khiển.
- Cổng vào/ra có thể được địa chỉ hóa cách biệt hoặc ánh xạ bộ nhớ.
- Các phương pháp điều khiển vào/ra gồm programmed I/O, interrupt-driven I/O và DMA.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| I/O | Vào/ra, quá trình trao đổi dữ liệu với bên ngoài. |
| Peripheral device | Thiết bị ngoại vi. |
| I/O module | Module vào/ra nối ghép thiết bị với hệ thống. |
| Buffer | Bộ đệm dữ liệu. |
| Isolated I/O | Vào/ra cách biệt với không gian địa chỉ riêng. |
| Memory-mapped I/O | Cổng I/O được ánh xạ vào không gian địa chỉ bộ nhớ. |
| Interrupt | Ngắt, tín hiệu yêu cầu CPU phục vụ. |
| DMA | Truy nhập bộ nhớ trực tiếp để truyền dữ liệu không qua CPU từng byte. |

## Câu hỏi ôn tập
1. Hệ thống vào/ra có chức năng gì?
2. Vì sao cần module vào/ra?
3. Nêu các loại thiết bị ngoại vi chính.
4. Thiết bị ngoại vi thường gồm những thành phần nào?
5. Module vào/ra có những chức năng gì?
6. Phân biệt isolated I/O và memory-mapped I/O.
7. Programmed I/O có hạn chế gì?
8. Ngắt giúp cải thiện hoạt động vào/ra như thế nào?
9. DMA phù hợp trong trường hợp nào?
