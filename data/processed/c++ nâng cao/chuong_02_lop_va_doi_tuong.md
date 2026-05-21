# Chương 2: Lớp và đối tượng

## Nội dung chính
- Định nghĩa lớp và các thành phần của lớp.
- Phạm vi truy cập `private`, `protected`, `public`.
- Khai báo và sử dụng đối tượng, mảng đối tượng.
- Hàm tạo, hàm hủy và con trỏ `this`.
- Lớp bao, hàm bạn, lớp bạn.
- Khả năng nạp chồng hàm, toán tử và phương thức.

## Tổng quan
Chương này trình bày cách mô hình hóa lớp và đối tượng trong C++. Lớp được dùng để mô tả tập đối tượng cùng kiểu, còn đối tượng là một thực thể cụ thể thuộc lớp đó. Nội dung chương cũng giới thiệu các cơ chế quan trọng như constructor, destructor, `this`, friend function, friend class và overloading.

## 2.1. Định nghĩa lớp và các thành phần của lớp

### Khái niệm lớp
Lớp còn gọi là lớp đối tượng, dùng để mô tả tập các đối tượng cùng kiểu. Mỗi đối tượng thuộc một lớp cụ thể biểu diễn một thực thể cụ thể của lớp đó.

Mỗi đối tượng đặc trưng bởi hai thành phần:

- Dữ liệu: thuộc tính và trạng thái.
- Hành động: phương thức.

### Xác định thành phần của lớp
Khi xác định một lớp, cần xác định:

- Thành phần dữ liệu để lưu thông tin của đối tượng.
- Thành phần phương thức để tác động lên dữ liệu hoặc làm thay đổi dữ liệu.

Các bước phân tích:

1. Nghiên cứu tập các đối tượng của lớp cần xác định.
2. Liệt kê tập thuộc tính và phương thức.
3. Sử dụng trừu tượng hóa để chọn ra thuộc tính và phương thức cần thiết.

### Xác định thuộc tính
Thuộc tính là các tính chất đặc trưng tạo nên đối tượng.

**Ví dụ:** Lớp công dân có thể có thuộc tính:

- Họ tên.
- Ngày sinh.
- Giới tính.
- Địa chỉ.
- Số chứng minh thư.

Các phương thức có thể gồm:

- Nhập.
- Hiển thị.

### Xác định phương thức
Phương thức là các hành động tác động lên đối tượng hoặc phát sinh từ đối tượng.

**Ví dụ:** Đối tượng phân số có thể có các hành động:

- Tạo lập phân số với tử số và mẫu số xác định.
- Cộng, trừ, nhân, chia.
- Nghịch đảo, phủ định, rút gọn phân số.

Đối tượng người có thể có các hành động:

- Thiết lập thông tin cá nhân.
- Hiển thị thông tin cá nhân.
- Tìm kiếm hoặc thống kê thông tin.

## Định nghĩa lớp trong C++

Định nghĩa lớp là quá trình khai báo và xây dựng lớp bằng một ngôn ngữ lập trình cụ thể.

```cpp
class TenLop {
private:
    // Khai báo thuộc tính

public:
    // Khai báo và xây dựng phương thức
    KieuDuLieu tenPhuongThuc(/* tham số */) {
        // Nội dung phương thức
    }
};
```

Thuộc tính thông thường là các thành phần dữ liệu đơn giản như số nguyên, số thực, ký tự, chuỗi hoặc mảng. Nếu thuộc tính là kiểu dữ liệu phức tạp hoặc kiểu trừu tượng, cần định nghĩa kiểu đó trước.

### Định nghĩa phương thức ngoài lớp
Trong C++, phương thức có thể được xây dựng bên trong hoặc bên ngoài lớp. Khi xây dựng bên ngoài lớp, dùng toán tử phạm vi `::`.

```cpp
class TenLop {
public:
    void hienThi();
};

void TenLop::hienThi() {
    // Nội dung phương thức
}
```

## Sử dụng lớp

Sử dụng lớp gồm:

- Khai báo đối tượng.
- Khai báo mảng đối tượng.
- Khai báo con trỏ đối tượng.
- Gửi các thông điệp cần thiết để giải quyết bài toán.

```cpp
PhanSo A, B;
ChienBinh C1, C2;
```

## 2.2. Phạm vi `private`, `protected`, `public`

Tính che giấu thông tin trong lập trình hướng đối tượng được thực hiện nhờ phạm vi truy cập.

| Phạm vi | Ý nghĩa |
|---|---|
| `private` | Thành phần chỉ được sử dụng bên trong lớp |
| `protected` | Thành phần được dùng trong lớp và lớp con kế thừa |
| `public` | Thành phần được dùng cả bên trong và bên ngoài lớp |

