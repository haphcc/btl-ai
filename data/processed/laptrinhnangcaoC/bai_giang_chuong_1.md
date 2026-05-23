# bai_giang_chuong_1



<!-- page 1 -->


# HỌC VIỆN NGÂN HÀNG
# KHOA HỆ THỐNG THÔNG TIN QUẢN LÝ

# CHƯƠNG I  CẤU TRÚC ĐIỀU KHIỂN TRONG C

# LẬP TRÌNH NÂNG CAO

**Giảng viện**: Lê Văn Hùng
 0906238311
 hunglv@hvnh.edu.vn


<!-- page 2 -->

# 1. Cấu trúc tuần tự

Các lệnh trong chương trình được thực hiện tuần tự từ lệnh này tới lệnh khác cho tới khi kết thúc

**Ví dụ:** Viết chương trình tính và in ra diện tích của hai đường tròn bán kính lần lượt là 3m và 4.5m cùng với hiệu số của 2 diện tích

```c
#include <conio.h>
void main()
{
    float r1, r2, hieuso;
    clrscr();
    printf("\nCHUONG TRINH TINH DIEN TICH 2 HINH TRON VA HIEU SO\n");
    printf("Ban kinh hinh tron thu nhat : ");
    scanf("%f",&r1);
    printf("Ban kinh hinh tron thu hai : ");
    scanf("%f",&r2);
    printf ("Dien tich hinh tron 1 = %.2f\n",PI*r1*r1);
    printf ("Dien tich hinh tron 2 = %.2f\n",PI*r2*r2);
    hieuso = PI*r1*r1 - PI*r2*r2;
    printf ("Hieu so dien tich 2 hinh tron = %.2f\n",hieuso);
    getch();
}
```


<!-- page 3 -->

# 2.1. Cấu trúc chọn: Lệnh if

- **Câu lệnh if** cho phép lựa chọn một trong hai nhánh tùy thuộc vào giá trị của biểu thức luận lý là đúng (true) hay sai (false) hoặc khác không hay bằng không.
- **Dạng if thiếu**


<!-- page 4 -->

# Lệnh if

## Dạng if thiếu

Quyết định sẽ thực hiện hay không một khối lệnh.

- **Cú pháp lệnh**
    - Khối lệnh là một lệnh ta viết lệnh if như sau:
      ```
      if (biểu thức luận lý)
          lệnh;
      ```
    - Khối lệnh bao gồm nhiều lệnh: lệnh 1, lệnh 2..., ta viết lệnh if như sau:
      ```
      if (biểu thức luận lý)
      {
          lệnh 1;
          lệnh 2;
          ...
      }
      ```

- Nếu **khối lệnh** bao gồm từ 2 lệnh trở lên thì phải đặt trong dấu { }


<!-- page 5 -->

# Cấu trúc if thiếu

Ví dụ: Viết chương trình nhập vào 2 số nguyên a, b. Tìm và in ra số lớn nhất.

/* Chuong trinh tim so lon nhat tu 2 so nguyen a, b */
#include <stdio.h>
#include <conio.h>

void main(void)
{
    int ia, ib, imax;
    printf("Nhap vao so a: ");
    scanf("%d", &ia);
    printf("Nhap vao so b: ");
    scanf("%d", &ib);
    imax = ia;
    if (ib>ia)
        imax = ib;
    printf("So lon nhat = %d.\n", imax);
    getch();
}

| | |
| :--- | :--- |
| - Khai báo 3 biến | |
| - Nhập vào giá trị a | |
| - Nhập vào giá trị b | |
| - Gán a cho max | |
| - Nếu b > a thì | |
| gán b cho max | |
| - In ra kết quả | |


<!-- page 6 -->

# Cấu trúc if đủ

Quyết định sẽ thực hiện 1 trong 2 khối lệnh cho trước.

- **Cú pháp lệnh**

