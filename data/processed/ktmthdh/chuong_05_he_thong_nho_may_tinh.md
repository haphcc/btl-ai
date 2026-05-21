# Chương 5: Hệ thống nhớ máy tính

## Nội dung chính
- Tổng quan và đặc trưng của hệ thống nhớ.
- Phân cấp hệ thống nhớ.
- Bộ nhớ bán dẫn: ROM, RAM, SRAM, DRAM và Flash.
- Tổ chức chip nhớ và các tín hiệu điều khiển.
- Thiết kế module nhớ, cache và bộ nhớ ngoài.

## Tổng quan
Hệ thống nhớ lưu chương trình và dữ liệu cho máy tính. Chương này trình bày các đặc trưng của bộ nhớ, nguyên lý phân cấp, các loại bộ nhớ bán dẫn, tổ chức chip nhớ và vai trò của cache, bộ nhớ chính, bộ nhớ ngoài.

## Đặc trưng của hệ thống nhớ

### Các tiêu chí đánh giá

**Khái niệm chính:**
- Vị trí: trong CPU, bộ nhớ trong hoặc bộ nhớ ngoài.
- Dung lượng: số bit hoặc byte có thể lưu trữ.
- Đơn vị truyền: lượng dữ liệu trao đổi mỗi lần.
- Phương pháp truy nhập: tuần tự, trực tiếp, ngẫu nhiên hoặc liên kết.
- Kiểu vật lý: bán dẫn, từ tính, quang.
- Đặc trưng vật lý: khả biến, không khả biến, tốc độ, độ tin cậy.

**Giải thích:**
Không có loại bộ nhớ nào tối ưu đồng thời về dung lượng, tốc độ và giá thành. Vì vậy hệ thống nhớ được tổ chức thành nhiều mức.

## Phân cấp hệ thống nhớ

### Các mức nhớ

**Sơ đồ / Cấu trúc / Quy trình:**
- Tập thanh ghi.
- Cache L1.
- Cache L2.
- Bộ nhớ chính.
- Bộ nhớ ngoài.

**Quy luật phân cấp:**
- Dung lượng tăng dần khi đi từ trên xuống.
- Tốc độ trao đổi dữ liệu giảm dần.
- Giá thành trên 1 bit giảm dần.
- Tần suất CPU truy nhập giảm dần.

**Giải thích:**
CPU cần dữ liệu rất nhanh, nhưng bộ nhớ nhanh thường đắt và dung lượng nhỏ. Phân cấp bộ nhớ tận dụng tính cục bộ của chương trình để đạt hiệu năng tốt với chi phí hợp lý.

## Bộ nhớ bán dẫn

### Phân loại

**Khái niệm chính:**
- ROM: bộ nhớ chỉ đọc, thường lưu chương trình cố định.
- PROM: ROM có thể lập trình một lần.
- EPROM: ROM có thể xóa bằng tia cực tím và lập trình lại.
- EEPROM: ROM có thể xóa/lập trình bằng điện.
- Flash memory: bộ nhớ không mất dữ liệu, có thể xóa/ghi theo khối.
- RAM: bộ nhớ đọc/ghi, thường mất dữ liệu khi mất điện.

**Quy trình / Mô hình / Ký hiệu:**
| Loại nhớ | Đặc điểm |
|---|---|
| ROM | Không mất dữ liệu, chủ yếu đọc. |
| PROM | Lập trình một lần. |
| EPROM | Có thể xóa và ghi lại bằng quy trình đặc biệt. |
| EEPROM | Có thể xóa/ghi bằng điện. |
| Flash | Không mất dữ liệu, dùng rộng rãi trong lưu trữ. |
| RAM | Đọc/ghi nhanh, thường mất dữ liệu khi tắt nguồn. |

## SRAM và DRAM

### So sánh SRAM và DRAM

**Khái niệm chính:**
- SRAM lưu bit bằng mạch chốt, nhanh nhưng đắt và dung lượng thấp hơn.
- DRAM lưu bit bằng tụ điện, cần làm tươi, chậm hơn nhưng dung lượng lớn và rẻ hơn.

**Quy trình / Mô hình / Ký hiệu:**
| Tiêu chí | SRAM | DRAM |
|---|---|---|
| Cách lưu bit | Mạch chốt | Tụ điện |
| Tốc độ | Nhanh hơn | Chậm hơn |
| Dung lượng | Thấp hơn | Lớn hơn |
| Giá thành | Cao hơn | Thấp hơn |
| Ứng dụng | Cache | Bộ nhớ chính |

## Tổ chức chip nhớ

### Ô nhớ và chip nhớ

