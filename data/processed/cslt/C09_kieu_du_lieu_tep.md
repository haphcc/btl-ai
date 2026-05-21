# Kiểu dữ liệu tệp

## Nội dung chính
- Khái niệm tệp và phân loại tệp.
- Biến tệp, con trỏ tệp và các bước xử lý tệp.
- Mở, đóng, đọc và ghi tệp trong C.
- Tệp văn bản và tệp nhị phân.
- Di chuyển con trỏ tệp.
- Truyền tham số là tệp cho hàm.

## Tổng quan
Tệp cho phép lưu trữ dữ liệu lâu dài trên thiết bị nhớ ngoài. Trong C, thao tác với tệp được thực hiện thông qua biến kiểu `FILE *` và các hàm trong thư viện `stdio.h`.

## 1. Khái niệm kiểu tệp

Tệp là tập hợp các dữ liệu có liên quan với nhau, được nhóm lại thành một dãy và lưu trên thiết bị nhớ ngoài. Kích thước và số lượng tệp gần như không bị giới hạn như dữ liệu trong bộ nhớ chính.

### Phân loại theo cách truy cập

- Tệp truy cập tuần tự: muốn đọc một phần tử bất kỳ phải đi qua các phần tử trước đó.
- Tệp truy cập ngẫu nhiên: có thể truy xuất phần tử bất kỳ thông qua vị trí hoặc chỉ số phần tử trong tệp.

### Phân loại theo bản chất dữ liệu

| Loại tệp | Đặc điểm | Ví dụ |
|---|---|---|
| Tệp văn bản | Chứa các ký tự ASCII, dữ liệu lưu theo dòng | `*.txt` |
| Tệp nhị phân | Chứa dữ liệu dạng nhị phân, có thể gồm ký tự điều khiển | `*.exe`, `*.com` |

## 2. Một số khái niệm

### Biến tệp

Biến tệp là biến đại diện cho một tệp tin. Dữ liệu trong tệp được truy xuất thông qua các thao tác với biến tệp.

### Con trỏ tệp

Con trỏ tệp xác định vị trí hiện tại để đọc hoặc ghi dữ liệu. Khi mở tệp để đọc hoặc ghi, con trỏ tệp thường ở vị trí đầu tệp. Sau mỗi lần đọc hoặc ghi, con trỏ tệp tự động dịch chuyển theo số byte vừa xử lý.

## 3. Các bước xử lý tệp

1. Khai báo biến tệp.
2. Mở tệp để đọc hoặc ghi.
3. Xử lý dữ liệu trong tệp.
4. Đóng tệp.

## 4. Khai báo và mở tệp

### Khai báo biến tệp

```c
FILE *f1, *f2;
```

`FILE` phải viết hoa và các biến tệp là biến con trỏ.

### Mở tệp bằng `fopen`

```c
<bien_tep> = fopen(<ten_tep>, <kieu_xu_ly_tep>);
```

Ví dụ:

```c
f1 = fopen("C:\\TC\\VIDU.TXT", "w");
f2 = fopen("C:\\TC\\VIDU.TXT", "r");
```

Nếu mở tệp lỗi, `fopen` trả về `NULL`.

### Các chế độ mở tệp

| Chế độ | Ý nghĩa |
|---|---|
| `r` | Mở tệp văn bản để đọc |
| `w` | Mở tệp văn bản để ghi, ghi đè nếu tệp đã có |
| `a` | Mở tệp văn bản để ghi nối vào cuối |
| `r+` | Mở tệp văn bản để đọc và ghi |
| `w+` | Mở tệp văn bản để ghi và đọc, ghi đè nếu tệp đã có |
| `a+` | Mở hoặc tạo tệp văn bản để đọc và ghi nối |
| `rb` | Mở tệp nhị phân để đọc |
| `wb` | Mở tệp nhị phân để ghi |
| `ab` | Ghi nối vào tệp nhị phân |
| `r+b` | Mở tệp nhị phân để đọc và ghi |
| `w+b` | Tạo tệp nhị phân để đọc và ghi |
| `a+b` | Nối hoặc tạo mới tệp nhị phân |