| | |
| :--- | :--- |
| **if (biểu thức luận lý)**<br>khối lệnh 1;<br>**else**<br>khối lệnh 2; | - từ khóa **if**, **else** phải viết bằng chữ thường<br>- kết quả của **biểu thức luận lý** phải là **đúng ($\neq 0$)** hoặc **sai ($= 0$)** |

- **Lưu đồ**

Vào $\rightarrow$ (bthức luận lý) $\xrightarrow{\text{Sai}}$ khối lệnh 2 $\rightarrow$ Ra
(bthức luận lý) $\xrightarrow{\text{Đúng}}$ khối lệnh 1 $\rightarrow$ Ra

- Nếu **biểu thức luận lý** đúng thì thực hiện khối lệnh 1 và thoát khỏi if
- Ngược lại thực hiện khối lệnh 2 và thoát khỏi if.

- Nếu **khối lệnh 1**, **khối lệnh 2** bao gồm từ 2 lệnh trở lên thì phải đặt trong dấu { }


<!-- page 7 -->

# Ví dụ Cấu trúc if đủ

**Viết chương trình nhập vào kí tự c. Kiểm tra xem nếu kí tự nhập vào là kí tự thường trong khoảng từ 'a' đến 'z' thì đổi sang chữ in hoa và in ra, ngược lại in ra thông báo "Kí tự bạn vừa nhập là: c".**

### a. Phác họa lời giải
Trước tiên bạn phải kiểm tra xem nếu kí tự c thuộc khoảng 'a' và 'z' thì đổi kí tự c thành chữ in hoa bằng cách lấy kí tự $c - 32$ rồi gán lại cho chính nó ($c = c - 32$) (vì giữa kí tự thường và in hoa trong bảng mã ASCII cách nhau 32, ví dụ: A trong bảng mã ASCII là 65, B là 66..., còn a là 97, b là 98...), sau khi đổi xong bạn in kí tự c ra. Ngược lại, in câu thông báo "Kí tự bạn vừa nhập là: c".

### b. Mô tả quy trình xử lý (giải thuật)

| Ngôn ngữ tự nhiên | Ngôn ngữ C |
| :--- | :--- |
| - Khai báo biến c kiểu kí tự | - char c; |
| - Nhập vào kí tự c | - printf("Nhap vao 1 ki tu: "); <br> scanf("%c", &c); |
| - Nếu $c >=$ 'a' và $c <=$ 'z' thì <br> $c = c - 32$ <br> in c ra màn hình | - if ($c >=$ 'a' && $c <=$ 'z') <br> { <br> $c = c - 32$; <br> printf("Ki tu hoa la: %c.\n", c); <br> }; |
| - Ngược lại <br> in ra thông báo " Kí tự bạn vừa nhập là: c " | - else <br> printf("Ki tu ban vua nhap la: %c.\n", c); |


<!-- page 8 -->

# Ví dụ Cấu trúc if đủ

❖ **Viết chương trình nhập vào kí tự c. Kiểm tra xem nếu kí tự nhập vào là kí tự thường trong khoảng từ 'a' đến 'z' thì đổi sang chữ in hoa và in ra, ngược lại in ra thông báo "Kí tự bạn vừa nhập là: c".**

/* Chuong trinh nhap vao ky tu c, neu c la chu thuong in ra chu IN HOA */
#include <stdio.h>
#include <conio.h>

void main(void)
{
    char c;
    printf("Nhap vao 1 ki tu: ");
    scanf("%c", &c);
    if (c >= 'a' && c <= 'z')        //hoac if(c >= 97 && c <= 122)
    {
        c = c - 32;                  //doi thanh chu in hoa
        printf("Ki tu hoa la: %c.\n", c);
    }
    else
    {
        printf("Ki tu ban vua nhap la: %c.\n", c);
    }
    getch();
}


<!-- page 9 -->

# Cấu trúc else if

Quyết định sẽ thực hiện 1 trong n khối lệnh cho trước.

### Cú pháp lệnh

