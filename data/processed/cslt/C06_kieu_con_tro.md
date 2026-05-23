# Kiểu con trỏ

## Nội dung chính
- Khái niệm địa chỉ và con trỏ.
- Khai báo, gán địa chỉ và truy xuất qua con trỏ.
- Quan hệ giữa con trỏ và mảng một chiều.
- Con trỏ và mảng hai chiều.
- Mảng con trỏ.

## Tổng quan
Con trỏ là một đặc trưng quan trọng của C. Con trỏ cho phép làm việc trực tiếp với địa chỉ bộ nhớ, hỗ trợ truyền tham số theo địa chỉ, xử lý mảng linh hoạt và quản lý dữ liệu động.

## 1. Con trỏ và địa chỉ

Mỗi biến trong chương trình có tên, kiểu dữ liệu, giá trị và địa chỉ trong bộ nhớ.

Con trỏ là biến dùng để lưu địa chỉ của một biến khác. Khi một con trỏ trỏ tới một biến, có thể truy xuất hoặc thay đổi giá trị của biến đó thông qua con trỏ.

## 2. Khai báo con trỏ

Cú pháp khai báo:

```c
<kieu_du_lieu> *<ten_con_tro>;
```

Ví dụ:

```c
int *p;
float *p1, *p2;
```

Gán địa chỉ của biến cho con trỏ bằng toán tử `&`:

```c
int a = 10;
int *p;
p = &a;
```

Truy xuất giá trị mà con trỏ trỏ tới bằng toán tử `*`:

```c
printf("%d", *p);
```

Nếu thay đổi `*p`, giá trị của biến `a` cũng thay đổi.

```c
int a = 10;
int *p = &a;
*p = *p + 3;  // a trở thành 13
```

## 3. Ví dụ về địa chỉ và giá trị con trỏ

```c
int n = 10;
int *p = &n;

printf("\nDia chi cua n: %p", &n);
printf("\nGia tri cua n: %d", n);
printf("\nDia chi cua con tro: %p", &p);
printf("\nGia tri cua con tro: %p", p);
printf("\nGia tri duoc tro toi la: %d", *p);
```

Với khai báo:

```c
int a;
int *pa = &a;
```

thì `*pa` và `a` đều biểu thị nội dung của biến `a`, còn `pa` và `&a` biểu thị địa chỉ của biến `a`.

## 4. Con trỏ và mảng một chiều

Tên mảng có thể được xem như địa chỉ của phần tử đầu tiên. Với mảng `a`, các biểu thức sau có quan hệ:

- `a` là địa chỉ phần tử đầu tiên.
- `a + i` là địa chỉ phần tử thứ `i`.
- `*(a + i)` là giá trị phần tử thứ `i`, tương đương `a[i]`.

**Ví dụ:** Nhập và xuất mảng bằng con trỏ.

```c
int a[100], n, i;

printf("Nhap so phan tu cua mang: ");
scanf("%d", &n);

for (i = 0; i < n; i++) {
    printf("a[%d] = ", i);
    scanf("%d", a + i);
}

printf("\nMang vua nhap la: ");
for (i = 0; i < n; i++)
    printf("%d ", *(a + i));
```

**Ví dụ:** Tính tổng các số dương trong mảng.

```c
int tong(int a[], int n) {
    int i, s = 0;
    for (i = 0; i < n; i++) {
        if (*(a + i) > 0)
            s += *(a + i);
    }
    return s;
}
```

## 5. Con trỏ và mảng hai chiều

Mảng hai chiều có thể được xử lý như một vùng nhớ liên tiếp. Với ma trận có `n` cột, phần tử ở dòng `d`, cột `c` có thể truy xuất bằng:

```c
*(p + d * n + c)
```

**Ví dụ:** Nhập dữ liệu ma trận qua con trỏ.

```c
int a[100][100], m, n, i;
int *p = &a[0][0];

printf("Nhap so dong, so cot: ");
scanf("%d%d", &m, &n);

for (i = 0; i < m * n; i++) {
    printf("a[%d][%d] = ", i / n, i % n);
    scanf("%d", p + i);
}
```

Xuất ma trận:

```c
for (i = 0; i < m * n; i++) {
    printf("%d ", *(p + i));
    if ((i + 1) % n == 0)
        printf("\n");
}
```

## 6. Mảng con trỏ

Mảng con trỏ là mảng mà mỗi phần tử là một con trỏ. Cấu trúc này hữu ích khi cần quản lý nhiều dãy dữ liệu có kích thước khác nhau.

```c
int *p[100];
```

Với `p[i]` trỏ tới đầu mảng thứ `i`, phần tử thứ `j` của mảng đó có thể truy xuất bằng:

```c
*((p[i]) + j)
```

## Lưu ý khi dùng con trỏ

- Con trỏ phải trỏ tới địa chỉ hợp lệ trước khi sử dụng toán tử `*`.
- Khi truyền con trỏ vào hàm, hàm có thể thay đổi giá trị của biến bên ngoài.
- Cần phân biệt địa chỉ của biến, giá trị của con trỏ và giá trị mà con trỏ trỏ tới.

## Tóm tắt

- Con trỏ lưu địa chỉ của biến.
- Toán tử `&` lấy địa chỉ, toán tử `*` truy xuất giá trị tại địa chỉ.
- Tên mảng có quan hệ chặt chẽ với con trỏ.
- Con trỏ giúp xử lý mảng, ma trận và truyền tham số linh hoạt hơn.
