# Chương trình con

## Nội dung chính
- Khái niệm chương trình con và hàm trong C.
- Cách xây dựng hàm và lời gọi hàm.
- Tham số hình thức, tham số thực sự và lệnh `return`.
- Tầm tác dụng của biến.
- Truyền tham số cho hàm.
- Hàm đệ quy và một số hàm thông dụng.

## Tổng quan
Chương trình con giúp chia chương trình lớn thành các phần nhỏ, dễ viết, dễ kiểm tra và có thể tái sử dụng. Trong C, chương trình con được thể hiện dưới dạng hàm.

## 1. Khái niệm

Chương trình con là một đoạn chương trình có tên, có thể có đầu vào và đầu ra, dùng để giải quyết một công việc chuyên biệt trong chương trình chính.

Chương trình con được dùng khi cần:

- Tái sử dụng một đoạn xử lý ở nhiều nơi.
- Chia chương trình lớn thành các phần nhỏ.
- Làm chương trình rõ ràng, dễ hiểu, dễ phát hiện lỗi và cải tiến.

Trong C chỉ tồn tại chương trình con dưới dạng hàm. Hàm có thể trả về giá trị hoặc không trả về giá trị nếu khai báo kiểu `void`.

## 2. Cách xây dựng hàm

Cú pháp tổng quát:

```c
<kieu_tra_ve> <ten_ham>(<danh_sach_tham_so>) {
    <cac_cau_lenh>
    return <gia_tri>;
}
```

Trong đó:

- `<kieu_tra_ve>` là kiểu dữ liệu của giá trị trả về, ví dụ `int`, `float`, `char`, `void`.
- `<ten_ham>` là tên hàm.
- `<danh_sach_tham_so>` là các tham số đầu vào.
- `return` dùng để trả giá trị cho hàm.

Khi viết hàm cần xác định:

1. Tên hàm.
2. Công việc hàm thực hiện.
3. Đầu vào nếu có.
4. Đầu ra nếu có.

## 3. Ví dụ về hàm

**Ví dụ:** Hàm tính và xuất tổng hai số nguyên, không trả về giá trị.

```c
void XuatTong(int x, int y) {
    int s;
    s = x + y;
    printf("%d cong %d bang %d", x, y, s);
}
```

**Ví dụ:** Hàm tính tổng hai số nguyên và trả về kết quả.

```c
int TinhTong(int x, int y) {
    int s;
    s = x + y;
    return s;
}
```

**Ví dụ:** Hàm nhập và xuất tổng hai số nguyên.

```c
void NhapXuatTong() {
    int x, y, s;
    printf("Nhap 2 so nguyen: ");
    scanf("%d%d", &x, &y);
    s = x + y;
    printf("Tong la: %d", s);
}
```

## 4. Một số quy tắc khi dùng hàm

### Tham số hình thức và tham số thực sự

- Tham số hình thức là tham số dùng khi khai báo hoặc định nghĩa hàm.
- Tham số thực sự là giá trị, biến hoặc biểu thức được truyền vào khi gọi hàm.
- Tham số thực sự có thể là biểu thức, còn tham số hình thức không thể là biểu thức.

### Lệnh `return`

`return` dùng để trả giá trị cho hàm. Giá trị trả về có thể là một biểu thức.

```c
return x * x + b * x + c;
```

Một hàm có thể có nhiều lệnh `return`.

```c
if (s > 0)
    return s;
else
    return -s;
```

### Nguyên mẫu hàm

Hàm cần được khai báo trước khi sử dụng. Thông thường có thể đặt nguyên mẫu hàm trước `main`, còn phần định nghĩa hàm đặt phía sau.

```c
int Tong(int a, int b);

int main() {
    int a = 2912, b = 1706;
    int sum = Tong(a, b);
    return 0;
}

int Tong(int a, int b) {
    return a + b;
}
```

## 5. Tầm tác dụng của biến

### Biến toàn cục

Biến toàn cục được khai báo ngoài tất cả các hàm và có tác dụng trên toàn bộ chương trình.

```c
int i;
```

### Biến cục bộ

Biến cục bộ được khai báo trong hàm hoặc trong khối `{ }` và chỉ có tác dụng trong phạm vi khối đó.

```c
void thi_du() {
    int m = 3;
}
```