```
if (biểu thức luận lý 1)
    khối lệnh 1;
else if (biểu thức luận lý 2)
    khối lệnh 2;
...
else if (biểu thức luận lý n-1)
    khối lệnh n-1;
else
    khối lệnh n;
```

- Từ khóa **if**, **else if**, **else** phải viết bằng chữ thường
- Kết quả của **biểu thức luận lý 1, 2..n** phải là **đúng ($\neq 0$)** hoặc **sai ($= 0$)**

- Nếu **khối lệnh 1, 2...n** bao gồm từ 2 lệnh trở lên thì phải đặt trong dấu { }


<!-- page 10 -->




<!-- page 11 -->

# Ví dụ Cấu trúc else if

- **Viết chương trình nhập vào kí tự c. Kiểm tra xem nếu kí tự nhập vào là kí tự thường trong khoảng từ 'a' đến 'z' thì đổi sang chữ in hoa và in ra, nếu kí tự in hoa trong khoảng A đến Z thì đổi sang chữ thường và in ra, nếu kí tự là số từ 0 đến 9 thì in ra câu "Kí tự bạn vừa nhập là số ...(in ra kí tự c)", còn lại không phải 3 trường hợp trên in ra thông báo "Bạn đã nhập kí tự ...(in ra kí tự c)".**

Nhập kí tự c vào, kiểm tra xem nếu kí tự c thuộc khoảng 'a' và 'z' đổi kí tự c thành chữ in hoa bằng cách lấy kí tự c – 32 rồi gán lại cho chính nó (c = c – 32) (vì giữa kí tự thường và in hoa trong bảng mã ASCII cách nhau 32, ví dụ: A trong bảng mã ASCII là 65, B là 66..., còn a là 97, b là 98...), sau khi đổi xong bạn in kí tự c ra. Ngược lại Nếu kí tự c thuộc khoảng 'A' và 'Z', đổi kí tự c thành chữ thường (theo cách ngược lại) và in ra. Ngược lại Nếu kí tự c thuộc khoảng '0' và '9' thì in ra thông báo "Kí tự bạn vừa nhập là số...". Ngược lại, in câu thông báo "Bạn đã nhập kí tự...".


<!-- page 12 -->

# Ví dụ Cấu trúc else if

| Ngôn ngữ tự nhiên | Ngôn ngữ C |
| :--- | :--- |
| - Khai báo biến c kiểu kí tự | - char c; |
| - Nhập vào kí tự c | - printf("Nhap vao 1 ki tu: "); <br> scanf("%c", &c); |
| - Nếu c >= a và c <= z thì <br> $c = c - 32$ <br> in c ra màn hình | - if (c >= 'a' && c <= 'z') <br> { <br> c = c - 32; <br> printf("Ki tu hoa la: %c.\n", c); <br> }; |
| Ngược lại Nếu c >= A và c <= Z thì <br> $c = c + 32$ <br> in c ra màn hình | else if(c >= 'A' && c <= 'Z') <br> { <br> c = c + 32; <br> printf("Ki tu thuong la: %c.\n", c); <br> } |


<!-- page 13 -->

# Ví dụ Cấu trúc else if

/* Chuong trinh nhap vao ki tu c. Doi ra hoa, thuong */

#include <stdio.h>
#include <conio.h>

void main(void)
{
    char c;
    printf("Nhap vao 1 ki tu: ");
    scanf("%c", &c);
    if (c >= 'a' && c <= 'z') //hoac if(c >= 97 && c <= 122)
    {
        c = c - 32; //doi thanh chu in hoa
        printf("Ki tu hoa la: %c.\n", c);
    };
    else if(c >= 'A' && c <= 'Z') //hoac if(c >= 65 && c <= 90)
    {
        c = c + 32; //doi thanh chu thuong
        printf("Ki tu thuong la: %c.\n", c);
    };
    else if(c >= '0' && c <= '9') //hoac if(c >= 48 && c <= 57)
        printf("Ki tu Ban vua nhap la so %c.\n", c);
    else
        printf("Ban da nhap ki tu %c.\n", c);
    getch();
}


