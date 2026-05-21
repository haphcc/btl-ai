# Các cấu trúc điều khiển

## Nội dung chính
- Cấu trúc rẽ nhánh với `if`, `if...else`, `switch`.
- Toán tử `goto` và nhãn.
- Cấu trúc lặp với `for`, `while`, `do...while`.
- Các lệnh `break` và `continue`.
- Bài tập thực hành về rẽ nhánh và vòng lặp.

## Tổng quan
Chương này trình bày cách điều khiển luồng thực hiện của chương trình. Thay vì các lệnh luôn chạy tuần tự, chương trình có thể rẽ nhánh theo điều kiện hoặc lặp lại một nhóm lệnh nhiều lần.

## 1. Cấu trúc rẽ nhánh

### 1.1 Câu lệnh `if`

Câu lệnh `if` dùng để thực hiện một lệnh hoặc một khối lệnh khi biểu thức logic đúng. Trong C, biểu thức có giá trị `0` là sai, khác `0` là đúng.

```c
if (<bieu_thuc_logic>)
    <lenh>;
```

**Ví dụ:**

```c
if (a == 0)
    printf("a bang 0");
```

Nếu cần thực hiện nhiều lệnh, đặt trong cặp `{ }`.

```c
if (a == 0) {
    printf("a bang 0");
    a = 2912;
}
```

### 1.2 Câu lệnh `if...else`

Dạng đầy đủ của `if` cho phép chọn một trong hai nhánh.

```c
if (<bieu_thuc_logic>)
    <lenh_1>;
else
    <lenh_2>;
```

**Ví dụ:**

```c
if (a == 0)
    printf("a bang 0");
else
    printf("a khac 0");
```

### Lưu ý với `if`

- `if` có thể lồng nhau; `else` luôn ứng với `if` gần nó nhất nếu không dùng `{ }`.
- Nên dùng `else` để loại trừ các trường hợp khi các điều kiện có liên hệ với nhau.
- Không đặt dấu `;` ngay sau điều kiện của `if`, vì khi đó thân `if` trở thành lệnh rỗng.

**Ví dụ sai thường gặp:**

```c
if (a != 0);
printf("a khac 0");
```

### 1.3 Câu lệnh `switch`

`switch` dùng khi cần rẽ nhánh theo các giá trị rời rạc của một biến hoặc biểu thức.

```c
switch (<bien_hoac_bieu_thuc>) {
case <gia_tri_1>:
    <lenh_1>;
    break;
case <gia_tri_2>:
    <lenh_2>;
    break;
default:
    <lenh_mac_dinh>;
}
```

**Ví dụ:**

```c
int a;
printf("Nhap a: ");
scanf("%d", &a);

switch (a) {
case 1:
    printf("Mot");
    break;
case 2:
    printf("Hai");
    break;
case 3:
    printf("Ba");
    break;
default:
    printf("Khong biet doc");
}
```

### Lưu ý với `switch`

- Các giá trị trong mỗi `case` phải khác nhau.
- Nếu thiếu `break`, chương trình sẽ tiếp tục chạy qua các `case` phía sau cho đến khi gặp `break` hoặc hết `switch`.
- Có thể tận dụng việc bỏ `break` để gom nhiều trường hợp cùng xử lý.

```c
switch (a) {
case 1:
case 3:
    printf("So le");
    break;
case 2:
case 4:
    printf("So chan");
    break;
}
```

### 1.4 `goto` và nhãn

Nhãn được viết như tên biến và có dấu `:` ở sau. Lệnh `goto` làm chương trình nhảy đến nhãn tương ứng.

```c
goto nhan;
```

**Ví dụ:**

```c
int i;

vaosl:
printf("Nhap i: ");
scanf("%d", &i);
if (i < 10)
    goto vaosl;
```

## 2. Cấu trúc lặp

### 2.1 Vòng lặp `for`

Vòng lặp `for` thường dùng khi biết trước số lần lặp.

```c
for (<khoi_tao>; <dieu_kien>; <thay_doi>)
    <lenh>;
```

Cách thực hiện:

