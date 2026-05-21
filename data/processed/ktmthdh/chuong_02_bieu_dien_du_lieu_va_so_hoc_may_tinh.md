# Chương 2: Biểu diễn dữ liệu và số học máy tính

## Nội dung chính
- Các hệ đếm cơ bản: thập phân, nhị phân và thập lục phân.
- Chuyển đổi giữa các hệ đếm.
- Mã hóa và lưu trữ dữ liệu trong máy tính.
- Biểu diễn số nguyên không dấu và có dấu.
- Số học máy tính, biểu diễn số thực và biểu diễn ký tự.

## Tổng quan
Chương này trình bày cách máy tính biểu diễn dữ liệu bằng các bit nhị phân. Người học cần hiểu các hệ đếm, cách chuyển đổi, cách lưu dữ liệu trong bộ nhớ và cách biểu diễn số nguyên, số thực, ký tự để hiểu hoạt động số học của máy tính.

## Các hệ đếm cơ bản

### Hệ thập phân

**Khái niệm chính:**
- Hệ thập phân (`decimal`) dùng 10 chữ số từ 0 đến 9.
- Một số có $n$ chữ số có thể biểu diễn các giá trị khác nhau theo trọng số lũy thừa của 10.

**Giải thích:**
Đây là hệ đếm quen thuộc với con người. Giá trị của mỗi chữ số phụ thuộc vào vị trí của nó trong số.

### Hệ nhị phân

**Khái niệm chính:**
- Hệ nhị phân (`binary`) dùng hai chữ số 0 và 1.
- Máy tính dùng nhị phân vì phần cứng số dễ biểu diễn hai trạng thái.

**Ví dụ / Minh họa:**
- Với $n$ bit, có thể biểu diễn $2^n$ giá trị khác nhau.
- Với 8 bit, dải số nguyên không dấu là từ 0 đến $2^8 - 1 = 255$.
- Với 16 bit, dải là từ 0 đến $2^{16} - 1 = 65535$.

### Hệ thập lục phân

**Khái niệm chính:**
- Hệ thập lục phân (`hexadecimal`) dùng 16 ký hiệu: 0-9 và A-F.
- Mỗi chữ số hexadecimal tương ứng với 4 bit.

**Giải thích:**
Hexadecimal được dùng để viết gọn chuỗi bit dài. Ví dụ một byte 8 bit có thể viết bằng 2 chữ số hex.

## Chuyển đổi hệ đếm

### Thập phân sang nhị phân

**Quy trình / Mô hình / Ký hiệu:**
- Phần nguyên: chia liên tiếp cho 2, lấy các số dư theo thứ tự ngược lại.
- Phần thập phân: nhân liên tiếp với 2, lấy phần nguyên theo thứ tự thực hiện.

**Ví dụ / Minh họa:**
- Số $13_{10}$ đổi sang nhị phân:
  - $13 / 2 = 6$ dư 1
  - $6 / 2 = 3$ dư 0
  - $3 / 2 = 1$ dư 1
  - $1 / 2 = 0$ dư 1
  - Kết quả: $13_{10} = 1101_2$.

### Nhị phân và thập lục phân

**Quy trình / Mô hình / Ký hiệu:**
- Nhóm chuỗi bit thành từng nhóm 4 bit từ phải sang trái.
- Đổi từng nhóm 4 bit thành một chữ số hex.

**Ví dụ / Minh họa:**
- $1011\ 0101_2 = B5_{16}$.

## Mã hóa và lưu trữ dữ liệu

### Nguyên tắc mã hóa

**Khái niệm chính:**
- Mọi dữ liệu đưa vào máy tính phải được mã hóa thành số nhị phân.
- Dữ liệu có thể là dữ liệu nhân tạo hoặc dữ liệu tự nhiên.
- Dữ liệu tự nhiên cần quá trình biến đổi qua thiết bị đo, ADC hoặc DAC nếu trao đổi với môi trường tương tự.

**Giải thích:**
Máy tính chỉ xử lý được bit. Văn bản, âm thanh, hình ảnh và số liệu đều phải được mã hóa thành dãy bit trước khi lưu trữ hoặc xử lý.

### Little-endian và Big-endian