<!-- page 14 -->

# 2.2. Cấu trúc chọn Sitwch_case : switch thiếu

## Chọn 1 trong n lệnh cho trước

- **Cú pháp lệnh**

| | |
| :--- | :--- |
| **switch (biểu thức)** <br> { <br> **case giá trị 1** : **lệnh 1**; <br> **break**; <br> **case giá trị 2** : **lệnh 2**; <br> **break**; <br> ... <br> **case giá trị n** : **lệnh n**; <br> [**break**;] <br> } | - từ khóa **switch**, **case**, **break** <br> phải viết bằng chữ thường <br> - **biểu thức** phải là có kết quả là <br> **giá trị hằng nguyên (char, int, long,...)** <br> - **Lệnh 1, 2...n** có thể gồm nhiều lệnh, nhưng <br> không cần đặt trong cặp dấu { } |


<!-- page 15 -->

# 2.2. Cấu trúc chọn Switch_case : switch thiếu

- **Lưu đồ**

Khi giá trị của biểu thức bằng giá trị i thì lệnh i sẽ được thực hiện. Nếu sau lệnh i không có lệnh break thì sẽ tiếp tục thực hiện lệnh i + 1... Ngược lại thoát khỏi cấu trúc switch.

| Thành phần | Mô tả |
| :--- | :--- |
| Vào | Điểm bắt đầu |
| Biểu thức | Kiểm tra giá trị |
| = giá trị 1 ? | Kiểm tra điều kiện 1 |
| = giá trị 2 ? | Kiểm tra điều kiện 2 |
| = giá trị n ? | Kiểm tra điều kiện n |
| Lệnh 1, 2, ..., n | Các khối lệnh thực thi |
| Break ? | Kiểm tra lệnh dừng |
| Ra | Điểm kết thúc |

**Quy trình:**
- Vào
- Biểu thức
- Nếu = giá trị 1 ? (Đúng) -> Lệnh 1 -> Break ? (Có) -> Ra
- Nếu = giá trị 1 ? (Đúng) -> Lệnh 1 -> Break ? (Không) -> Lệnh 2 -> ...
- Nếu = giá trị 2 ? (Đúng) -> Lệnh 2 -> Break ? (Có) -> Ra
- Nếu = giá trị 2 ? (Đúng) -> Lệnh 2 -> Break ? (Không) -> ...
- Nếu = giá trị n ? (Đúng) -> Lệnh n -> Break ? (Có) -> Ra
- Nếu = giá trị n ? (Đúng) -> Lệnh n -> Break ? (Không) -> Ra


<!-- page 16 -->

# Ví dụ Cấu trúc chọn Sitwch_case : switch thiếu

- **Viết chương trình nhập vào độ dài cạnh của hình vuông. Sau đó hỏi người dùng tính diện tích hay chu vi của hình vuông**

```c
#include <stdio.h>
#include <conio.h>
int main()
{
    int x;
    printf("Hay nhap do dai canh cua hinh vuong: ");
    scanf("%d",&x);
    printf("Ban muon tinh dien tich (nhap phim 1) hay tinh chu vi (nhap phim 2):");
    int i;
    scanf("%d",&i);
    switch(i)
    {
        case 1: printf("Dien tich cua hinh vuong la: %d\n",x*x);
                break;
        case 2: printf("Chu vi cua hinh vuong la: %d\n",4*x);
    };
    printf("An phim bat ky de ket thuc\n");
    getch();
}
```


<!-- page 17 -->

# 2.2. Cấu trúc chọn switch_case: switch đầy đủ

Chọn thực hiện 1 trong n + 1 lệnh cho trước.

- **Cú pháp lệnh**

| switch (biểu thức) |
| :--- |
| { |
| **case** giá trị 1 : lệnh 1; |
| **break**; |
| **case** giá trị 2 : lệnh 2; |
| **break**; |
| ... |
| **case** giá trị n : lệnh n; |
| **break**; |
| **default** : lệnh; |
| [**break**;] |
| } |

