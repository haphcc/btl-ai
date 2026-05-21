# Chương 3.1: Danh sách liên kết

## Nội dung chính
- Hạn chế của mảng một chiều và biến tĩnh.
- Khái niệm biến động và biến con trỏ.
- Các thao tác cấp phát, giải phóng vùng nhớ động.
- Khái niệm danh sách liên kết.
- Liên kết ngầm bằng mảng và liên kết tường minh bằng con trỏ.
- Các loại danh sách liên kết: đơn, kép, vòng.

## Tổng quan
Danh sách liên kết được dùng để khắc phục hạn chế của mảng tĩnh: kích thước cố định và thao tác chèn/xóa không thuận tiện. Danh sách liên kết lưu các phần tử ở vị trí bất kỳ trong bộ nhớ và liên kết chúng bằng con trỏ.

## 3.1. Đặt vấn đề

Mảng một chiều có các đặc điểm:

- Kích thước cố định.
- Các phần tử được đánh chỉ số từ `0` đến `n - 1`.
- Truy cập ngẫu nhiên nhanh.
- Chèn một phần tử vào giữa mảng khó vì phải dịch chuyển nhiều phần tử.

### Biến tĩnh
Biến tĩnh:

- Được khai báo tường minh và có tên gọi.
- Tồn tại trong phạm vi khai báo.
- Được cấp phát trong stack.
- Kích thước không đổi nên có thể không tận dụng hiệu quả bộ nhớ.

**Ví dụ:**

```cpp
int x, y;
char c;
float f[5];
```

### Hạn chế của biến tĩnh
Ví dụ tổ chức danh sách lớp học bằng mảng tĩnh:

```cpp
typedef struct {
    char ten[20];
    int maso;
} Hocvien;

Hocvien danhsach[50];
```

Nếu số học viên nhỏ hơn 50 thì lãng phí bộ nhớ. Nếu số học viên lớn hơn 50 thì thiếu chỗ.

## Biến động

Biến động:

- Không được khai báo tường minh bằng tên cố định.
- Được xin cấp phát khi cần và giải phóng khi dùng xong.
- Được cấp phát trong heap.
- Linh động về kích thước.

Vấn đề đặt ra: biến động không có tên gọi tường minh, nên cần con trỏ để thao tác với nó.

## 3.2. Biến con trỏ

Kiểu con trỏ dùng để lưu địa chỉ của một đối tượng dữ liệu khác. Biến con trỏ kiểu `T*` có giá trị là địa chỉ của một vùng nhớ ứng với biến kiểu `T`, hoặc là `NULL`.

**Ví dụ khai báo trong C/C++:**

```cpp
typedef int* intpointer;
intpointer p;
```

Bản thân biến con trỏ là biến không động, nhưng nó có thể lưu địa chỉ của biến động. Nhờ đó, ta truy xuất biến động thông qua biến con trỏ.

### Cấp phát và giải phóng
Tạo biến động và cho con trỏ `p` chỉ đến nó:

```cpp
int *p;
p = new int;
*p = 5;
```

Một số hàm/thao tác cấp phát:

- `malloc(size)`.
- `calloc(n, size)`.
- `new`.

Giải phóng:

- `free(p)` hủy vùng nhớ cấp phát bởi `malloc` hoặc `calloc`.
- `delete p` hủy vùng nhớ cấp phát bởi `new`.

## 3.3. Danh sách liên kết

Danh sách là tập các phần tử cùng kiểu và là kiểu dữ liệu tuyến tính:

- Mỗi phần tử có nhiều nhất một phần tử đứng trước.
- Mỗi phần tử có nhiều nhất một phần tử đứng sau.

Ví dụ thực tế:

- Danh sách học sinh.
- Danh mục sách trong thư viện.
- Danh bạ điện thoại.
- Danh sách nhân viên trong công ty.

## Các hình thức tổ chức danh sách

Cần xác định:

- Cấu trúc dữ liệu cho mỗi phần tử.
- Cách thể hiện liên kết giữa các phần tử.

Hai hình thức cơ bản:

| Hình thức | Cách biểu diễn |
|---|---|
| Liên kết ngầm | Mảng |
| Liên kết tường minh | Danh sách liên kết |

### Liên kết ngầm bằng mảng
Trong mảng, phần tử `xi` và `x(i+1)` kề nhau vì chúng nằm liên tiếp trong bộ nhớ.

Công thức xác định địa chỉ phần tử thứ `i`:

```text
address(i) = address(1) + (i - 1) * sizeof(T)
```

Ưu điểm:

- Truy xuất trực tiếp, nhanh chóng.

Nhược điểm:

- Sử dụng bộ nhớ kém hiệu quả.
- Kích thước cố định.
- Thêm và loại bỏ phần tử không hiệu quả.

### Liên kết tường minh bằng danh sách liên kết
Mỗi phần tử trong danh sách liên kết gồm:

- Thông tin bản thân.
- Địa chỉ của phần tử kế tiếp trong danh sách.

Mỗi phần tử là một biến động.

Ưu điểm:

- Sử dụng bộ nhớ hiệu quả hơn.
- Linh động về số lượng phần tử.

## Các loại danh sách liên kết

| Loại | Đặc điểm |
|---|---|
| Danh sách liên kết đơn | Mỗi phần tử liên kết với phần tử đứng sau |
| Danh sách liên kết kép | Mỗi phần tử liên kết với phần tử đứng trước và đứng sau |
| Danh sách liên kết vòng | Phần tử cuối liên kết với phần tử đầu danh sách |

## Tóm tắt chương
- Mảng tĩnh có kích thước cố định và khó chèn/xóa.
- Biến động được cấp phát trong heap, cần con trỏ để truy xuất.
- Danh sách liên kết dùng con trỏ để nối các phần tử nằm rời rạc trong bộ nhớ.
- Có ba dạng danh sách liên kết chính: đơn, kép và vòng.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Biến tĩnh | Biến có tên, cấp phát trong stack, kích thước cố định |
| Biến động | Vùng nhớ được cấp phát khi cần trong heap |
| Con trỏ | Biến lưu địa chỉ của vùng nhớ khác |
| Heap | Vùng nhớ cấp phát động |
| Danh sách liên kết | Danh sách có phần tử liên kết bằng con trỏ |
| Node | Nút, phần tử của danh sách liên kết |
| Danh sách liên kết đơn | Mỗi nút trỏ đến nút kế tiếp |
| Danh sách liên kết kép | Mỗi nút trỏ đến nút trước và nút sau |

## Câu hỏi ôn tập
1. Mảng một chiều có hạn chế gì khi tổ chức danh sách?
2. Biến tĩnh và biến động khác nhau như thế nào?
3. Con trỏ dùng để làm gì?
4. Phân biệt `new` và `delete`.
5. Danh sách liên kết biểu diễn liên kết giữa các phần tử như thế nào?
6. Liên kết ngầm và liên kết tường minh khác nhau ra sao?
7. Nêu các loại danh sách liên kết cơ bản.