Nên khai báo thành phần dữ liệu là `private` để bảo vệ dữ liệu của lớp, không cho phép hàm bên ngoài truy cập trực tiếp. Các phương thức thường được khai báo `public` để các phần khác của chương trình có thể gọi đến.

**Ví dụ diễn giải:** Thông tin riêng tư tương ứng `private`; thông tin chỉ truyền cho thế hệ kế tiếp trong gia đình tương ứng `protected`; thông tin trao đổi hằng ngày tương ứng `public`.

## 2.3. Đối tượng và mảng đối tượng

### Khai báo đối tượng
Đối tượng trong máy tính là biến đối tượng được sinh ra từ lớp.

```cpp
TenLop doiTuong;
KieuDuLieuTruuTuong bien;
```

**Ví dụ:**

```cpp
PhanSo A, B;
ChienBinh C1, C2;
```

### Truy cập thành viên lớp
Thành viên của lớp được truy cập thông qua đối tượng bằng dấu chấm.

```cpp
tenDoiTuong.tenThanhPhan;
```

Thành phần có thể là thuộc tính hoặc phương thức. Việc truy cập phụ thuộc vào phạm vi của thành phần được gọi.

### Mảng đối tượng
Kiểu dữ liệu trừu tượng có thể khai báo mảng đối tượng giống như các kiểu dữ liệu thông thường.

```cpp
TenLop danhSach[100];
danhSach[i].tenThanhPhan;
```

## 2.4. Hàm tạo và hàm hủy

### Hàm tạo
Hàm tạo (constructor) là phương thức đặc biệt dùng để khởi gán giá trị cho thuộc tính của đối tượng và có thể cấp phát bộ nhớ cho thành phần kiểu con trỏ.

Đặc điểm:

- Thường có tên trùng với tên lớp.
- Không bắt đầu bằng `void` hoặc kiểu dữ liệu trả về.
- Không trả về dữ liệu.
- Tự động được gọi khi khai báo hoặc tạo đối tượng.

Các loại hàm tạo:

- Hàm tạo không đối.
- Hàm tạo có đối.
- Hàm tạo sao chép.

```cpp
class Diem {
private:
    int x;
    int y;

public:
    Diem() {
        x = 0;
        y = 0;
    }

    Diem(int x0, int y0) {
        x = x0;
        y = y0;
    }
};
```

### Hàm hủy
Hàm hủy (destructor) là phương thức đặc biệt có nhiệm vụ hủy bỏ hoặc giải phóng bộ nhớ đã được cấp phát bởi hàm tạo.

Đặc điểm:

- Được gọi trước khi kết thúc hàm hoặc trước khi chương trình ra khỏi phạm vi của đối tượng.
- Nếu lớp không định nghĩa hàm hủy, trình dịch sẽ tự phát sinh một hàm hủy không làm gì.

```cpp
class TenLop {
public:
    ~TenLop() {
        // Giải phóng tài nguyên nếu có
    }
};
```

## 2.5. Con trỏ `this`

Mỗi lớp khi khai báo tồn tại một con trỏ `this` đặc biệt trỏ tới chính đối tượng hiện tại. Các thành phần của lớp được quản lý thông qua con trỏ này.

```cpp
class A {
private:
    int x;

public:
    void TT() {
        x = 10;        // Tương đương this->x = 10;
        this->x = 10;
    }
};
```

## 2.6. Lớp bao

Lớp bao là lớp có thành viên thuộc tính là đối tượng của lớp khác.

```cpp
class A;
class B;

class C {
private:
    A a;
    B b, c;
    float d;
};
```

Trong ví dụ trên, `C` là lớp bao của `A` và `B`; `A`, `B` là các lớp thành viên của `C`. Khi xây dựng hàm tạo cho lớp bao, cần sử dụng hàm tạo của lớp thành viên để khởi gán giá trị cho các đối tượng thành viên.

## 2.7. Hàm bạn

Hàm bạn (friend function) của một lớp không phải là phương thức của lớp, nhưng có thể truy cập các thành phần riêng của lớp. Một hàm có thể là bạn của nhiều lớp.

Hàm bạn phải được khai báo bên trong lớp bằng từ khóa `friend` và xây dựng bên ngoài lớp.

```cpp
class A {
private:
    int x;

public:
    friend void hienThi(A a);
};

void hienThi(A a) {
    // Có thể truy cập a.x
}
```

## 2.8. Lớp bạn

Nếu lớp `A` được khai báo là bạn của lớp `B`, thì tất cả phương thức của lớp `A` có thể truy cập các thành phần riêng của lớp `B`.

Quan hệ bạn không nhất thiết hai chiều: `A` là bạn của `B` không có nghĩa `B` là bạn của `A`. Một lớp có thể là bạn của nhiều lớp.