- Từ khóa **switch, case, break, default** phải viết bằng chữ thường
- **biểu thức** phải là có kết quả là giá trị nguyên (char, int, long,...)
- **Lệnh 1, 2...n** có thể gồm nhiều lệnh, nhưng không cần đặt trong cặp dấu { }


<!-- page 18 -->

# Ví dụ Cấu trúc chọn switch_case: switch đầy đủ

- **Viết chương trình tạo ra một máy tính có 4 phép toán +, -, *, /**

```c
#include <stdio.h>
#include <conio.h>
#include <windows.h>
int main()
{
    float num1, num2;
    char op;
    system("cls");
    printf ("Go vao so, toan tu, so \n");
    scanf("%f %c %f", &num1, &op, &num2);
    switch (op)
    {
        case '+': printf("= %f",num1+num2);
        break;
        case '-': printf("= %f",num1-num2);
        break;
        case '*': printf("= %f",num1*num2);
        break;
        case '/': printf("= %f",num1/num2);
        break;
        default : printf("Toan tu la khong biet");
    } ;
    printf("\n An phim bat ky de ket thuc") ;
    getch();
}
```


<!-- page 19 -->

# Ví dụ Cấu trúc chọn switch_case: switch đầy đủ

## Viết chương trình menu 2 cấp

```c
/* Chuong trinh menu 2 cap */

#include <stdio.h>
#include <include <conio.h>

void main(void)
{
    int imenu, isubmenu;
    printf("--------------------------\n");
    printf("      MAIN MENU \n");
    printf("--------------------------\n");
    printf("1. File\n");
    printf("2. Edit\n");
    printf("3. Search\n");
    printf("Chon muc tuong ung: ");
    scanf("%d", &imenu);

    switch(imenu)
    {
        case 1: printf("--------------------------\n");
                printf("      MENU FILE \n");
                printf("--------------------------\n");
                printf("1. New\n");
                printf("2. Open\n");
                printf("Chon muc tuong ung: ");
                scanf("%d", &isubmenu);
                switch(isubmenu)
                {
                    case 1: printf("Ban da chon chuc nang New File\n");
                            break;
                    case 2: printf("Ban da chon chuc nang Open File\n");
                }
                break; //break cua case 1 - switch(imenu)
        case 2: printf("Ban da chon chuc nang Edit\n");
                break;
        case 3: printf("Ban da chon chuc nang Search\n");
    };
    getch();
}
```


<!-- page 20 -->

# 3. Cấu trúc lặp

- 3.1. Lệnh While
- 3.2. Lệnh do_while
- 3.3. Lệnh for
- 3.4. Phát biểu break, continue, goto


<!-- page 21 -->

# 3.1. Lệnh for

**Cú pháp:**
for ([bt_khởi động]; [bt_đk]; [bt_lặp])
S;

**Ví dụ 1:** Lặp lệnh S từ 1 đến 10
for (int I=1; I== 10; I++) $\rightarrow$ **sai**
S;
for (int I=1; I<= 10; I++) $\rightarrow$ **đúng**
S;.

- từ khóa **for** phải viết bằng chữ thường
- Nếu **khối lệnh** bao gồm từ 2 lệnh trở lên thì phải đặt trong dấu { }

### Lưu đồ

- Vào
- Điều kiện
- **Đúng**
- **khối lệnh**
- **Sai**
- Ra

- kiểm tra **điều kiện**
- nếu **đúng** đúng thì thực hiện khối lệnh; lặp lại kiểm tra điều kiện
- nếu **sai** thoát khỏi vòng lặp.


<!-- page 22 -->

# Ví dụ lặp for

- **Viết chương trình nhập vào số nguyên dương n. Tính tổng các giá trị lẻ từ 0 đến n.**

/* Chuong trinh nhap vao 3 so va tinh tong */

#include <stdio.h>
#include <conio.h>

void main(void)
{
    int i, in, is = 0;
    printf("Nhap vao so n: ");
    scanf("%d", &in);
    is = 0;
    for(i = 0; i<=in; i++)
    {
        if (i % 2 != 0)        //neu i la so le
            is = is + i;       //hoac is += i;
    }
    printf("Tong: %d", is);
    getch();
}


<!-- page 23 -->

# Ví dụ lặp for

- **Đọc vào một loạt kí tự trên bàn phím. Kết thúc khi gặp dấu chấm '.' .**

```c
/* Doc vao 1 loat ktu tren ban phim. Ket thuc khi gap dau cham */
#include <stdio.h>

