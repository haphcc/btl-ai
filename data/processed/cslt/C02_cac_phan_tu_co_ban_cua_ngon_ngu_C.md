# Các phần tử cơ bản của ngôn ngữ C

## Nội dung chính
- Các thành phần cơ bản của ngôn ngữ C.
- Cấu trúc một chương trình C.
- Các kiểu dữ liệu cơ sở.
- Hằng, biến và quy tắc đặt tên.
- Toán tử trong C.
- Các lệnh vào ra cơ bản.

## Tổng quan
Chương này trình bày những thành phần nền tảng để viết chương trình C: bộ ký tự, từ khóa, tên, câu lệnh, chú thích, kiểu dữ liệu, biến, hằng, toán tử và các lệnh nhập xuất.

## 1. Các thành phần cơ bản

### Bộ ký tự

Chương trình C được viết từ các ký tự chữ cái, chữ số và các ký hiệu đặc biệt. Các ký tự này kết hợp thành từ khóa, tên, hằng, toán tử và câu lệnh.

### Từ khóa

Từ khóa là những từ có ý nghĩa xác định sẵn trong ngôn ngữ C. Không được dùng từ khóa để đặt tên biến, tên hàm hoặc tên chương trình con.

### Tên trong C

Tên dùng để đặt cho biến, hằng, hàm hoặc các đối tượng khác trong chương trình. Tên thường gồm chữ cái, chữ số và dấu gạch dưới, không bắt đầu bằng chữ số.

### Câu lệnh và chú thích

Các câu lệnh trong C thường kết thúc bằng dấu `;`.

```c
printf("Hello World!");
printf("\n");
```

Chú thích có thể viết theo hai dạng:

```c
/* Ho va ten: NVA */
// MSSV: 0712078
```

## 2. Cấu trúc chương trình C

Một chương trình C thường gồm phần khai báo thư viện, khai báo hằng, nguyên mẫu hàm và hàm `main`.

```c
#include <stdio.h>
#define PI 3.14

int main() {
    /* Cac cau lenh */
    return 0;
}
```

**Ví dụ:** In một dòng chữ ra màn hình.

```c
#include <stdio.h>
#include <conio.h>

int main() {
    printf("CHAO MUNG DEN VOI NGON NGU C");
    getch();
    return 0;
}
```

## 3. Các kiểu dữ liệu cơ sở

### Kiểu số nguyên

Kiểu số nguyên dùng để lưu các giá trị không có phần thập phân. Các kiểu thường gặp gồm `char`, `int`, `short`, `long` và các biến thể `unsigned`.

Hằng số nguyên có thể viết ở nhiều hệ:

- Hệ thập phân: `65`.
- Hệ thập lục phân: `0x41` hoặc `0X41`.
- Hệ bát phân: `0101`.
- Có thể dùng hậu tố như `U`, `L`, ví dụ `50000U`, `012345L`.

Trong C, phép chia hai số nguyên cho kết quả nguyên:

```c
int x = 3 / 2;  // x nhận giá trị 1
```

### Kiểu số thực

Kiểu số thực dùng để lưu giá trị có phần thập phân. Các kiểu thường gặp gồm `float`, `double`, `long double`.

Ví dụ hằng số thực:

```c
3.14
3.0
-24.12345
6.2144E+02
```

### Kiểu ký tự

Kiểu ký tự lưu một ký tự, đặt trong dấu nháy đơn:

```c
char c = 'A';
```

Ký tự cũng có thể biểu diễn bằng mã, ví dụ ký tự `'A'` tương ứng với `\x41` hoặc `\101`.

### Kiểu xâu ký tự

Xâu ký tự là dãy ký tự đặt trong dấu nháy kép. Trong C, xâu kết thúc bằng ký tự `'\0'`.

```c
char s[] = "Viet nam";
```

### Kiểu logic

Trong C, giá trị `0` được xem là sai, giá trị khác `0` được xem là đúng.

## 4. Hằng và biến

Biến là vùng nhớ có tên, dùng để lưu dữ liệu trong quá trình chương trình chạy. Hằng là giá trị không thay đổi trong chương trình.

Ví dụ khai báo biến:

```c
int a;
float r;
char ch;
```

Ví dụ khai báo hằng:

```c
#define MAX 100
#define PI 3.14
```

## 5. Toán tử

Các nhóm toán tử thường dùng trong C gồm:

| Nhóm toán tử | Ví dụ | Ý nghĩa |
|---|---|---|
| Số học | `+`, `-`, `*`, `/`, `%` | Tính toán số học |
| Quan hệ | `>`, `<`, `>=`, `<=`, `==`, `!=` | So sánh |
| Logic | `&&`, `||`, `!` | Kết hợp điều kiện |
| Gán | `=`, `+=`, `-=`, `*=`, `/=` | Gán giá trị |
| Tăng giảm | `++`, `--` | Tăng hoặc giảm một đơn vị |

## 6. Các lệnh vào ra

### Xuất dữ liệu với `printf`

```c
printf("Gia tri cua a la: %d", a);
```

### Nhập dữ liệu với `scanf`

```c
int a;
printf("Nhap a: ");
scanf("%d", &a);
```

Một số đặc tả định dạng thường dùng:

| Đặc tả | Kiểu dữ liệu |
|---|---|
| `%d` | Số nguyên |
| `%f` | Số thực |
| `%c` | Ký tự |
| `%s` | Xâu ký tự |

## Lưu ý khi viết chương trình C

- C phân biệt chữ hoa và chữ thường.
- Mỗi câu lệnh thường kết thúc bằng dấu `;`.
- Khi nhập dữ liệu bằng `scanf`, cần truyền địa chỉ của biến bằng toán tử `&`.
- Chuỗi ký tự đặt trong dấu nháy kép, ký tự đặt trong dấu nháy đơn.

## Tóm tắt

- Chương trình C được xây dựng từ từ khóa, tên, hằng, biến, toán tử và câu lệnh.
- Hàm `main` là điểm bắt đầu thực thi chương trình.
- C hỗ trợ nhiều kiểu dữ liệu cơ sở và các lệnh nhập xuất cơ bản qua `printf`, `scanf`.