### Biến `static` và `register`

- `static` dùng để cấp phát bộ nhớ tĩnh cho biến cục bộ.
- `register` gợi ý dùng thanh ghi cho biến được sử dụng nhiều, thường là biến đếm vòng lặp.

```c
register int t;
for (t = 0; t < 1000; t++)
    printf("Lan goi thu %d", t);
```

## 6. Truyền tham số cho hàm

### Truyền tham trị

Truyền tham trị là truyền bản sao giá trị của biến vào hàm. Thay đổi trong hàm không làm thay đổi biến bên ngoài.

### Truyền địa chỉ

Truyền địa chỉ là truyền địa chỉ của biến vào hàm để hàm có thể thay đổi giá trị gốc.

### Truyền con trỏ

Truyền con trỏ tương tự truyền địa chỉ; biến bên ngoài có thể thay đổi khi thay đổi giá trị mà con trỏ trỏ tới.

```c
void HonHop(int x, int *y) {
    /* Xu ly */
}
```

Khi gọi hàm, cần truyền đối số theo đúng thứ tự đã khai báo.

```c
<ten_ham>(<doi_so_1>, <doi_so_2>);
```

## 7. Hàm đệ quy

Đệ quy là trường hợp một hàm gọi lại chính nó. Hàm đệ quy phải có điểm dừng để tránh gọi vô hạn.

Một hàm đệ quy thường gồm:

- Phần dừng: điều kiện kết thúc.
- Phần đệ quy: lời gọi lại chính hàm đó với bài toán nhỏ hơn.

**Ví dụ:** Tính giai thừa.

```c
int GT(int n) {
    if (n == 0)
        return 1;
    else
        return GT(n - 1) * n;
}
```

**Ví dụ:** Tính UCLN bằng đệ quy.

```c
int UCLN(int x, int y) {
    if (y == 0)
        return x;
    else
        return UCLN(y, x % y);
}
```

**Ví dụ:** Bài toán tháp Hà Nội.

```c
#include <stdio.h>

void CHUYEN(int N, char A, char B, char C);

int main() {
    int N;
    printf("Nhap so dia: ");
    scanf("%d", &N);
    CHUYEN(N, 'A', 'B', 'C');
    return 0;
}

void CHUYEN(int N, char A, char B, char C) {
    if (N == 1)
        printf("%c -> %c\n", A, B);
    else {
        CHUYEN(N - 1, A, C, B);
        CHUYEN(1, A, B, C);
        CHUYEN(N - 1, C, B, A);
    }
}
```

## 8. Một số hàm thông dụng

| Nhóm hàm | Ví dụ | Ý nghĩa |
|---|---|---|
| Giá trị tuyệt đối | `abs`, `labs`, `fabs` | Tính trị tuyệt đối |
| Ngẫu nhiên | `rand`, `srand`, `random` | Sinh số ngẫu nhiên |
| Lượng giác | `sin`, `cos`, `tan` | Tính các hàm lượng giác |
| Logarit, lũy thừa | `log`, `log10`, `pow` | Tính logarit, lũy thừa |
| Làm tròn | `ceil`, `floor` | Làm tròn lên, làm tròn xuống |
| Chuyển đổi xâu | `itoa`, `atoi`, `atof`, `atol` | Chuyển đổi giữa xâu và số |
| Cấp phát động | `malloc`, `calloc`, `realloc`, `free` | Quản lý bộ nhớ động |

## Bài tập thực hành

- Viết hàm tính số Fibonacci thứ `n`.
- Viết hàm kiểm tra số nguyên tố, số chính phương, số hoàn hảo.
- Viết hàm kiểm tra số đối xứng.
- Viết hàm trả về số đảo.
- Viết hàm tính tổ hợp chập `k` của `n`.
- Viết hàm tính `a^n` theo cách trực tiếp và đệ quy.
- Viết chương trình con in tất cả hoán vị của dãy `1 2 3 ... n` với `n < 10`.

## Tóm tắt

- Hàm giúp chương trình dễ tổ chức, tái sử dụng và kiểm thử.
- Cần xác định rõ tên hàm, đầu vào, đầu ra và công việc của hàm.
- Đệ quy là kỹ thuật hàm tự gọi chính nó và phải có điều kiện dừng.
