# Kiểu dữ liệu cấu trúc

## Nội dung chính
- Khái niệm kiểu cấu trúc `struct`.
- Khai báo cấu trúc trực tiếp và gián tiếp.
- Truy cập, gán và xử lý dữ liệu cấu trúc.
- Con trỏ cấu trúc và truyền cấu trúc cho hàm.
- Kiểu `union`.
- Bài tập thực hành với phân số, điểm, tam giác và quản lý học sinh.

## Tổng quan
Kiểu cấu trúc cho phép gom nhiều dữ liệu có kiểu khác nhau vào cùng một đối tượng. Đây là cách xây dựng kiểu dữ liệu mới phù hợp với các đối tượng thực tế như sinh viên, ngày tháng, điểm, phân số hoặc số phức.

## 1. Khái niệm kiểu cấu trúc

`struct` là kiểu dữ liệu gồm nhiều thành phần có thể khác kiểu nhau. Mỗi thành phần được gọi là một trường.

So với mảng:

| Mảng | Cấu trúc |
|---|---|
| Các phần tử cùng kiểu | Các trường có thể khác kiểu |
| Truy xuất bằng chỉ số | Truy xuất bằng tên trường |
| Phù hợp với dãy dữ liệu đồng nhất | Phù hợp với đối tượng gồm nhiều thuộc tính |

## 2. Khai báo cấu trúc

### Khai báo trực tiếp

```c
struct NgayThang {
    int Ngay;
    int Thang;
    int Nam;
};
```

### Khai báo gián tiếp bằng `typedef`

```c
typedef struct {
    unsigned char Ngay;
    unsigned char Thang;
    unsigned int Nam;
} NgayThang;
```

### Cấu trúc lồng nhau

Ví dụ kiểu `SinhVien` có trường ngày sinh thuộc kiểu `NgayThang`.

```c
typedef struct {
    char Masv[10];
    char Hoten[40];
    NgayThang NgaySinh;
    int Gioitinh;
    char Diachi[50];
} SinhVien;
```

## 3. Khai báo biến cấu trúc

Khai báo biến cấu trúc tương tự khai báo biến kiểu dữ liệu chuẩn.

```c
struct Diem {
    float x;
    float y;
} A, B;
```

Hoặc với kiểu đã định nghĩa:

```c
SinhVien SV1, SV2;
```

## 4. Các thao tác với cấu trúc

### Khởi tạo cấu trúc

```c
struct NgayThang ngaysinh = {1, 8, 1991};
```

### Truy cập trường của cấu trúc

Dùng toán tử chấm `.` để truy cập trường:

```c
printf("x = %f, y = %f", A.x, A.y);
```

### Gán dữ liệu cấu trúc

Có thể gán toàn bộ biến cấu trúc hoặc gán từng trường.

```c
struct Diem {
    int x, y;
} diem1 = {2912, 1706}, diem2;

diem2 = diem1;
diem2.x = diem1.x;
diem2.y = diem1.y * 2;
```

Không thực hiện trực tiếp các phép nhập xuất, quan hệ, số học hoặc logic trên toàn bộ biến cấu trúc; cần xử lý từng trường hoặc viết hàm riêng.

## 5. Ví dụ nhập và in thông tin sinh viên

```c
typedef struct {
    unsigned char Ngay;
    unsigned char Thang;
    unsigned int Nam;
} NgayThang;

typedef struct {
    char MSSV[10];
    char HoTen[40];
    NgayThang NgaySinh;
    int Gioitinh;
    char DiaChi[40];
} SinhVien;

void InSV(SinhVien s) {
    printf("MSSV: | Ho va ten | Ngay Sinh | Dia chi\n");
    printf("%s | %s | %d-%d-%d | %s\n",
           s.MSSV, s.HoTen,
           s.NgaySinh.Ngay, s.NgaySinh.Thang, s.NgaySinh.Nam,
           s.DiaChi);
}
```

## 6. Ví dụ tính tổng hai số phức

```c
typedef struct {
    float Thuc;
    float Ao;
} SoPhuc;

void InSoPhuc(SoPhuc p) {
    printf("%.2f + i%.2f\n", p.Thuc, p.Ao);
}

SoPhuc cong(SoPhuc u, SoPhuc v) {
    SoPhuc tong;
    tong.Thuc = u.Thuc + v.Thuc;
    tong.Ao = u.Ao + v.Ao;
    return tong;
}
```

## 7. Con trỏ cấu trúc

C cho phép dùng con trỏ trỏ tới cấu trúc.

```c
struct NgayThang *p;
struct NgayThang date;
p = &date;
```

Khi truy cập trường thông qua con trỏ, dùng toán tử `->`.

```c
printf("%d-%d-%d", p->Ngay, p->Thang, p->Nam);
```

Biểu thức `p->Ngay` tương đương:

```c
(*p).Ngay
```

## 8. Truyền tham số cấu trúc cho hàm

Tham số của hàm có thể là:

- Từng trường của cấu trúc.
- Biến cấu trúc.
- Con trỏ cấu trúc.
- Mảng cấu trúc.

Hàm có thể trả về giá trị cấu trúc hoặc con trỏ cấu trúc.

## 9. Union

`union` được khai báo và sử dụng gần giống `struct`, nhưng các thành phần của `union` dùng chung địa chỉ đầu và nằm chồng lên nhau trong bộ nhớ.

```c
union MYUNION {
    char c;
    int n;
};
```

So với `struct`, các trường của `union` không tồn tại độc lập đồng thời ở các vùng nhớ khác nhau.

## Bài tập thực hành

- Khai báo kiểu dữ liệu phân số, nhập xuất, rút gọn, tính tổng, hiệu, tích, thương hai phân số.
- Kiểm tra phân số tối giản, quy đồng và so sánh hai phân số.
- Xử lý mảng phân số: đếm phân số âm, dương; tìm phân số lớn nhất, nhỏ nhất; sắp xếp.
- Khai báo kiểu điểm trong mặt phẳng Oxy, tính khoảng cách và điểm đối xứng.
- Khai báo kiểu tam giác, tính chu vi và diện tích.
- Quản lý học sinh gồm họ tên, năm sinh, điểm toán, lý, hóa, tổng điểm.
- Sắp xếp danh sách học sinh theo tổng điểm giảm dần và tìm kiếm theo họ tên.

## Tóm tắt

- `struct` dùng để gom nhiều trường dữ liệu có thể khác kiểu.
- Truy cập trường bằng toán tử `.` hoặc `->` nếu dùng con trỏ.
- Có thể truyền cấu trúc vào hàm, trả về cấu trúc từ hàm và xây dựng mảng cấu trúc.
- `union` khác `struct` ở chỗ các trường dùng chung vùng nhớ.