**Khái niệm chính:**
- `Big-endian`: byte có trọng số lớn được lưu ở địa chỉ thấp.
- `Little-endian`: byte có trọng số nhỏ được lưu ở địa chỉ thấp.

**Ví dụ / Minh họa:**
Với dữ liệu 32 bit gồm các byte `12 34 56 78`:

| Kiểu lưu | Địa chỉ thấp đến cao |
|---|---|
| Big-endian | `12 34 56 78` |
| Little-endian | `78 56 34 12` |

## Biểu diễn số nguyên

### Số nguyên không dấu

**Khái niệm chính:**
- Số nguyên không dấu dùng toàn bộ bit để biểu diễn độ lớn.
- Với $n$ bit, dải biểu diễn là:

$$
0 \le x \le 2^n - 1
$$

**Ví dụ / Minh họa:**
- 8 bit: 0 đến 255.
- 16 bit: 0 đến 65535.

### Số nguyên có dấu

**Khái niệm chính:**
- Cần dành thông tin để biểu diễn dấu âm/dương.
- Các cách biểu diễn thường gặp: dấu - độ lớn (`sign-magnitude`) và bù 2 (`two's complement`).

**Quy trình / Mô hình / Ký hiệu:**
| Cách biểu diễn | Ý nghĩa |
|---|---|
| Sign-magnitude | Bit cao nhất biểu diễn dấu, các bit còn lại biểu diễn độ lớn. |
| Two's complement | Số âm được biểu diễn bằng mã bù 2, thuận tiện cho phép cộng/trừ. |

**Lưu ý:**
- Trong bù 2 với $n$ bit, dải giá trị thường là từ $-2^{n-1}$ đến $2^{n-1}-1$.

## Số học máy tính

### Phép toán số nguyên

**Khái niệm chính:**
- Các phép cộng, trừ, nhân, chia được thực hiện trên biểu diễn nhị phân.
- Cần chú ý tràn số khi kết quả vượt quá dải biểu diễn.

**Giải thích:**
Với số nguyên không dấu, tràn xảy ra khi kết quả lớn hơn $2^n - 1$. Với số nguyên có dấu bù 2, tràn xảy ra khi kết quả vượt khỏi dải biểu diễn có dấu.

### Số thực và ký tự

**Khái niệm chính:**
- Số thực cần biểu diễn phần dấu, phần mũ và phần trị nếu dùng dạng dấu phẩy động.
- Ký tự được biểu diễn bằng mã ký tự.

**Lưu ý:**
- Khi tính toán số thực, kết quả có thể có sai số do giới hạn số bit biểu diễn.

## Tóm tắt chương
- Máy tính biểu diễn dữ liệu bằng nhị phân.
- Hệ thập lục phân giúp viết gọn chuỗi bit.
- Dữ liệu nhiều byte có thể lưu theo big-endian hoặc little-endian.
- Số nguyên không dấu dùng toàn bộ bit cho độ lớn; số nguyên có dấu thường dùng bù 2.
- Cần chú ý dải biểu diễn và tràn số khi thực hiện số học máy tính.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Binary | Hệ nhị phân, dùng hai ký hiệu 0 và 1. |
| Hexadecimal | Hệ thập lục phân, dùng 16 ký hiệu 0-9 và A-F. |
| Bit | Đơn vị thông tin nhị phân. |
| Byte | Nhóm 8 bit. |
| Big-endian | Cách lưu byte trọng số lớn ở địa chỉ thấp. |
| Little-endian | Cách lưu byte trọng số nhỏ ở địa chỉ thấp. |
| Sign-magnitude | Biểu diễn số có dấu bằng bit dấu và phần độ lớn. |
| Two's complement | Biểu diễn số âm bằng mã bù 2. |

## Câu hỏi ôn tập
1. Vì sao máy tính dùng hệ nhị phân?
2. Chuyển $25_{10}$ sang hệ nhị phân.
3. Vì sao hệ thập lục phân thường được dùng khi mô tả dữ liệu máy tính?
4. Phân biệt big-endian và little-endian.
5. Với 8 bit, số nguyên không dấu biểu diễn được dải giá trị nào?
6. Mã bù 2 có ưu điểm gì trong phép cộng/trừ?
7. Tràn số là gì?
8. Vì sao biểu diễn số thực có thể gây sai số?
