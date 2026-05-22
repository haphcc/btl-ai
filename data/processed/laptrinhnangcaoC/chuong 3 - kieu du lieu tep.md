# chuong 3 - kieu du lieu tep



<!-- page 1 -->

HC VIN NGN HNG
KHOA H THNG THNG TIN QUN L

# CHNG III  KIU D LIU TP

LP TRNH NNG CAO

**Ging vin**: L Vn Hng
 0906238311
 hunglv@hvnh.edu.vn


<!-- page 2 -->

# 1. Khái niệm

- Nếu máy tính của các bạn có ổ cứng, hoặc các bạn có USB hoặc bất kỳ thiết bị lưu trữ nào thì chắc chắn các bạn đã từng làm việc với File. Khi các bạn chơi một game offline, thông tin nhân vật, điểm số, ... sẽ được lưu trữ trong File để khi chương trình game bị tắt đi thì các bạn không phải chơi lại từ đầu. Khi các bạn cài đặt cấu hình cho một phần mềm và tắt đi, cấu hình đó được lưu vào File để lần làm việc tiếp theo sẽ sử dụng.
- **File trong C là một loại dữ liệu trong chương trình**, và một file khi nhập vào chương trình cũng sẽ được **lưu giữ** tại một vùng nào đó trên bộ nhớ máy tính.


<!-- page 3 -->

# 1. Khái niệm

- **Khác với các loại dữ liệu khác** có thể gán vào một biến để xử lý, thì để **thao tác với file**, chúng ta cần tạo ra một thực thể của kiểu cấu trúc FILE để chứa thông tin của file cần thao tác, sau đó sử dụng tới một **con trỏ để chỉ đến vị trí của thực thể FILE chứa thông tin file đó trên bộ nhớ**, qua đó thực hiện các thao tác với file thông qua các hàm có sẵn, với các chức năng cụ thể như đóng, mở, ghi hay lưu file.


<!-- page 4 -->

# 2. Các kiểu dữ liệu tệp

- **File văn bản – text files**
- **File nhị phân – binary file**


<!-- page 5 -->

# File văn bản – text files

- **File văn bản** là file thường có đuôi là .txt. Những file này chúng ta có thể dễ dàng tạo ra bằng cách dùng các text editer thông dụng như Notepad, Notepad++, Sublime Text,...
- Khi chúng ta mở các file này bằng các text editer nói trên, chúng ta sẽ thấy được văn bản ngay và có thể dễ dàng thao tác sửa, xóa, thêm nội dung của file này.
- Kiểu file này thuận tiện cho chúng ta trong việc sử dụng hàng ngày, nhưng nó sẽ kém bảo mật và cần nhiều bộ nhớ để lưu trữ hơn.


<!-- page 6 -->

# File nhị phân – binary file

- File nhị phân thường có đuôi mở rộng là **.bin**
- Thay vì lưu trữ dưới dạng văn bản thuần thúy, các file này được lưu dưới dạng nhị phân, chỉ bao gồm các số 0 và 1. Bạn cũng sẽ thấy các con số này nếu cố mở nó bằng 1 text editer kể trên.
- Loại file này giúp lưu trữ được dữ liệu với kích thước lớn hơn, không thể đọc bằng các text editer thông thường và thông tin lưu trữ ở loại file được bảo mật hơn so với file văn bản.


<!-- page 7 -->

# QUY TRÌNH XỬ LÝ FILE

## Quy trình xử lý file trong C

- Tạo con trỏ chỉ đến file trên bộ nhớ
- Mở file
- Đọc dữ liệu từ file
- Ghi file
- Đóng file


<!-- page 8 -->

# 2.1. File nhị phân – Binary files

- **Khai báo file:** `FILE * fptr;`
- **Thao tác mở file:**

`fptr = fopen (tênfile, “kiểu”);`

| Kiểu | Ý nghĩa |
| :--- | :--- |
| **rb** (b: binary) | mở chỉ để đọc |
| **wb** | để ghi. Nếu file đã có thì xóa trước khi mở. |
| **ab** | nối thêm; mở để ghi thêm vào cuối file, nếu u file chưa có thì tạo mới |
| **rb+** | mở file đã có để cập nhật (đọc/ghi) |
| **wb+** | tạo file mới cho phép đọc/ghi |
| **ab+** | mở để nối thêm về cuối file, cho phép đọc/ghi |


<!-- page 9 -->

# 2.1. File nhị phân – Binary files

- **Đóng tệp nhị phân: fclose (fptr)**
- **Đọc trong tệp nhị phân:**

`size_t fread(const void *ptr, size_t size, size_t n, FILE *f)`

- ptr: con trỏ chỉ đến vùng nhớ sẽ nhận dữ liệu từ tập tin.
- n: số phần tử được đọc từ tập tin.
- size: kích thước của mỗi phần tử.
- f: con trỏ tập tin đã được mở.

