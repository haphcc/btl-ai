# Kiểu dữ liệu mảng

## Nội dung chính
- Khái niệm mảng một chiều.
- Khai báo, truy xuất, nhập và xuất mảng.
- Một số bài toán cơ bản trên mảng một chiều.
- Mảng nhiều chiều và ma trận.
- Truyền mảng cho hàm.

## Tổng quan
Mảng là kiểu dữ liệu dùng để lưu nhiều phần tử cùng kiểu dưới một tên chung. Thay vì khai báo nhiều biến rời rạc, mảng giúp quản lý dãy dữ liệu theo chỉ số.

## 1. Mảng một chiều

### Khái niệm

Mảng một chiều là tập hợp các phần tử cùng kiểu, được lưu liên tiếp và truy xuất thông qua chỉ số.

Ví dụ, để lưu 100 số nguyên, thay vì khai báo 100 biến, có thể khai báo một mảng:

```c
int a[100];
```

### Khai báo mảng

Cú pháp:

```c
<kieu_du_lieu> <ten_mang>[<so_phan_tu>];
```

Ví dụ:

```c
int a[100];
float b[50];
char c[20];
```

### Truy xuất phần tử

Phần tử thứ `i` của mảng `a` được truy xuất bằng:

```c
a[i]
```

Trong C, chỉ số mảng thường bắt đầu từ `0`.

## 2. Nhập và xuất mảng một chiều

**Ví dụ:** Nhập mảng `n` số nguyên.

```c
int a[100], n, i;

printf("Nhap so luong phan tu n: ");
scanf("%d", &n);

for (i = 0; i < n; i++) {
    printf("Nhap phan tu thu %d: ", i);
    scanf("%d", &a[i]);
}
```

**Ví dụ:** Xuất mảng ra màn hình.

```c
printf("Noi dung cua mang la: ");
for (i = 0; i < n; i++)
    printf("%d ", a[i]);
printf("\n");
```

## 3. Một số bài toán cơ bản trên mảng

### Tìm kiếm tuyến tính

Tìm vị trí đầu tiên của giá trị `x` trong mảng. Nếu tìm thấy thì trả về chỉ số, nếu không thì trả về `-1`.

```c
int timkiem(int a[], int n, int x) {
    int i;
    for (i = 0; i < n; i++) {
        if (a[i] == x)
            return i;
    }
    return -1;
}
```

### Sắp xếp tăng dần

Một cách sắp xếp là so sánh từng cặp phần tử và đổi chỗ khi phần tử trước lớn hơn phần tử sau.

```c
for (i = 0; i < n - 1; i++) {
    for (j = i + 1; j < n; j++) {
        if (a[i] > a[j]) {
            int temp = a[i];
            a[i] = a[j];
            a[j] = temp;
        }
    }
}
```

### Truyền mảng cho hàm

Khi truyền mảng cho hàm, hàm có thể thay đổi nội dung các phần tử của mảng.

```c
void nhapMang(int a[], int n) {
    int i;
    for (i = 0; i < n; i++) {
        printf("a[%d] = ", i);
        scanf("%d", &a[i]);
    }
}
```

## 4. Mảng nhiều chiều

### Khái niệm

Mảng nhiều chiều dùng để biểu diễn dữ liệu có dạng bảng. Mảng hai chiều thường được dùng để biểu diễn ma trận.

Khai báo ma trận số nguyên:

```c
int a[100][100];
```

### Nhập ma trận

```c
int a[100][100], m, n, i, j;

printf("Nhap so dong, so cot cua ma tran: ");
scanf("%d%d", &m, &n);

for (i = 0; i < m; i++) {
    for (j = 0; j < n; j++) {
        printf("Nhap a[%d][%d]: ", i, j);
        scanf("%d", &a[i][j]);
    }
}
```

### Xuất ma trận

```c
for (i = 0; i < m; i++) {
    for (j = 0; j < n; j++)
        printf("%d  ", a[i][j]);
    printf("\n");
}
```

## 5. Một số bài toán với ma trận

### Cộng hai ma trận

Hai ma trận cùng kích thước `m x n` có thể cộng theo từng phần tử:

```c
for (i = 0; i < m; i++) {
    for (j = 0; j < n; j++)
        c[i][j] = a[i][j] + b[i][j];
}
```

### Nhân hai ma trận

Bài tập yêu cầu nhân ma trận `a` kích thước `m x k` với ma trận `b` kích thước `k x n`.

### Ma trận vuông

Với ma trận vuông cấp `n`, các bài toán thường gặp gồm:

- Tính tổng đường chéo chính.
- Xử lý phần tam giác trên hoặc tam giác dưới.
- Tìm điểm yên ngựa nếu có.

## Bài tập thực hành

- Nhập và xuất mảng một chiều.
- Tìm kiếm phần tử trong mảng.
- Sắp xếp mảng tăng dần hoặc giảm dần.
- Sắp xếp số dương, số âm và số không theo yêu cầu.
- Nhập và xuất ma trận.
- Cộng, nhân hai ma trận.
- Xử lý ma trận vuông: đường chéo, tam giác trên, tam giác dưới.

## Tóm tắt

- Mảng lưu nhiều phần tử cùng kiểu dưới một tên chung.
- Mảng một chiều biểu diễn dãy, mảng hai chiều biểu diễn bảng hoặc ma trận.
- Khi truyền mảng vào hàm, nội dung mảng có thể bị thay đổi.
