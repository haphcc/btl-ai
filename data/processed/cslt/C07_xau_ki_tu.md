# Xâu kí tự

## Nội dung chính
- Khai báo xâu kí tự trong C.
- Nhập và xuất xâu.
- Xác định độ dài, ghép, sao chép, so sánh xâu.
- Tìm kiếm kí tự hoặc xâu con.
- Mảng xâu kí tự.
- Một số hàm xử lý xâu và kí tự.

## Tổng quan
Trong C, xâu kí tự được xây dựng như một mảng một chiều các kí tự và kết thúc bằng kí tự `'\0'`. Vì vậy, xử lý xâu trong C gắn liền với mảng, con trỏ và các hàm trong thư viện `string.h`, `ctype.h`, `stdlib.h`.

## 1. Khai báo xâu kí tự

Xâu kí tự trong C là mảng các kí tự kết thúc bằng kí tự null `'\0'`.

Do cần một ô nhớ để chứa `'\0'`, độ dài tối đa của xâu bằng kích thước mảng trừ 1.

```c
char line[80];   // Dài tối đa 79 kí tự
char hoten[30];  // Dài tối đa 29 kí tự
```

### Khai báo có khởi tạo

Khai báo với độ dài cụ thể:

```c
char string[40] = "Ngon ngu C";
```

Khai báo để chương trình dịch tự xác định độ dài:

```c
char str[] = "Ngon ngu C";
```

Cũng có thể khai báo xâu bằng con trỏ:

```c
char *message;
message = "Xin chao!";
```

## 2. Các thao tác trên xâu kí tự

### Nhập xâu bằng `scanf`

Khi dùng `scanf` với `%s`, chương trình chỉ nhận đến trước dấu cách, tab hoặc xuống dòng.

```c
char monhoc[50];
printf("Nhap mot xau ki tu: ");
scanf("%s", monhoc);
printf("Xau nhan duoc la: %s", monhoc);
```

Nếu nhập `Ngon ngu lap trinh C`, xâu nhận được chỉ là `Ngon`.

### Nhập xâu bằng `gets`

`gets` nhận các kí tự cho đến khi gặp xuống dòng, nên có thể đọc cả xâu có khoảng trắng.

```c
char monhoc[50];
printf("Nhap mot chuoi: ");
gets(monhoc);
printf("Chuoi nhan duoc la: %s", monhoc);
```

### Xuất xâu

Có thể dùng `printf` với `%s` hoặc dùng `puts`.

```c
char monhoc[50] = "Ngon ngu C";
printf("%s", monhoc);
puts(monhoc);
```

## 3. Xác định độ dài xâu

### Tự đếm đến `'\0'`

```c
char str[] = "Ngon ngu C";
int dem = 0;

while (str[dem] != '\0')
    dem++;

printf("Do dai xau la: %d ki tu", dem);
```

### Dùng con trỏ

```c
char *message = "Ngon ngu C";
int dem = 0;

while (*message != '\0') {
    message++;
    dem++;
}

printf("Do dai xau la: %d ki tu", dem);
```

### Dùng hàm `strlen`

```c
#include <string.h>

printf("Do dai xau la: %d", strlen(str));
```

## 4. Ghép, sao chép và so sánh xâu

### Ghép xâu

Hàm `strcat(st1, st2)` nối xâu `st2` vào sau xâu `st1`.

```c
#include <stdio.h>
#include <string.h>
#define maxst 40

int main() {
    char st1[maxst] = "Chao mung";
    char st2[maxst] = "Ngon ngu C";

    if (maxst > strlen(st1) + strlen(st2))
        puts(strcat(st1, st2));
    else
        printf("Khong du bo nho!");

    return 0;
}
```

Không viết `st = st1 + st2` để ghép xâu trong C.

### Sao chép xâu

C không cho phép gán trực tiếp một xâu cho biến mảng, ví dụ không viết:

```c
line = "Hello";
```

Cần dùng `strcpy`:

```c
strcpy(line, "Hello");
```

Khi dùng `strcpy`, cần chú ý kích thước vùng nhớ đích có đủ chứa xâu nguồn hay không.

### So sánh xâu

Hàm `strcmp(st1, st2)` so sánh hai xâu theo mã ASCII:

- Trả về `0` nếu `st1 == st2`.
- Trả về giá trị âm nếu `st1 < st2`.
- Trả về giá trị dương nếu `st1 > st2`.