```c
fread(&d,sizeof(double),1,f);
fread(&i,sizeof(int),1,f);
fread(&l,sizeof(long),1,f);
```


<!-- page 10 -->

# 2.1. File nhị phân – Binary files

### **Ghi vào tệp nhị phân** `size_t fwrite(const void *ptr, size_t size, size_t n, FILE *f)`

Để ghi file nhị phân, bạn cần sử dụng hàm `fwrite()`. Hàm này cần 4 tham số: địa chỉ của biến lưu dữ liệu cần ghi, kích thước của biến lưu dữ liệu đó, số lượng kiểu dữ liệu của biến đó và con trỏ FILE trỏ tới file bạn muốn ghi.

```c
fwrite(&d,sizeof(double),1,f);
fwrite(&i,sizeof(int),1,f);
fwrite(&l,sizeof(long),1,f);
```


<!-- page 11 -->

# Ví dụ 1

- **Viết chương trình ghi lên tập tin number.txt 3 giá trị số (thực, nguyên, nguyên dài). Sau đó đọc các số từ tập tin vừa ghi và hiển thị lên màn hình.**


<!-- page 12 -->

# Ví dụ 1

```c
#include <stdio.h>
#include <conio.h>

int main()
{
    FILE *f;
    f=fopen("number.txt","wb");
    if (f!=NULL)
    {
        double d=3.14;
        int i=101;
        long l=54321;
        fwrite(&d,sizeof(double),1,f);
        fwrite(&i,sizeof(int),1,f);
        fwrite(&l,sizeof(long),1,f);
        /* Doc tu tap tin*/
        rewind(f);
        fread(&d,sizeof(double),1,f);
        fread(&i,sizeof(int),1,f);
        fread(&l,sizeof(long),1,f);
        printf("Cac ket qua la: %f %d %ld",d,i,l);
        fclose(f);
    }
    else
    {
        printf("Khong mo duoc file");
    }
    getch();
    return 0;
}
```


<!-- page 13 -->

# Ví dụ 2

- **Viết chương trình ghi lên tập tin danh sách học viên (mỗi học viên bao gồm họ tên, tuổi) vào file (tên file do người dùng nhập)**


<!-- page 14 -->

# Ví dụ 2

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{ struct hocvien
 { char hoten[30];
 int tuoi;
 } hv;
FILE *fptr;
char tenfile[67];
char tuoi[3];
printf("Nhap ten file :");
gets(tenfile);
if ((fptr=fopen(tenfile,"wb")) == NULL) // mở file nhị phân để ghi
{ printf ("Khong the tao file\n"); exit(0);
}
do
{ printf("Nhap ho ten hoc vien :");
gets(hv.hoten);
if (strlen(hv.hoten) !=0)
{ printf("Nhap tuoi :");
gets(tuoi);
hv.tuoi = atoi(tuoi); // macro doi chuoi qua so nguyen
fwrite(&hv, sizeof(hv), 1, fptr) ; // ghi noi dung 1 mau tin trong bien hv
// vao file fptr
}
}
while (strlen(hv.hoten)!=0);
fclose (fptr);
return 0;
}
```


<!-- page 15 -->

# Ví dụ 3

## Viết chương trình đọc file ở ví dụ 2

```c
// In danh sách học viên
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <windows.h>
int main()
{ struct hocvien
{ char hoten[30];
int tuoi;
} hv;
FILE *fptr;
char tenfile[67];
char tuoi[3];
printf("Nhap ten file :");
gets(tenfile);
if ((fptr=fopen(tenfile,"rb")) == NULL) // Mở file để đọc
{ printf("Khong the mo file\n"); exit(0);
}
system("cls");
printf(" Ho va ten Tuoi");
while (fread(&hv,sizeof(hv),1,fptr) ==1)
{
printf("\n%-20s",hv.hoten);
printf("%3d",hv.tuoi);
}
fclose (fptr);
return 1;
}
```


<!-- page 16 -->

# TỆP VĂN BẢN

- **Khai báo:** `FILE *fptr`
- **Mở file:** `FILE *fopen( const char * ten_file, const char * che_do );`

| Mode | Miêu tả |
| :--- | :--- |
| r | Mở các file đã tồn tại với mục đích đọc |
| w | Mở các file với mục đích ghi. Nếu các file này chưa tồn tại thì file mới được tạo ra. Ở đây, chương trình bắt đầu ghi nội dung từ phần mở đầu của file |
| a | Mở file văn bản cho việc ghi ở chế độ ghi tiếp theo vào cuối, nếu nó chưa tồn tại thì file mới được tạo. Đây là chương trình ghi nội dung với phần cuối của file đã tồn tại. |
| r+ | Mở file văn bản với mục đích đọc và ghi. |
| w+ | Mở một file văn bản cho chế độ đọc và ghi. Nó làm trắng file đã tồn tại nếu file này có và tạo mới nếu file này chưa có. |
| a+ | Mở file đã tồn tại với mục đích đọc và ghi. Nó tạo file mới nếu không tồn tại. Việc đọc file sẽ bắt đầu đọc từ đầu nhưng ghi file sẽ chỉ ghi vào cuối file. |


<!-- page 17 -->

# TỆP VĂN BẢN

- **Đóng file:** `int fclose( FILE *fp );`
- **Đọc/ghi ký tự:**
    - Đọc ký tự từ tập tin
        $ch = getc (fptr)$
    - Ghi ký tự lên tập tin
        $putc (ch, fptr)$


<!-- page 18 -->

# TỆP VĂN BẢN

## Đọc/ghi một chuỗi:

- Hàm **fgets** (chuỗi, chiều dài, fptr);
Hàm **fgets** đọc 1 chuỗi ký tự từ trong file fptr và vào biến <chuỗi> với chiều dài tối đa là <chiều dài>. Hàm này trả về NULL khi đã đọc hết file

- Hàm **fputs** (chuỗi, fptr): ghi 1 chuỗi ký tự trong <chuỗi> vào file fptr.
Hàm này không tự động thêm vào mã kết thúc để chuyển dòng mới, do đó ta phải ghi thêm mã này vào tập tin bằng lệnh **fputs ("\n", fptr);**


<!-- page 19 -->

# Ví dụ 3

**Viết chương trình đọc từng ký tự trong file vidu3.txt**

```c
#include <stdio.h>

