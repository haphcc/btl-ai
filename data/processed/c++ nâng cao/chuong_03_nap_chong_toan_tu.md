# Chương 3: Nạp chồng toán tử

## Nội dung chính
- Khái niệm và nguyên tắc nạp chồng toán tử.
- Các giới hạn khi nạp chồng toán tử trong C++.
- Nạp chồng toán tử hai ngôi và một ngôi.
- Nạp chồng toán tử đặc biệt `[]`, `()`, toán tử chuyển đổi kiểu, `new`, `delete`.
- Nạp chồng toán tử chèn dòng `<<` và trích dòng `>>`.
- Bài tập tổng hợp với lớp `Vector2D`.

## Tổng quan
Nạp chồng toán tử (operator overloading) cho phép định nghĩa lại cách hoạt động của một toán tử C++ khi áp dụng cho đối tượng của lớp do người dùng định nghĩa. Nhờ cơ chế này, các đối tượng có thể được sử dụng tự nhiên hơn với các toán tử quen thuộc như `+`, `-`, `==`, `<<`, `>>`.

## 3.1. Nguyên tắc nạp chồng toán tử

### Khái niệm
Nạp chồng toán tử cho phép định nghĩa lại cách hoạt động của toán tử C++ đối với đối tượng thuộc `class` hoặc `struct` do người dùng định nghĩa.

**Ví dụ vấn đề:** Nếu có lớp `A` và thử cộng hai đối tượng bằng toán tử `+`, C++ không tự biết phép `+` giữa hai đối tượng `A` phải thực hiện như thế nào. Người lập trình cần định nghĩa phép cộng đó.

### Nguyên tắc cơ bản
- Chỉ nạp chồng được toán tử có sẵn trong C++.
- Không thể tạo toán tử mới.
- Ít nhất một toán hạng phải là kiểu do người dùng định nghĩa, như `class` hoặc `struct`.
- Không thay đổi độ ưu tiên (precedence) và tính kết hợp (associativity) của toán tử.
- Không thay đổi số lượng toán hạng của toán tử.
- Có thể định nghĩa dưới dạng hàm thành viên hoặc hàm bạn.
- Cần giữ ý nghĩa ngữ pháp hợp lý để tránh gây nhầm lẫn.

## 3.2. Các giới hạn

Một số toán tử không thể nạp chồng:

| Toán tử | Ý nghĩa |
|---|---|
| `::` | Phân giải phạm vi |
| `.` | Truy cập thành viên |
| `.*` | Truy cập thành viên qua con trỏ |
| `sizeof` | Lấy kích thước |
| `typeid` | Lấy thông tin kiểu |
| `?:` | Toán tử điều kiện ba ngôi |

Các toán tử này được xử lý ở mức ngôn ngữ hoặc tại thời điểm biên dịch, nên C++ không cho phép người lập trình thay đổi.

## 3.3. Nạp chồng toán tử hai ngôi

Toán tử hai ngôi (binary operator) làm việc với hai toán hạng.

Các toán tử phổ biến:

- `+`, `-`, `*`, `/`, `%`.
- `==`, `!=`, `<`, `<=`, `>`, `>=`.
- `&&`, `||`.

### Dạng hàm thành viên
Khi viết dưới dạng phương thức của lớp, toán hạng bên trái thường là đối tượng hiện tại.

```cpp
class A {
public:
    A operator+(const A &other);
};
```

### Dạng hàm bạn
Khi viết dưới dạng hàm bạn, cần khai báo với từ khóa `friend` bên trong lớp.

```cpp
class A {
public:
    friend A operator+(const A &left, const A &right);
};
```

## 3.4. Nạp chồng toán tử một ngôi

Toán tử một ngôi (unary operator) tác động lên một toán hạng duy nhất.

Ví dụ các toán tử một ngôi thường gặp:

- Đổi dấu `-`.
- Tăng `++`.
- Giảm `--`.

### Dạng hàm thành viên

```cpp
class A {
public:
    A operator-();
};
```

### Dạng hàm bạn

```cpp
class A {
public:
    friend A operator-(const A &value);
};
```

## 3.5. Nạp chồng toán tử đặc biệt `[]` và `()`

### Toán tử `[]`
Toán tử `[]` cho phép đối tượng được truy cập như mảng.

```cpp
double &operator[](int index);
const double &operator[](int index) const;
```

### Toán tử `()`
Toán tử `()` cho phép đối tượng hoạt động như một hàm, còn gọi là functor.

```cpp
double operator()(const Vector2D &other) const;
```