**Ví dụ:** Mở tệp để ghi.

```c
FILE *f;
f = fopen("VIDU.txt", "w");

if (f != NULL) {
    /* Cac cau lenh thao tac voi tep */
    fclose(f);
} else {
    printf("Loi - Khong mo duoc tep!");
}
```

## 5. Các thao tác cơ bản

### Đóng tệp

```c
fclose(f);
```

Hàm trả về `0` nếu đóng tệp thành công, trả về `EOF` nếu có lỗi.

### Kiểm tra kết thúc tệp

```c
feof(f);
```

### Đưa con trỏ tệp về đầu

```c
rewind(f);
```

## 6. Tệp văn bản

### Ghi dữ liệu lên tệp văn bản

Các hàm thường dùng:

- `putc(ch, f)`: ghi một ký tự vào tệp.
- `fputs(str, f)`: ghi một xâu vào tệp.
- `fprintf(f, chuoi_dinh_dang, danh_sach_bieu_thuc)`: ghi dữ liệu theo định dạng.

**Ví dụ:** Ghi một dòng chữ hoa vào tệp.

```c
#include <stdio.h>
#include <ctype.h>

int main() {
    FILE *f;
    char c;

    f = fopen("C:\\sample.txt", "w");
    do {
        putc(toupper(c = getchar()), f);
    } while (c != '\n');

    fclose(f);
    return 0;
}
```

**Ví dụ:** Ghi xâu vào tệp.

```c
FILE *f;
f = fopen("C:\\vidu.txt", "w");
fputs("Ngon ngu lap trinh C", f);
fclose(f);
```

### Đọc dữ liệu từ tệp văn bản

Các hàm thường dùng:

- `getc(f)` hoặc `fgetc(f)`: đọc một ký tự.
- `fgets(str, n, f)`: đọc một xâu.
- `fscanf(f, chuoi_dinh_dang, danh_sach_bien)`: đọc dữ liệu theo định dạng.

**Ví dụ:** Sao chép tệp văn bản.

```c
int main() {
    FILE *f1, *f2;
    int ch;

    f1 = fopen("C:\\sample.txt", "r");
    f2 = fopen("C:\\sp.txt", "w");

    if (f1 != NULL && f2 != NULL) {
        ch = fgetc(f1);
        while (!feof(f1)) {
            fputc(ch, f2);
            ch = fgetc(f1);
        }
        fclose(f1);
        fclose(f2);
    }

    return 0;
}
```

## 7. Tệp nhị phân

### Ghi dữ liệu bằng `fwrite`

```c
fwrite(<dia_chi_khoi_du_lieu>, <kich_thuoc_moi_phan_tu>, <so_phan_tu>, f);
```

**Ví dụ:** Ghi 100 số nguyên vào tệp nhị phân.

```c
FILE *f;
int i;

f = fopen("C:\\SN100.txt", "wb");
for (i = 1; i <= 100; i++)
    fwrite(&i, sizeof(int), 1, f);
fclose(f);
```

### Đọc dữ liệu bằng `fread`

```c
fread(<dia_chi_vung_nho_nhan>, <kich_thuoc_moi_phan_tu>, <so_phan_tu>, f);
```

```c
FILE *g;
int i;

g = fopen("C:\\SN100.txt", "rb");
do {
    fread(&i, sizeof(int), 1, g);
    if (!feof(g))
        printf("%d", i);
} while (!feof(g));
fclose(g);
```

## 8. Di chuyển con trỏ tệp

Hàm `fseek` dùng để di chuyển con trỏ tệp.

```c
fseek(f, No * kich_thuoc, vi_tri);
```

Các vị trí:

| Giá trị | Ý nghĩa |
|---|---|
| `SEEK_SET` hoặc `0` | Di chuyển từ đầu tệp |
| `SEEK_CUR` hoặc `1` | Di chuyển từ vị trí hiện tại |
| `SEEK_END` hoặc `2` | Di chuyển từ cuối tệp |