int main(void)
{
    FILE * fp = NULL;
    //Mở file bằng hàm fopen
    fp= fopen("vidu3.txt", "r");

    char c;
    //Đọc từng ký tự từ file cho tới khi gặp EOF
    while ((c = fgetc(fp)) != EOF)
    {
        //Xuất từng ký tự ra màn hình
        printf("%c", c);
    }

    fclose(fp);

    return 0;
}
```


<!-- page 20 -->

# Ví dụ 4

**Viết chương trình đọc từng dòng trong file văn bản vidu4.txt**

```c
#include <stdio.h>

int main(void)
{
    FILE * fp = NULL;
    char arr[128];

    //Mở file bằng hàm fopen
    fp= fopen("vidu4.txt", "r");

    //Đọc dòng 1
    fgets(arr, 128, fp);
    printf("%s", arr);

    //Đọc dòng 2
    fgets(arr, 128, fp);
    printf("%s", arr);
}
```


<!-- page 21 -->

# Ví dụ 5

### Viết chương trình xóa file chỉ định

```c
#include <stdio.h>
int main()
{ char filename[80];
/* prompt for file name to delete */
printf("File muon xoa: ");
gets(filename);
/* delete the file */
if (remove(filename) == 0)
printf("Removed %s.\n",filename);
else
perror("remove"); // in thông báo lỗi mà hàm remove gây ra
return 0;
}
```


<!-- page 22 -->

# Ví dụ 6

- **Viết chương trình nhập thông tin sinh viên, lưu vào file. Sau đó, đọc file và in ra màn hình thông tin những sinh viên đã nhập**


<!-- page 23 -->

# Ví dụ 6

- **Viết chương trình nhập thông tin sinh viên, lưu vào file. Sau đó, đọc file và in ra màn hình thông tin những sinh viên đã nhập**


<!-- page 24 -->

# Ví dụ 6


<!-- page 25 -->

# Ví dụ 6


<!-- page 26 -->

# Bài tập chương 3

- **Viết chương trình nhập danh sách sinh viên vào tệp với tên do người dùng nhập vào: Mã học viên, tên, lớp, ngày sinh, Điểm toán, lý, hóa và tổng điểm**
- **Viết chương trình đọc danh sách sinh viên nhập ở trên**
- **Viết chương trình đếm xem có bao nhiêu sinh viên có tổng điểm >24**

```text
Ma cua hoc vien: A10
Ten cua hoc vien: Le Van Hung
Lop: A
Ngay sinh 20-11-1983
Diem toan: 10
Diem ly: 10
Diem hoa: 10
Tong diem: 30
Thong tin sinh vien thu 2
Ma cua hoc vien: A11
Ten cua hoc vien: Le Vu Gia Hung
Lop: B
Ngay sinh 02-12-2014
Diem toan: 10
Diem ly: 10
Diem hoa: 10
Tong diem: 30
Thong tin sinh vien thu 3
Ma cua hoc vien: A130
Ten cua hoc vien: Le Vu Gia Huy
Lop: C
Ngay sinh 27-04-2022
Diem toan: 10
Diem ly: 10
Diem hoa: 10
Tong diem: 30
```
