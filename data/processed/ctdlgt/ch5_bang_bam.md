# Chương 5: Bảng băm

## Nội dung chính
- Khái niệm bảng băm và hàm băm.
- Xung đột trong bảng băm.
- Bảng băm mở và cách xử lý xung đột bằng danh sách liên kết.
- Một số hàm băm thông dụng.
- Bảng băm đóng.
- Các phương pháp băm lại: tuyến tính, bình phương, tạo vùng mới.

## Tổng quan
Bảng băm là cấu trúc dữ liệu dùng hàm băm để ánh xạ khóa dữ liệu thành chỉ số trong bảng. Mục tiêu của bảng băm là truy cập dữ liệu nhanh, nhưng cần xử lý trường hợp nhiều khóa khác nhau cho cùng một giá trị băm.

## 1. Bảng băm mở

### Bảng băm
Bảng băm (Hash Table) là mảng `B` gồm `m` phần tử, dùng để lưu trữ hoặc định vị phần tử dữ liệu có khóa phân biệt thuộc tập chỉ số `{0, 1, 2, ..., m - 1}`.

### Hàm băm
Hàm băm (Hash function) `H(x)` cho giá trị là một chỉ số phần tử của bảng `B`.

```text
H(x) -> chỉ số trong bảng B
```

### Xung đột
Xung đột (collision) xảy ra khi hai khóa khác nhau nhưng có cùng giá trị hàm băm:

```text
x1 != x2 nhưng H(x1) = H(x2)
```

### Xử lý xung đột trong bảng băm mở
Slide nêu cách giải quyết: liên kết các phần tử có khóa khác nhau nhưng cùng giá trị hàm băm thành một danh sách. Ô tương ứng trong bảng băm `B` sẽ trỏ tới danh sách đầu tiên.

Nói cách khác, mỗi vị trí trong bảng băm có thể là đầu của một danh sách liên kết chứa các phần tử cùng giá trị băm.

## Một số hàm băm thông dụng

### Hàm cắt bỏ
Hàm cắt bỏ loại bớt một phần nào đó của khóa.

**Ví dụ:** Với `x = 842615`, bỏ các chữ số hàng lẻ như vị trí 1, 3, 5 thì số còn lại là `821`; khi đó `H(842615) = 821`.

Nhận xét: hàm này khó bảo đảm phân bố đều.

### Hàm gấp
Hàm gấp chia số nguyên thành một số đoạn tùy chọn, sau đó kết hợp các đoạn.

**Ví dụ:** Với khóa `842615`, lấy số các hàng lẻ là `465`, số các hàng chẵn là `821`, khi đó:

```text
H(x) = 465 + 821 = 1286
```

Nhận xét: khả năng phân bố có thể tốt hơn hàm cắt bỏ.

### Hàm phần dư
Hàm phần dư lấy phần dư của phép chia `x / m`.

```text
H(x) = x mod m
```

Nên chọn `m` là số nguyên tố. Cách lấy phần dư có khả năng tránh xung đột tốt hơn.

## 2. Bảng băm đóng

Bảng băm mở chỉ lưu các liên kết trỏ đến thành phần dữ liệu có khóa tương ứng.

Bảng băm đóng là bảng băm mà mỗi thành phần của nó lưu trữ trực tiếp chính các thành phần dữ liệu.

## Các phương pháp xử lý xung đột trong bảng băm đóng

### Băm lại tuyến tính
Công thức:

```text
Hi(x) = (H(x) + i) mod m
```

Nhận xét: các giá trị hàm băm có thể xếp thành từng đoạn con, nên việc tìm kiếm vị trí rỗng có thể chậm.

### Băm lại bình phương
Công thức:

```text
Hi(x) = (H(x) + i^2) mod m
```

### Băm lại bằng cách tạo vùng mới
Ngoài bảng `B`, tạo thêm một vùng không gian mới để xử lý các phần tử khi xảy ra xung đột.

## Tóm tắt chương
- Bảng băm dùng hàm băm để ánh xạ khóa thành chỉ số.
- Xung đột xảy ra khi hai khóa khác nhau có cùng giá trị băm.
- Bảng băm mở xử lý xung đột bằng danh sách liên kết.
- Bảng băm đóng lưu trực tiếp phần tử dữ liệu trong bảng.
- Các cách băm lại gồm tuyến tính, bình phương và tạo vùng mới.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Bảng băm | Cấu trúc ánh xạ khóa vào vị trí trong bảng |
| Hàm băm | Hàm tính chỉ số từ khóa |
| Xung đột | Hai khóa khác nhau có cùng giá trị băm |
| Bảng băm mở | Bảng dùng liên kết đến danh sách phần tử cùng giá trị băm |
| Bảng băm đóng | Bảng lưu trực tiếp dữ liệu trong từng ô |
| Băm lại tuyến tính | Dò vị trí theo `(H(x) + i) mod m` |
| Băm lại bình phương | Dò vị trí theo `(H(x) + i^2) mod m` |

## Câu hỏi ôn tập
1. Bảng băm là gì?
2. Hàm băm có vai trò gì?
3. Xung đột xảy ra khi nào?
4. Bảng băm mở xử lý xung đột như thế nào?
5. Trình bày hàm cắt bỏ, hàm gấp và hàm phần dư.
6. Bảng băm đóng khác bảng băm mở như thế nào?
7. Băm lại tuyến tính có công thức gì?
8. Vì sao nên chọn `m` là số nguyên tố trong hàm phần dư?