**Ví dụ:** Cập nhật trực tiếp một số nguyên trong tệp nhị phân.

```c
FILE *f;
int no, number;

f = fopen("C:\\SN100.txt", "r+b");
do {
    printf("Vi tri can cap nhat: ");
    scanf("%d", &no);
    printf("Gia tri can cap nhat: ");
    scanf("%d", &number);

    if (no > 0) {
        fseek(f, sizeof(int) * (no - 1), SEEK_SET);
        fwrite(&number, sizeof(int), 1, f);
    }
} while (no != 0);

fclose(f);
```

## 9. Ví dụ quản lý sinh viên bằng tệp

Bài toán quản lý sinh viên yêu cầu:

- Nhập danh sách sinh viên từ bàn phím và ghi vào `SinhVien.dat`.
- Đọc dữ liệu từ `SinhVien.dat` và hiển thị danh sách.
- Tìm kiếm họ tên sinh viên theo mã sinh viên.

Kiểu dữ liệu sinh viên:

```c
typedef struct {
    char Ma[10];
    char HoTen[40];
} SinhVien;
```

Ghi sinh viên vào tệp nhị phân:

```c
void WriteFile(char *FileName) {
    FILE *f;
    int n, i;
    SinhVien sv;

    f = fopen(FileName, "wb");
    printf("Nhap bao nhieu sinh vien?");
    scanf("%d", &n);
    fflush(stdin);

    for (i = 1; i <= n; i++) {
        printf("Sinh vien thu %i\n", i);
        printf(" - MSSV: ");
        gets(sv.Ma);
        printf(" - Ho ten: ");
        gets(sv.HoTen);
        fwrite(&sv, sizeof(sv), 1, f);
        fflush(stdin);
    }

    fclose(f);
}
```

## 10. Các hàm xử lý tệp

| Hàm | Ý nghĩa |
|---|---|
| `ferror(FILE *fp)` | Kiểm tra lỗi tệp |
| `remove(char *filename)` | Xóa tệp |
| `rename(char *old, char *new)` | Đổi tên tệp |
| `fflush(FILE *fp)` | Đổ bộ nhớ đệm |
| `ftell(FILE *fp)` | Cho biết vị trí hiện tại của con trỏ tệp |

## 11. Truyền tham số là tệp cho hàm

Khi chương trình nhận tham số dòng lệnh, có thể dùng `argc`, `argv` để lấy tên tệp nguồn và tệp đích.

**Ví dụ:** Sao chép hai tệp.

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    FILE *in, *out;
    char ch;

    if (argc != 3) {
        printf("Chua co ten tep.\n");
        exit(1);
    }

    if ((in = fopen(argv[1], "rb")) == NULL) {
        printf("Khong the mo tep nguon!");
        exit(1);
    }

    if ((out = fopen(argv[2], "wb")) == NULL) {
        printf("Khong the mo tep dich!");
        exit(1);
    }

    while (!feof(in)) {
        ch = getc(in);
        if (!feof(in))
            putc(ch, out);
    }

    printf("Da sao chep xong!");
    fclose(in);
    fclose(out);
    return 0;
}
```

## Bài tập thực hành

- Đếm số chữ từng loại trong bảng chữ cái từ một tệp văn bản.
- Đếm số dòng, số ký tự, dòng dài nhất và từ dài nhất trong tệp văn bản.
- Đọc dãy số nguyên từ `songuyen.txt` và tạo các tệp `prime.txt`, `cp.txt`, `dep.txt`, `hoanhao.txt`.
- Sắp xếp các số trong hai tệp `So1.txt`, `So2.txt` và tạo tệp `So3.txt` đã sắp xếp tăng dần.

## Tóm tắt

- Làm việc với tệp trong C cần khai báo `FILE *`, mở tệp, xử lý dữ liệu và đóng tệp.
- Tệp văn bản dùng các hàm như `fgetc`, `fputs`, `fprintf`, `fscanf`.
- Tệp nhị phân dùng `fread`, `fwrite`.
- `fseek` cho phép truy cập trực tiếp vị trí dữ liệu trong tệp.