#define DAU_CHAM '.'

void main(void)
{
    char c;
    for(; (c = getchar()) != DAU_CHAM; )
        putchar(c);
}
```


<!-- page 24 -->

# Ví dụ lặp for

- **Đọc vào một loạt kí tự trên bàn phím, đếm số kí tự nhập vào. Kết thúc khi gặp dấu chấm '.'**

/* Doc vao 1 loat ktu tren ban phim, dem so ktu nhap vao. Ket thuc khi gap dau cham */

#include <stdio.h>
#include <conio.h>

#define DAU_CHAM '.'

void main(void)
{
    char c;
    int idem;
    for(idem = 0; (c = getchar()) != DAU_CHAM; )
        idem++;
    printf("So ki tu: %d.\n", idem);
    getch();
}


<!-- page 25 -->

# Ví dụ lặp for

- **Viết chương trình in ra bảng cửu chương**

```c
void main ()
{ int a;
  for (a=2; a<= 9; a++)
  { for (b =1; b <= 9; b++)
      printf("%d* %d = %d\t", a, b, a*b);
    printf("\n");
  }
}
```


<!-- page 26 -->

# 3.2. Lệnh while

| Cấu trúc | Lưu đồ thuật toán |
| :--- | :--- |
| While (bt)<br>S; | ![Lưu đồ thuật toán](https://i.imgur.com/5y11111.png) |

**Chú ý:** Trong phần thân lệnh phải có biến điều khiển vòng lặp.


<!-- page 27 -->

# Ví dụ: Lệnh while

- **Viết chương trình in ra câu "Vi du su dung vong lap while" 3 lần**

```c
/* Chuong trinh in ra cau "Vi du su dung vong lap while" 3 lan */

#include <stdio.h>
#include <conio.h>

#define MSG "Vi du su dung vong lap while.\n"

void main(void)
{
    int i = 0;
    while (i++ < 3)
        printf("%s", MSG);
    getch();
}
```


<!-- page 28 -->

# Ví dụ: Lệnh while

- **Viết chương trình tính tổng các số nguyên dương từ 1 đến n, với n được nhập vào từ bàn phím**

/* Chuong trinh tinh tong cac so nguyen tu 1 den n */

#include <stdio.h>
#include <conio.h>

void main(void)
{
    int i = 0, in, is = 0;
    printf("Nhap vao so n: ");
    scanf("%d", &in);
    while (i++ < in)
        is = is + i;        //hoac is += i;
    printf("Tong: %d", is);
    getch();
}


<!-- page 29 -->

# 3.3. Lệnh do_while

Vòng lặp thực hiện lặp lại cho đến khi biểu thức sai.

- **Cú pháp lệnh**

```
do
  khối lệnh;
while (biểu thức);
```

☞ từ khóa **do**, **while** phải viết bằng chữ thường
➦ Nếu **khối lệnh** bao gồm từ 2 lệnh trở lên thì phải đặt trong dấu { }


<!-- page 30 -->

# Ví dụ: Lệnh do_while

- **Viết chương trình in bảng mã ASCII**

```c
#include <stdio.h>
int main ()
{ int n=0;
do
{ printf("%c Co ma ASCII la %d\n",n,n);
n ++;
} while (n <= 255);
}
```


<!-- page 31 -->

# Ví dụ Lệnh do_while

❖ **Viết chương trình kiểm tra password.**

```c
/* Chuong trinh kiem tra mat khau */

