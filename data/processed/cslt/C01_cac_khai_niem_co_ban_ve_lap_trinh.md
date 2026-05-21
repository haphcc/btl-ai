# Các khái niệm cơ bản về lập trình

## Nội dung chính
- Khái niệm bài toán, thuật toán, chương trình và lập trình.
- Các bước xây dựng một chương trình.
- Quan hệ giữa thuật toán và chương trình.
- Ví dụ thuật toán giải phương trình, tìm UCLN, kiểm tra số nguyên tố.
- Giới thiệu ngôn ngữ C, ưu điểm, hạn chế và công cụ lập trình.

## Tổng quan
Chương này giới thiệu nền tảng của lập trình: từ bài toán cần giải, cách mô tả lời giải bằng thuật toán, đến việc cài đặt thuật toán thành chương trình bằng ngôn ngữ C.

## 1. Các khái niệm cơ bản

### Bài toán

Bài toán là vấn đề đặt ra cần được giải quyết. Trong lập trình, bài toán thường được mô tả bằng dữ liệu đầu vào, yêu cầu xử lý và kết quả đầu ra.

**Ví dụ:** Giải phương trình bậc nhất `ax + b = 0`.

- Đầu vào: hai hệ số `a`, `b`.
- Đầu ra: nghiệm `x` hoặc thông báo phương trình vô nghiệm, vô số nghiệm.

### Thuật toán

Thuật toán là một dãy hữu hạn các thao tác được sắp xếp theo trình tự xác định để từ dữ liệu đầu vào tạo ra kết quả đầu ra.

**Ví dụ:** Thuật toán giải phương trình `ax + b = 0`.

1. Nhập `a`, `b`.
2. Nếu `a == 0` và `b == 0`, kết luận phương trình vô số nghiệm.
3. Nếu `a == 0` và `b != 0`, kết luận phương trình vô nghiệm.
4. Nếu `a != 0`, tính nghiệm `x = -b / a`.

### Lập trình

Lập trình là việc cài đặt một hoặc nhiều thuật toán bằng một ngôn ngữ lập trình để tạo thành chương trình máy tính.

### Chương trình

Chương trình là tập hợp các lệnh điều khiển máy tính thực hiện một công việc nhất định. Có thể xem chương trình là cách diễn tả thuật toán bằng ngôn ngữ lập trình.

## 2. Các bước xây dựng chương trình

Quá trình xây dựng chương trình thường gồm các bước:

1. Xác định bài toán.
2. Xây dựng thuật toán.
3. Viết chương trình bằng ngôn ngữ lập trình.
4. Dịch và chạy chương trình.
5. Kiểm thử chương trình.
6. Sửa lỗi nếu có.

Khi viết chương trình, lỗi có thể xuất hiện ở nhiều dạng, trong đó lỗi cú pháp là lỗi do viết sai quy tắc của ngôn ngữ lập trình.

## 3. Thuật toán và chương trình

### Ví dụ thuật toán tìm UCLN

**Ví dụ:** Tìm ước chung lớn nhất của hai số nguyên dương `a`, `b`.

**Giải:**

1. Nhập hai số nguyên `a`, `b`.
2. Nếu `a == b`, UCLN là `a`, kết thúc.
3. Nếu `a > b`, gán `a = a - b`, quay lại bước 2.
4. Nếu `a < b`, gán `b = b - a`, quay lại bước 2.

Một đoạn chương trình minh họa:

```c
#include <stdio.h>

int main() {
    int a, b;
    printf("Nhap a, b: ");
    scanf("%d%d", &a, &b);

    while (a != b) {
        if (a > b)
            a = a - b;
        else
            b = b - a;
    }

    printf("UCLN la: %d", a);
    return 0;
}
```

### Ví dụ kiểm tra số nguyên tố

**Ví dụ:** Kiểm tra số nguyên dương `N` có phải là số nguyên tố hay không.

**Giải:**

- Nếu `N == 1`, kết luận không phải số nguyên tố.
- Nếu `N < 4`, kết luận là số nguyên tố.
- Kiểm tra các ước từ `2` đến phần nguyên của `sqrt(N)`.
- Nếu tồn tại ước chia hết cho `N`, kết luận không phải số nguyên tố.
- Nếu không có ước nào, kết luận là số nguyên tố.

## 4. Giới thiệu ngôn ngữ C

Ngôn ngữ C là ngôn ngữ lập trình mạnh, linh hoạt và được sử dụng rộng rãi. C được chuẩn hóa bởi ANSI vào năm 1983, thường gọi là ANSI C.

### Ưu điểm của C

- Có khả năng diễn đạt nhiều ý tưởng lập trình.
- Được dùng để viết hệ điều hành, chương trình điều khiển thiết bị, trình biên dịch và nhiều phần mềm ứng dụng.
- Hiệu quả thực thi cao.
- Hỗ trợ lập trình có cấu trúc thông qua hàm.
- Có khả năng tái sử dụng mã lệnh.

### Hạn chế của C

- Cú pháp có thể khó với người mới học.
- Một số ký hiệu có nhiều ý nghĩa tùy ngữ cảnh, ví dụ `*` có thể là phép nhân hoặc toán tử liên quan đến con trỏ.

### Công cụ lập trình C

Slide giới thiệu một số môi trường lập trình như Dev-C++ và các phiên bản Visual Studio.

## Bài tập thực hành

- Nêu các bước xây dựng một chương trình.
- Trình bày khái niệm bài toán, thuật toán và chương trình.
- Viết thuật toán giải phương trình bậc nhất.
- Viết thuật toán tìm UCLN của hai số.
- Viết thuật toán kiểm tra số nguyên tố.

## Tóm tắt

- Thuật toán là lời giải có trình tự cho bài toán.
- Chương trình là cách cài đặt thuật toán bằng ngôn ngữ lập trình.
- Ngôn ngữ C mạnh, linh hoạt, nhưng yêu cầu người học nắm chắc cú pháp và cách tổ chức chương trình.

