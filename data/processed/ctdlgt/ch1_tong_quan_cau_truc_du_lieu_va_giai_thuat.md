# Chương 1: Tổng quan cấu trúc dữ liệu và giải thuật

## Nội dung chính
- Khái niệm cấu trúc dữ liệu và vai trò của cấu trúc dữ liệu.
- Các kiểu cấu trúc dữ liệu cơ bản.
- Khái niệm thuật toán và các tiêu chuẩn của thuật toán.
- Các cách biểu diễn thuật toán: ngôn ngữ tự nhiên, lưu đồ, mã giả, ngôn ngữ lập trình.
- Ví dụ thuật toán tính tổng và tìm phần tử lớn nhất trong mảng.

## Tổng quan
Chương này giới thiệu nền tảng của môn Cấu trúc dữ liệu và giải thuật. Cấu trúc dữ liệu quyết định cách tổ chức lưu trữ dữ liệu, còn thuật toán quyết định cách xử lý dữ liệu đó để giải quyết bài toán hiệu quả.

## 1.1. Cấu trúc dữ liệu

### Khái niệm
Cấu trúc dữ liệu là cách kết hợp nhiều thành phần dữ liệu khác nhau thành một thực thể thống nhất để biểu diễn một kiểu dữ liệu.

Nói cách khác, cấu trúc dữ liệu mô tả cách tổ chức lưu trữ dữ liệu trong máy tính sao cho phù hợp với bài toán và thao tác xử lý.

### Tiêu chuẩn của cấu trúc dữ liệu
Một cấu trúc dữ liệu tốt cần:

- Biểu diễn đầy đủ thông tin.
- Phù hợp với các thao tác cần thực hiện.
- Phù hợp với điều kiện cho phép của ngôn ngữ lập trình.
- Tiết kiệm tài nguyên hệ thống.

### Vai trò
Cấu trúc dữ liệu đóng vai trò quan trọng trong việc kết hợp dữ liệu và đưa ra cách giải quyết bài toán. Cấu trúc dữ liệu phù hợp giúp các thuật toán thao tác trên đối tượng hiệu quả hơn.

## Các kiểu cấu trúc dữ liệu cơ bản

| Cấu trúc | Ý nghĩa |
|---|---|
| Bản ghi (`struct`) | Gom nhiều trường dữ liệu liên quan |
| Danh sách/mảng (`array`) | Lưu các phần tử cùng kiểu theo chỉ số |
| Danh sách liên kết (`list`) | Lưu các phần tử rời rạc, liên kết bằng con trỏ |
| Cây (`tree`) | Biểu diễn quan hệ phân cấp |
| Bảng băm (`hash table`) | Truy xuất dữ liệu qua hàm băm |

## 1.2. Thuật toán

### Khái niệm
Thuật toán là một dãy hữu hạn các chỉ thị có thể thi hành để đạt được một mục tiêu đặt ra.

**Ví dụ:** Thuật toán tính tổng các số nguyên dương nhỏ hơn `n`.

```text
Bước 1: S = 0, i = 1
Bước 2: Nếu i < n thì S = S + i
        Ngược lại chuyển sang bước 4
Bước 3: i = i + 1
        Quay lại bước 2
Bước 4: Tổng cần tìm là S
```

### Tiêu chuẩn của thuật toán
Một thuật toán cần thỏa mãn:

- Xác định rõ dữ liệu đầu vào.
- Xác định rõ kết quả đầu ra.
- Tính xác định: cùng dữ liệu đầu vào cho cùng kết quả đầu ra.
- Tính khả thi: các bước đơn giản, thực hiện được trong thời gian hữu hạn.
- Tính dừng: sau hữu hạn bước phải kết thúc.

### Sự cần thiết của thuật toán
Dùng máy tính xử lý dữ liệu giúp:

- Xử lý nhanh hơn.
- Xử lý nhiều hơn.
- Giải quyết các bài toán con người khó hoặc không thể hoàn thành thủ công.

Để đạt hiệu quả, không chỉ tăng cấu hình máy tính mà cần thuật toán hiệu quả. Slide nhấn mạnh rằng máy tính mạnh vẫn không cứu được một thuật toán tồi.

