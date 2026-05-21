# Chương 2.1: Danh sách

## Nội dung chính
- Khái niệm danh sách, danh sách con, phần đầu, phần cuối và dãy con.
- Các phép toán cơ bản trên danh sách.
- Biểu diễn danh sách bằng mảng một chiều.
- Thao tác chèn và xóa trên danh sách cài đặt bằng mảng.
- Biểu diễn danh sách bằng danh sách móc nối và địa chỉ gián tiếp.
- Nhận xét ưu, nhược điểm của từng cách biểu diễn.

## Tổng quan
Danh sách là cấu trúc dữ liệu tuyến tính gồm các phần tử cùng kiểu được sắp theo thứ tự trước sau. Chương này tập trung vào cách biểu diễn danh sách trong bộ nhớ, đặc biệt là biểu diễn bằng mảng và các thao tác chèn, xóa.

## 1. Khái niệm danh sách

Danh sách là một tập sắp thứ tự các phần tử cùng kiểu. Các phần tử được sắp theo quan hệ trước - sau.

### Danh sách con, phần đầu, phần cuối
Danh sách con gồm các phần tử liên tiếp từ `ai` đến `aj` của danh sách.

- Nếu `i = 1`, danh sách con được gọi là phần đầu (prefix).
- Nếu `j = n`, danh sách con được gọi là phần cuối (postfix).

### Dãy con
Dãy con là danh sách tạo thành bằng cách loại khỏi danh sách ban đầu một số phần tử.

**Ví dụ:** Với `DS = (a, b, c, d, e, f)`:

- `(c, d, e)` là một danh sách con.
- `(a, b)` là phần đầu.
- `(c, d, e, f)` là phần cuối.
- `(a, c, f)` là một dãy con.

## Các phép toán trên danh sách

Các phép toán thường gặp:

- Khởi tạo danh sách rỗng.
- Xác định độ dài.
- Xóa phần tử.
- Chèn phần tử.
- Tìm kiếm.
- Kiểm tra trạng thái rỗng.
- Kiểm tra trạng thái tràn.
- Duyệt danh sách.
- Sắp xếp.

## 2. Biểu diễn danh sách trong máy tính

### 2.1. Cài đặt bằng mảng một chiều
Cài đặt bằng mảng lưu các phần tử của danh sách trong một vector gồm các ô nhớ liên tiếp.

**Ví dụ:** Danh sách `DS = (A, B, C, D, E, F, G, H, I, J, K)` được lưu trong mảng `M` gồm 11 phần tử liên tiếp.

Ưu điểm:

- Truy cập trực tiếp đến mọi phần tử theo chỉ số.
- Cài đặt đơn giản.

Nhược điểm:

- Kích thước mảng cố định.
- Chèn và xóa thường phải dịch chuyển nhiều phần tử.

### Chèn phần tử trong mảng
Để chèn giá trị `V` vào vị trí `P`:

1. Dồn các phần tử từ vị trí `P` đến cuối sang phải một vị trí.
2. Đặt `V` vào vị trí `P`.
3. Tăng `n` lên 1.

```text
for i = n - 1 downto P
    a[i + 1] = a[i]
a[P] = V
n = n + 1
```

### Xóa phần tử trong mảng
Để xóa phần tử ở vị trí `P`:

1. Chuyển các phần tử từ vị trí `P + 1` đến cuối sang trái một vị trí.
2. Giảm `n` đi 1.

```text
for i = P to n - 2
    a[i] = a[i + 1]
n = n - 1
```

Nếu không cần bảo toàn thứ tự các phần tử sau khi xóa, có thể đổi phần tử cần xóa với phần tử cuối rồi giảm `n` đi 1.

### 2.2. Cài đặt bằng danh sách móc nối
Trong danh sách móc nối, các phần tử được lưu ở các ô nhớ bất kỳ trong bộ nhớ. Các phần tử liên kết với nhau bằng con trỏ.

Cách biểu diễn này được trình bày chi tiết ở chương danh sách liên kết.

### 2.3. Dùng địa chỉ gián tiếp
Các phần tử được lưu ở các ô nhớ bất kỳ. Ngoài ra có một mảng địa chỉ, trong đó phần tử thứ `i` của mảng chứa địa chỉ của phần tử thứ `i` trong danh sách.

## Nhận xét

| Cách biểu diễn | Ưu điểm | Hạn chế |
|---|---|---|
| Mảng một chiều | Truy cập trực tiếp nhanh | Kích thước cố định, chèn/xóa phải dịch chuyển |
| Danh sách móc nối | Linh hoạt về vị trí lưu trữ | Không truy cập trực tiếp theo chỉ số |
| Địa chỉ gián tiếp | Phần tử có thể nằm rời rạc trong bộ nhớ | Cần thêm mảng địa chỉ |

## Tóm tắt chương
- Danh sách là tập các phần tử cùng kiểu có thứ tự.
- Danh sách có thể biểu diễn bằng mảng, danh sách liên kết hoặc địa chỉ gián tiếp.
- Mảng cho phép truy cập trực tiếp nhưng khó chèn/xóa và có kích thước cố định.
- Danh sách liên kết khắc phục hạn chế về vị trí lưu trữ nhưng cần con trỏ.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Danh sách | Tập phần tử cùng kiểu có thứ tự |
| Danh sách con | Các phần tử liên tiếp trong danh sách |
| Prefix | Phần đầu của danh sách |
| Postfix | Phần cuối của danh sách |
| Dãy con | Danh sách tạo bằng cách bỏ bớt một số phần tử |
| Mảng | Cấu trúc lưu các phần tử liên tiếp trong bộ nhớ |
| Danh sách móc nối | Danh sách có phần tử liên kết bằng con trỏ |

## Câu hỏi ôn tập
1. Danh sách là gì?
2. Phân biệt danh sách con và dãy con.
3. Các phép toán cơ bản trên danh sách gồm những gì?
4. Cài đặt danh sách bằng mảng có ưu điểm gì?
5. Vì sao thao tác chèn/xóa trên mảng có thể tốn chi phí?
6. Khi nào có thể xóa phần tử bằng cách đổi với phần tử cuối?
7. Địa chỉ gián tiếp dùng để biểu diễn danh sách như thế nào?