## 3.6. Toán tử chuyển đổi kiểu

Toán tử chuyển đổi kiểu cho phép đối tượng được chuyển đổi sang kiểu dữ liệu khác. Slide nêu rằng cơ chế này hỗ trợ cả chuyển đổi tường minh và ngầm định.

```cpp
operator double() const;
explicit operator std::string() const;
```

## 3.7. Toán tử `new` và `delete`

Nạp chồng `new` và `delete` giúp tùy biến cách cấp phát và giải phóng bộ nhớ khi tạo hoặc xóa đối tượng.

```cpp
void* operator new(size_t size);
void operator delete(void* ptr);
```

## 3.8. Toán tử chèn dòng và trích dòng

Toán tử `<<` và `>>` cho phép định nghĩa cách xuất và nhập dữ liệu của đối tượng qua luồng.

```cpp
friend ostream &operator<<(ostream &out, const A &obj);
friend istream &operator>>(istream &in, A &obj);
```

Vì toán tử nhập/xuất liên quan đến luồng, khi nạp chồng cho lớp thường khai báo chúng là hàm bạn.

## 3.9. Bài tập tổng hợp

### Bài tập lớp `Vector2D`
Viết lớp `Vector2D` biểu diễn véc-tơ hai chiều `(x, y)` và nạp chồng các toán tử sau:

1. Toán tử hai ngôi: `+`, `-`, `==`, `!=`.
2. So sánh bằng dùng sai số `epsilon = 1e-9`.
3. Toán tử một ngôi: `-` để đổi dấu, `++` dạng prefix và postfix.
4. Toán tử đặc biệt:
   - `operator[](int)` dạng non-const và const.
   - Chỉ số `0` ứng với `x`, chỉ số `1` ứng với `y`; chỉ số sai ném `std::out_of_range`.
   - `operator()(const Vector2D&) const` tính dot product.
   - `operator()(double, double)` đặt lại `(x, y)`.
   - `operator double() const` trả về độ dài.
   - `explicit operator std::string() const` trả về chuỗi dạng `"(x,y)"`.
5. I/O:
   - `operator<<` in dạng `(x, y)` với 2 chữ số thập phân.
   - `operator>>` đọc 2 số thực; nhập lỗi ném `std::invalid_argument`.
6. Quản lý bộ nhớ tùy biến:
   - `operator new/delete`.
   - `operator new[]/delete[]`.
   - In log khi cấp phát/giải phóng.
   - Kiểm tra null và ném `std::bad_alloc`.
7. Viết `main()` minh họa đầy đủ các toán tử trên.

Yêu cầu thêm:

- Dùng const-correctness.
- Tham số truyền bằng `const&` khi phù hợp.
- Giải thích ngắn vì sao `explicit` cần thiết.

## Tóm tắt chương
- Nạp chồng toán tử giúp đối tượng do người dùng định nghĩa sử dụng được các toán tử quen thuộc.
- Không thể tạo toán tử mới hoặc thay đổi độ ưu tiên, tính kết hợp, số lượng toán hạng.
- Toán tử có thể nạp chồng bằng hàm thành viên hoặc hàm bạn.
- Các toán tử đặc biệt như `[]`, `()`, `<<`, `>>`, `new`, `delete` có ứng dụng riêng trong thiết kế lớp.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Operator overloading | Nạp chồng toán tử |
| Binary operator | Toán tử hai ngôi |
| Unary operator | Toán tử một ngôi |
| Member function | Hàm thành viên của lớp |
| Friend function | Hàm bạn có thể truy cập thành phần riêng |
| Functor | Đối tượng hoạt động như hàm thông qua `operator()` |
| Conversion operator | Toán tử chuyển đổi kiểu |
| Stream insertion | Toán tử chèn dòng `<<` |
| Stream extraction | Toán tử trích dòng `>>` |

## Câu hỏi ôn tập
1. Nạp chồng toán tử là gì?
2. Vì sao cần nạp chồng toán tử cho lớp do người dùng định nghĩa?
3. Các nguyên tắc cơ bản khi nạp chồng toán tử là gì?
4. Những toán tử nào không thể nạp chồng?
5. Phân biệt nạp chồng toán tử bằng hàm thành viên và hàm bạn.
6. Toán tử `[]` và `()` được dùng cho mục đích gì?
7. Vì sao toán tử `<<` và `>>` thường được khai báo là hàm bạn?
8. Bài tập `Vector2D` yêu cầu nạp chồng những nhóm toán tử nào?