## Biểu diễn thuật toán

Các cách biểu diễn thuật toán:

- Ngôn ngữ tự nhiên.
- Lưu đồ hoặc sơ đồ khối.
- Mã giả.
- Ngôn ngữ lập trình.

### Biểu diễn bằng ngôn ngữ tự nhiên
Ngôn ngữ tự nhiên liệt kê tuần tự các bước của thuật toán.

Ưu điểm:

- Đơn giản.
- Không cần biết quy ước mã giả hoặc lưu đồ.

Nhược điểm:

- Dài dòng.
- Thiếu cấu trúc.
- Có thể khó hiểu và không diễn đạt chính xác thuật toán.

### Biểu diễn bằng lưu đồ
Lưu đồ là hệ thống các nút và cung có hình dạng khác nhau để thể hiện các chức năng khác nhau.

Một số thành phần thường gặp:

| Thành phần | Ý nghĩa |
|---|---|
| Begin/End | Bắt đầu hoặc kết thúc |
| Khối xử lý | Thực hiện một thao tác |
| Khối vào/ra | Nhập hoặc xuất dữ liệu |
| Khối điều kiện | Rẽ nhánh đúng/sai |
| Gọi hàm | Gọi một thuật toán hoặc chương trình con |

### Biểu diễn bằng mã giả
Mã giả dùng ngôn ngữ tựa ngôn ngữ lập trình, có cấu trúc chuẩn hóa, có thể gần với Pascal hoặc C.

Ưu điểm:

- Gọn hơn lưu đồ khối.
- Dễ chuyển sang chương trình.

Nhược điểm:

- Không trực quan bằng lưu đồ.

Một số cấu trúc mã giả:

```text
if ... then ... else ...
while ... do ...
do ... while (...)
for ... do ...
return [giá trị]
Tên(tham số)
```

Quy ước khai báo thuật toán:

```text
Thuật toán <tên thuật toán>(<tham số>)
Input: <dữ liệu vào>
Output: <dữ liệu ra>
<Các câu lệnh>
End
```

## Ví dụ: tìm phần tử lớn nhất trong mảng

**Ví dụ:** Tìm phần tử lớn nhất trong mảng một chiều.

```text
amax = a0
i = 1
while (i < n)
    if (amax < ai) amax = ai
    i = i + 1
```

**Giải thích:** Thuật toán giả sử phần tử đầu tiên là lớn nhất, sau đó lần lượt so sánh với các phần tử còn lại để cập nhật giá trị lớn nhất.

## Tóm tắt chương
- Cấu trúc dữ liệu là cách tổ chức lưu trữ dữ liệu.
- Thuật toán là dãy hữu hạn các bước xử lý để đạt mục tiêu.
- Cấu trúc dữ liệu và thuật toán phải phù hợp với nhau để bài toán được giải quyết hiệu quả.
- Thuật toán có thể biểu diễn bằng ngôn ngữ tự nhiên, lưu đồ, mã giả hoặc ngôn ngữ lập trình.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Cấu trúc dữ liệu | Cách tổ chức và lưu trữ dữ liệu |
| Thuật toán | Dãy hữu hạn các bước xử lý |
| Mã giả | Cách mô tả thuật toán gần với ngôn ngữ lập trình |
| Lưu đồ | Sơ đồ khối biểu diễn luồng xử lý |
| Input | Dữ liệu đầu vào |
| Output | Kết quả đầu ra |
| Tính dừng | Thuật toán kết thúc sau hữu hạn bước |

## Câu hỏi ôn tập
1. Cấu trúc dữ liệu là gì?
2. Một cấu trúc dữ liệu tốt cần thỏa mãn những tiêu chuẩn nào?
3. Thuật toán là gì?
4. Trình bày các tiêu chuẩn của thuật toán.
5. Có những cách nào để biểu diễn thuật toán?
6. Ưu điểm và nhược điểm của mã giả là gì?
7. Hãy mô tả thuật toán tìm phần tử lớn nhất trong mảng.