#include <stdio.h>

#define PASSWORD 12345

void main(void)
{
    int in;
    do
    {
        printf("Nhap vao password: ");
        scanf("%d", &in);
    } while (in != PASSWORD)
}
```


<!-- page 32 -->

# Ví dụ Lệnh do_while

❖ **Viết chương trình nhập vào năm hiện tại, năm sinh. In ra tuoi.**

/* Chuong trinh in tuoi */

#include <stdio.h>

#define CHUC "Chuc ban vui ve (: \n"

void main(void)
{
unsigned char choi;
int inamhtai, inamsinh;
do
{
printf("Nhap vao nam hien tai: ");
scanf("%d", &inamhtai);
printf("Nhap vao nam sinh: ");
scanf("%d", &inamsinh);
printf("Ban %d tuoi, %s", inamhtai - inamsinh, CHUC);
printf("Ban co muon tiep tuc? (Y/N)\n");
choi = getch();
} while (choi == 'y' || choi == 'Y');
}


<!-- page 33 -->




<!-- page 34 -->

# 3.4. Phát biểu break, goto, continue

- **Break**: Giúp ta thoát ra sớm khỏi vòng lặp for/while/do_while
- **Continue**: Làm cho chương trình nhảy tắt về điều kiện kiểm tra của vòng lặp để bắt đầu một vòng lặp mới
- **Goto**: Chuyển ngay lập tức chương trình tới nhãn chỉ định.

**Cú pháp**: goto nhãn;


<!-- page 35 -->

# Bài tập chương

- 1. Viết chương trình in ra bảng mã ASCII
- 2. Viết chương trình tính tổng bậc 3 của N số nguyên đầu tiên.
- 3. Viết chương trình nhập vào một số nguyên rồi in ra tất cả các ước số của số đó.
- 4. Viết chương trình vẽ một tam giác cân bằng các dấu *
- 5. Viết chương trình tính tổng nghịch đảo của N số nguyên đầu tiên theo công thức $S = 1 + 1/2 + 1/3 + ... + 1/N$
- 6. Viết chương trình tính tổng bình phương các số lẻ từ 1 đến N.
- 7. Viết chương trình nhập vào N số nguyên, tìm số lớn nhất, số nhỏ nhất.
- 8. Viết chương trình nhập vào N rồi tính giai thừa của N.
- 9. Viết chương trình tìm USCLN, BSCNN của 2 số.
- 10. Viết chương trình vẽ một tam giác cân rỗng bằng các dấu *.


<!-- page 36 -->

# Bài tập chương

- 11. Viết chương trình vẽ hình chữ nhật rỗng bằng các dấu *.
- 12. Viết chương trình nhập vào một số và kiểm tra xem số đó có phải là số nguyên tố hay không?
- 13. Viết chương trình tính tiền điện

Người ta muốn lập hóa đơn cho khách hàng của Công ty điện lực. Chỉ số đầu và chỉ số cuối kỳ sẽ được cho biết. Biết rằng biểu giá được tính tùy theo điện năng tiêu thụ.
- Nếu điện năng tiêu thụ nhỏ hơn 100Kwh, giá mỗi Kwh là 500đ.
- Nếu điện năng tiêu thụ từ 100Kwh trở lên, thì mỗi Kwh dôi ra sẽ được tính giá là 800đ
- Phí khu vực là 5000đ cho mỗi khách hàng. Viết chương trình tính tiền phải trả tổng cộng gồm tiền điện, và phí khu vực


<!-- page 37 -->

# Bài tập chương

## 14. Chương trình trò chơi

Viết chương trình đoán số: người chơi sẽ đoán 1 số trong phạm vi từ 0 đến 100, tối đa 5 lần. Chương trình kiểm tra kết quả và xuất thông báo hướng dẫn:
- Số bạn đoán lớn hơn
- Số bạn đoán nhỏ hơn
- Bạn đoán đúng
- Máy thắng cuộc