**Khái niệm chính:**
- Chip nhớ có các đường địa chỉ, đường dữ liệu và tín hiệu điều khiển.
- Nếu có `n` đường địa chỉ thì có thể chọn $2^n$ ngăn nhớ.
- Nếu mỗi ngăn nhớ có `m` bit, dung lượng chip là $2^n \times m$ bit.

**Sơ đồ / Cấu trúc / Quy trình:**
- Đường địa chỉ: `A0 ... An-1`.
- Đường dữ liệu: `D0 ... Dm-1`.
- `CS/CE`: chọn chip.
- `RD/OE`: đọc hoặc cho phép xuất dữ liệu.
- `WR/WE`: ghi hoặc cho phép ghi.

### Tổ chức DRAM

**Khái niệm chính:**
- DRAM thường dùng địa chỉ dồn kênh.
- `RAS` chọn địa chỉ hàng.
- `CAS` chọn địa chỉ cột.

**Giải thích:**
Địa chỉ dồn kênh giúp giảm số chân địa chỉ trên chip DRAM nhưng cần quá trình chọn hàng và cột.

## Thiết kế module nhớ bán dẫn

### Các kiểu mở rộng

**Quy trình / Mô hình / Ký hiệu:**
- Tăng độ dài ngăn nhớ: ghép chip để tăng số bit dữ liệu mỗi từ nhớ.
- Tăng số lượng ngăn nhớ: ghép chip để tăng số địa chỉ.
- Tăng cả số lượng và độ dài: kết hợp cả hai cách trên.

**Ví dụ / Minh họa:**
- Module 8K x 8 bit có 8K ngăn nhớ, mỗi ngăn 8 bit.
- Nếu dùng chip 8K x 4 bit, cần ghép song song 2 chip để tạo module 8K x 8 bit.
- Nếu cần tăng từ 8K lên 16K ngăn, cần ghép theo chiều địa chỉ và dùng tín hiệu chọn chip.

## Bộ nhớ cache và bộ nhớ ngoài

### Cache

**Khái niệm chính:**
- Cache là bộ nhớ nhanh nằm giữa CPU và bộ nhớ chính.
- Cache lưu các khối dữ liệu/lệnh được truy cập thường xuyên.
- Các vấn đề chính gồm ánh xạ cache và thuật toán thay thế.

### Bộ nhớ ngoài

**Khái niệm chính:**
- Bộ nhớ ngoài có dung lượng lớn hơn bộ nhớ chính.
- Tốc độ thấp hơn nhưng dùng để lưu trữ lâu dài.
- Có thể gồm ổ đĩa từ, đĩa quang, flash và hệ thống RAID.

## Tóm tắt chương
- Hệ thống nhớ được đánh giá theo vị trí, dung lượng, đơn vị truyền, phương pháp truy nhập và đặc trưng vật lý.
- Phân cấp bộ nhớ cân bằng giữa tốc độ, dung lượng và giá thành.
- ROM không mất dữ liệu; RAM đọc/ghi nhanh nhưng thường mất dữ liệu khi mất điện.
- SRAM nhanh, dùng cho cache; DRAM dung lượng lớn, dùng cho bộ nhớ chính.
- Chip nhớ được tổ chức bằng đường địa chỉ, dữ liệu và tín hiệu điều khiển.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Memory hierarchy | Phân cấp hệ thống nhớ. |
| Register | Thanh ghi, mức nhớ nhanh nhất trong CPU. |
| Cache | Bộ nhớ nhanh giữa CPU và bộ nhớ chính. |
| ROM | Bộ nhớ chỉ đọc, không mất dữ liệu. |
| RAM | Bộ nhớ đọc/ghi, thường mất dữ liệu khi tắt nguồn. |
| SRAM | RAM tĩnh, nhanh, thường dùng làm cache. |
| DRAM | RAM động, dung lượng lớn, thường dùng làm bộ nhớ chính. |
| RAS/CAS | Tín hiệu chọn hàng/cột trong DRAM. |

## Câu hỏi ôn tập
1. Nêu các đặc trưng chính của hệ thống nhớ.
2. Phân cấp hệ thống nhớ gồm những mức nào?
3. Vì sao cần tổ chức hệ thống nhớ theo phân cấp?
4. Phân biệt ROM, PROM, EPROM, EEPROM và Flash.
5. So sánh SRAM và DRAM.
6. Nếu chip nhớ có 13 đường địa chỉ và mỗi ngăn 8 bit, dung lượng chip là bao nhiêu?
7. Các tín hiệu `CS`, `RD/OE`, `WR/WE` có chức năng gì?
8. Cache có vai trò gì trong hệ thống nhớ?