```cpp
class B {
    friend class A;
private:
    int data;
};
```

## 2.9. Khả năng nạp chồng

### Nạp chồng hàm
Nạp chồng hàm là khả năng có các hàm trùng tên nhưng khác nhau ít nhất một trong các tiêu chí:

- Kiểu dữ liệu trả về.
- Kiểu dữ liệu của tham số truyền vào.
- Số lượng tham số truyền vào.

**Ví dụ:**

```cpp
int triTuyetDoi(int a);
long triTuyetDoi(long a);
double triTuyetDoi(double a);

void hoanVi(int &a, int &b);
void hoanVi(char &a, char &b);
void hoanVi(float &a, float &b);
```

### Nạp chồng toán tử
Toán tử cũng có khả năng nạp chồng. Ví dụ phép cộng có thể dùng cho số nguyên, số thực hoặc đối tượng do người dùng định nghĩa.

Slide nêu ví dụ với phân số:

```cpp
PhanSo operator+(const PhanSo &a, const PhanSo &b);
```

Toán tử có thể được xây dựng như hàm thông thường, hàm bạn hoặc phương thức của lớp.

### Một số toán tử đặc biệt
- Toán tử gán `=`.
- Toán tử tăng `++` và giảm `--`.
- Toán tử nhập `>>` và xuất `<<`.

Toán tử nhập/xuất nằm trong thư viện luồng, khi nạp chồng cho lớp thường được xây dựng theo nguyên tắc hàm bạn.

## Bài tập trong chương

### Bài 1: Lớp `Time`
Xây dựng lớp `Time` để lưu giờ, phút, giây:

- Xây dựng hàm tạo để khởi tạo giá trị ban đầu.
- Xây dựng phương thức hiển thị dữ liệu thời gian.
- Xây dựng phép cộng giữa thời gian và một số nguyên là số giây.
- Xây dựng phép trừ giữa dữ liệu thời gian.
- Viết hàm chính để khởi tạo đối tượng `Time` và gọi các phương thức, toán tử đã xây dựng.

### Bài 2: Lớp `Nhanvien`
Xây dựng lớp `Nhanvien` gồm họ tên, ngày sinh, giới tính, mã nhân viên, số chứng minh thư, lương cơ bản, phụ cấp.

Yêu cầu:

- Xây dựng phương thức nhập và xuất thông tin.
- Xây dựng hàm so sánh tuổi của hai nhân viên.
- Xây dựng phương thức tính lương theo công thức: `lương = lương cơ bản * 3 + phụ cấp`.
- Viết hàm chính khai báo danh sách ít nhất 5 nhân viên, nhập thông tin và hiển thị danh sách đã sắp xếp theo tuổi giảm dần, có cả lương được lĩnh.

## Tóm tắt chương
- Lớp mô tả tập đối tượng cùng kiểu; đối tượng là thực thể cụ thể của lớp.
- Thành phần của lớp gồm thuộc tính và phương thức.
- `private`, `protected`, `public` giúp che giấu và kiểm soát truy cập dữ liệu.
- Constructor khởi tạo đối tượng, destructor giải phóng tài nguyên.
- `this`, lớp bao, hàm bạn, lớp bạn và nạp chồng là các cơ chế quan trọng khi lập trình C++ hướng đối tượng.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Class | Lớp, mô tả tập đối tượng cùng kiểu |
| Object | Đối tượng, thực thể cụ thể của lớp |
| Attribute | Thuộc tính, dữ liệu mô tả trạng thái |
| Method | Phương thức, hành động của đối tượng |
| Constructor | Hàm tạo dùng để khởi tạo đối tượng |
| Destructor | Hàm hủy dùng để hủy đối tượng hoặc giải phóng tài nguyên |
| `this` | Con trỏ trỏ đến đối tượng hiện tại |
| Friend function | Hàm bạn có quyền truy cập thành phần riêng của lớp |
| Friend class | Lớp bạn có phương thức truy cập thành phần riêng của lớp khác |
| Overloading | Nạp chồng hàm, toán tử hoặc phương thức |

## Câu hỏi ôn tập
1. Lớp và đối tượng khác nhau như thế nào?
2. Khi phân tích một lớp cần xác định những thành phần nào?
3. Vì sao thuộc tính thường được khai báo `private`?
4. Phân biệt `private`, `protected` và `public`.
5. Hàm tạo có đặc điểm gì?
6. Hàm hủy được gọi khi nào?
7. Con trỏ `this` dùng để làm gì?
8. Lớp bao là gì?
9. Hàm bạn và lớp bạn có điểm gì đặc biệt?
10. Nạp chồng hàm và nạp chồng toán tử khác nhau như thế nào?