1. Thực hiện phần khởi tạo.
2. Kiểm tra điều kiện.
3. Nếu điều kiện sai, thoát khỏi vòng lặp.
4. Nếu điều kiện đúng, thực hiện thân vòng lặp.
5. Thực hiện phần thay đổi rồi quay lại bước kiểm tra điều kiện.

**Ví dụ:** Tính số tiền sau `n` tháng gửi tiết kiệm.

```c
#include <stdio.h>

int main() {
    float a, k;
    int thang, n;

    printf("Nhap so tien can gui: ");
    scanf("%f", &a);
    printf("Nhap lai suat: ");
    scanf("%f", &k);
    printf("Nhap so thang gui: ");
    scanf("%d", &n);

    for (thang = 1; thang <= n; thang++)
        a = a + a * k;

    printf("So tien thu duoc sau %d thang la: %0.4f", n, a);
    return 0;
}
```

**Ví dụ:** In hình chữ nhật kích thước `N x M`.

```c
for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= M; j++)
        printf("A");
    printf("\n");
}
```

### 2.2 Vòng lặp `while`

`while` dùng khi số lần lặp không biết trước và điều kiện được kiểm tra trước khi thực hiện thân vòng lặp.

```c
while (<dieu_kien>)
    <lenh>;
```

**Ví dụ:** Tính số tháng cần gửi để đạt số tiền mong muốn.

```c
#include <stdio.h>

int main() {
    float a, b, k;
    int thang;

    printf("Nhap so tien can gui: ");
    scanf("%f", &a);
    printf("Nhap so tien mong muon: ");
    scanf("%f", &b);
    printf("Nhap lai suat: ");
    scanf("%f", &k);

    thang = 0;
    while (a < b) {
        a = a + a * k;
        thang = thang + 1;
    }

    printf("So thang can gui la: %d", thang);
    return 0;
}
```

### 2.3 Vòng lặp `do...while`

`do...while` thực hiện thân vòng lặp ít nhất một lần, sau đó mới kiểm tra điều kiện.

```c
do {
    <lenh>;
} while (<dieu_kien>);
```

**Ví dụ:** Nhập số nguyên dương.

```c
int n;
do {
    printf("Hay nhap mot so > 0: ");
    scanf("%d", &n);
    printf("Ban da nhap so %d\n", n);
} while (n <= 0);
printf("Dung so duong roi!");
```

### 2.4 `break` và `continue`

`break` cho phép thoát khỏi `for`, `while`, `do...while` hoặc `switch`. Khi có nhiều vòng lặp lồng nhau, `break` thoát khỏi vòng lặp trong cùng gần nhất.

```c
for (i = 2; i <= sqrt(n); i++) {
    if (n % i == 0) {
        ng_to = 0;
        break;
    }
}
```

`continue` bỏ qua các lệnh còn lại trong thân vòng lặp hiện tại và chuyển sang vòng lặp tiếp theo. Lệnh này không áp dụng cho `switch`.

```c
for (i = 1; i <= n; i++) {
    if (i % 2 == 0)
        continue;
    printf("%d ", i);
}
```

## Bài tập thực hành

- Nhập số từ 1 đến 9 và đọc giá trị của số đó.
- Đổi chữ thường sang chữ hoa và ngược lại.
- Giải phương trình bậc nhất, bậc hai.
- Tìm số nhỏ nhất trong 4 số nguyên.
- Sắp xếp 4 số nguyên tăng dần.
- Tính tiền taxi theo số km và chính sách giảm giá.
- Kiểm tra số đối xứng, số chính phương, số nguyên tố, số lẻ.
- Tính các tổng dạng `1 + 2 + ... + n`, `1! + 2! + ... + n!`.
- In dãy Fibonacci theo công thức `F0 = F1 = 1`, `Fn = Fn-1 + Fn-2`.

## Tóm tắt

- `if` và `switch` dùng để rẽ nhánh.
- `for`, `while`, `do...while` dùng để lặp.
- `break` thoát khỏi vòng lặp hoặc `switch`; `continue` chuyển sang vòng lặp tiếp theo.
- Cần chú ý điều kiện lặp để tránh vòng lặp vô hạn.