```c
char st[80];
do {
    gets(st);
    printf("Xau vua nhap: %s\n", st);
} while (strcmp(st, "done"));
```

Một số hàm so sánh khác:

| Hàm | Ý nghĩa |
|---|---|
| `stricmp(st1, st2)` | So sánh không phân biệt hoa thường |
| `strncmp(st1, st2, n)` | So sánh `n` kí tự đầu |
| `strnicmp(st1, st2, n)` | So sánh `n` kí tự đầu, không phân biệt hoa thường |

## 5. Tìm kiếm kí tự và xâu con

Hàm `strchr(str, c)` tìm kí tự `c` trong xâu `str`. Nếu tìm thấy, hàm trả về con trỏ tới vị trí đó; nếu không, trả về `NULL`.

```c
char str[80];
char c;

printf("Nhap xau: ");
gets(str);
printf("Nhap ki tu can tim: ");
c = getchar();

if (strchr(str, c))
    printf("Tim thay %c", c);
else
    printf("Khong tim thay!");
```

Hàm `strstr(str1, str2)` tìm xâu `str2` trong xâu `str1`.

## 6. Mảng xâu kí tự

Mảng xâu kí tự có thể được lưu bằng mảng hai chiều. Ví dụ, sắp xếp các xâu theo thứ tự từ điển:

```c
void sapxep(int n, char x[][80]) {
    char temp[80];
    int i, j;

    for (i = 0; i < n - 1; i++) {
        for (j = i + 1; j < n; j++) {
            if (strcmp(x[i], x[j]) > 0) {
                strcpy(temp, x[i]);
                strcpy(x[i], x[j]);
                strcpy(x[j], temp);
            }
        }
    }
}
```

Nhập các xâu đến khi gặp `"end"`:

```c
char st[40][80];
int i, n = 0;

printf("Nhap cac xau ki tu, ket thuc bang chu \"end\"\n");
do {
    printf("Nhap xau thu %d: ", n + 1);
    gets(st[n]);
} while (strcmp(st[n++], "end"));

n--;
sapxep(n, st);

printf("Day cac xau ki tu sau khi sap xep\n");
for (i = 0; i < n; i++)
    puts(st[i]);
```

## 7. Một số hàm xử lý xâu và kí tự

| Thư viện | Hàm | Ý nghĩa |
|---|---|---|
| `string.h` | `strlwr(st)` | Chuyển xâu thành chữ thường |
| `string.h` | `strupr(st)` | Chuyển xâu thành chữ hoa |
| `string.h` | `strrev(st)` | Đảo ngược xâu |
| `ctype.h` | `toupper(c)` | Chuyển kí tự thành chữ hoa |
| `ctype.h` | `tolower(c)` | Chuyển kí tự thành chữ thường |
| `ctype.h` | `isalpha(c)` | Kiểm tra chữ cái |
| `ctype.h` | `islower(c)` | Kiểm tra chữ thường |
| `ctype.h` | `isupper(c)` | Kiểm tra chữ hoa |
| `ctype.h` | `isspace(c)` | Kiểm tra khoảng trắng, xuống dòng, tab |
| `stdlib.h` | `atoi(str)` | Chuyển xâu thành số nguyên |
| `stdlib.h` | `atol(str)` | Chuyển xâu thành số nguyên long |
| `stdlib.h` | `atof(str)` | Chuyển xâu thành số thực |

## Bài tập thực hành

- Viết hàm `upper(char s[])` đổi toàn bộ kí tự sang chữ hoa.
- Viết hàm `lower(char s[])` đổi toàn bộ kí tự sang chữ thường.
- Viết hàm `proper(char s[])` đổi kí tự đầu mỗi từ sang chữ hoa.
- Đếm số từ trong xâu và in các từ ra màn hình.
- Viết các hàm `left`, `right`, `mid`.
- Tìm từ có độ dài lớn nhất trong xâu.
- Xóa tất cả khoảng trắng trong xâu.
- Chuẩn hóa xâu để đầu, cuối không có khoảng trắng và giữa hai từ chỉ còn một khoảng trắng.
- Đếm số lượng từ `"em"` trong xâu.
- Kiểm tra một từ có phải là palindrome hay không.

## Tóm tắt

- Xâu kí tự trong C là mảng kí tự kết thúc bằng `'\0'`.
- Các thao tác xâu thường dùng hàm trong `string.h`.
- Khi sao chép hoặc ghép xâu cần chú ý kích thước vùng nhớ.

