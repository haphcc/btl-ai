# Chương 2.2: Tìm kiếm và sắp xếp

## Nội dung chính
- Bài toán tìm kiếm trên danh sách lưu bằng mảng.
- Tìm kiếm tuyến tính và cải tiến bằng phần tử lính canh.
- Tìm kiếm nhị phân trên mảng đã có thứ tự.
- Bài toán sắp xếp và khái niệm nghịch thế.
- Các thuật toán sắp xếp: Interchange Sort, Selection Sort, Bubble Sort, Shaker Sort, Insertion Sort, Binary Insertion Sort, Shell Sort, Heap Sort, Quick Sort, Merge Sort, Radix Sort.
- Cài đặt một số thuật toán tìm kiếm và sắp xếp bằng C/C++.

## Tổng quan
Tìm kiếm và sắp xếp là hai nhóm thuật toán cơ bản trên danh sách. Slide trình bày tìm kiếm tuyến tính, tìm kiếm nhị phân và một số thuật toán sắp xếp trực tiếp, trong đó danh sách được biểu diễn bằng mảng một chiều.

## Bài toán tìm kiếm

Cho danh sách có `n` phần tử `a0, a1, ..., a(n-1)`. Để đơn giản, dùng mảng một chiều `a` để lưu danh sách trong bộ nhớ chính. Bài toán là tìm phần tử có khóa bằng `x` trong mảng.

## Tìm kiếm tuyến tính

### Ý tưởng
So sánh `x` lần lượt với phần tử thứ nhất, thứ hai, ... của mảng cho đến khi gặp khóa cần tìm hoặc đã xét hết mảng.

### Các bước
1. Khởi gán `i = 0`.
2. So sánh `a[i]` với `x`:
   - Nếu `a[i] == x`, tìm thấy và dừng.
   - Nếu `a[i] != x`, sang bước 3.
3. Tăng `i = i + 1`.
   - Nếu `i == n`, hết mảng và dừng.
   - Ngược lại quay lại bước 2.

### Cài đặt

```cpp
int LinearSearch(int a[], int n, int x) {
    int i = 0;
    while ((i < n) && (a[i] != x)) {
        i++;
    }
    if (i == n) {
        return 0; // Tìm không thấy
    }
    return 1;     // Tìm thấy
}
```

### Cải tiến bằng lính canh
Trong trường hợp xấu nhất, thuật toán tuyến tính có thể cần nhiều phép so sánh. Để giảm phép so sánh trong vòng lặp, thêm phần tử `x` vào cuối dãy làm lính canh.

```cpp
int LinearSearchSentinel(int a[], int n, int x) {
    int i = 0;
    a[n] = x; // a[n] là phần tử lính canh
    while (a[i] != x) {
        i++;
    }
    if (i == n) {
        return 0;
    }
    return 1;
}
```

### Đánh giá
| Trường hợp | Số phép so sánh |
|---|---|
| Tốt nhất | 1 |
| Trung bình | `(n + 1) / 2` |
| Xấu nhất | `n` |

Độ phức tạp: `O(n)`.

## Tìm kiếm nhị phân

### Điều kiện áp dụng
Tìm kiếm nhị phân áp dụng trên mảng đã có thứ tự.

### Ý tưởng
Tại mỗi bước, so sánh `x` với phần tử đứng giữa dãy tìm kiếm hiện hành:

- Nếu `x == a[mid]`, tìm thấy.
- Nếu `x > a[mid]`, chỉ cần tìm trong nửa phải.
- Nếu `x < a[mid]`, chỉ cần tìm trong nửa trái.

### Các bước
1. `left = 0`, `right = n - 1`.
2. Tính `mid = (left + right) / 2`.
3. So sánh `a[mid]` với `x`:
   - `a[mid] == x`: tìm thấy.
   - `a[mid] > x`: `right = mid - 1`.
   - `a[mid] < x`: `left = mid + 1`.
4. Nếu `left <= right`, lặp lại bước 2; ngược lại dừng.

### Cài đặt

```cpp
int BinarySearch(int a[], int n, int x) {
    int left = 0;
    int right = n - 1;
    int mid;

    do {
        mid = (left + right) / 2;
        if (a[mid] == x) {
            return 1;
        } else if (a[mid] < x) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    } while (left <= right);

    return 0;
}
```

## Bài toán sắp xếp

Sắp xếp là quá trình xử lý các phần tử trong danh sách để đặt chúng theo một thứ tự thỏa mãn tiêu chuẩn nào đó.

**Ví dụ:**

- Sắp xếp danh sách lớp học tăng theo điểm trung bình.
- Sắp xếp danh sách sinh viên tăng theo tên.

### Nghịch thế
Với dãy `a0, a1, ..., a(n-1)`, nếu `i < j` và `a[i] > a[j]`, thì cặp `(a[i], a[j])` là một nghịch thế.

Để sắp xếp dãy tăng, cần triệt tiêu các nghịch thế.

Các tiêu chí đánh giá:

- `Css`: số phép so sánh.
- `CHV`: số phép hoán vị.

## Các thuật toán sắp xếp

Slide liệt kê các thuật toán:

1. Đổi chỗ trực tiếp - Interchange Sort.
2. Chọn trực tiếp - Selection Sort.
3. Nổi bọt - Bubble Sort.
4. Shaker Sort.
5. Chèn trực tiếp - Insertion Sort.
6. Chèn nhị phân - Binary Insertion Sort.
7. Shell Sort.
8. Heap Sort.
9. Quick Sort.
10. Merge Sort.
11. Radix Sort.

## Interchange Sort

### Ý tưởng
Xuất phát từ đầu dãy, tìm tất cả các nghịch thế chứa phần tử hiện hành và triệt tiêu chúng bằng cách đổi chỗ hai phần tử trong cặp nghịch thế. Lặp lại với phần tử kế tiếp.

### Các bước
1. `i = 0`.
2. `j = i + 1`.
3. Trong khi `j < n`, nếu `a[j] < a[i]` thì đổi chỗ `a[i]` và `a[j]`; sau đó tăng `j`.
4. Tăng `i`. Nếu `i < n - 1`, lặp lại từ bước 2; ngược lại dừng.

### Cài đặt

```cpp
void InterchangeSort(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (a[j] < a[i]) {
                Swap(a[i], a[j]);
            }
        }
    }
}
```

## Selection Sort

### Ý tưởng
Chọn phần tử nhỏ nhất trong dãy hiện hành và đưa về vị trí đầu dãy hiện hành. Sau đó xem dãy hiện hành chỉ còn `n - 1` phần tử, bắt đầu từ vị trí kế tiếp. Lặp lại cho đến khi dãy chỉ còn một phần tử.

### Các bước
1. `i = 0`.
2. Tìm phần tử `a[min]` nhỏ nhất trong đoạn từ `a[i]` đến cuối dãy.
3. Đổi chỗ `a[min]` và `a[i]`.
4. Nếu `i < n - 1`, tăng `i` và lặp lại bước 2; ngược lại dừng.

### Cài đặt

```cpp
void SelectionSort(int a[], int n) {
    int min;
    for (int i = 0; i < n - 1; i++) {
        min = i;
        for (int j = i + 1; j < n; j++) {
            if (a[j] < a[min]) {
                min = j;
            }
        }
        Swap(a[min], a[i]);
    }
}
```

## Tóm tắt chương
- Tìm kiếm tuyến tính duyệt lần lượt các phần tử, độ phức tạp `O(n)`.
- Tìm kiếm nhị phân chỉ áp dụng cho mảng đã sắp xếp và thu hẹp phạm vi tìm kiếm theo từng nửa.
- Sắp xếp là quá trình đưa danh sách về thứ tự thỏa mãn tiêu chuẩn.
- Interchange Sort triệt tiêu nghịch thế bằng đổi chỗ.
- Selection Sort chọn phần tử nhỏ nhất của dãy hiện hành và đưa về đầu dãy.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Tìm kiếm tuyến tính | Tìm bằng cách duyệt lần lượt từ đầu đến cuối |
| Lính canh | Phần tử thêm vào cuối dãy để giảm điều kiện kiểm tra |
| Tìm kiếm nhị phân | Tìm trên dãy có thứ tự bằng cách chia đôi phạm vi |
| Sắp xếp | Đưa danh sách về một thứ tự xác định |
| Nghịch thế | Cặp phần tử sai thứ tự trong dãy |
| Interchange Sort | Sắp xếp đổi chỗ trực tiếp |
| Selection Sort | Sắp xếp chọn trực tiếp |

## Câu hỏi ôn tập
1. Trình bày ý tưởng của tìm kiếm tuyến tính.
2. Lính canh trong tìm kiếm tuyến tính có tác dụng gì?
3. Điều kiện để dùng tìm kiếm nhị phân là gì?
4. Tìm kiếm nhị phân cập nhật `left`, `right` như thế nào?
5. Nghịch thế là gì?
6. Interchange Sort triệt tiêu nghịch thế như thế nào?
7. Selection Sort chọn phần tử nào trong mỗi lượt?
8. So sánh tìm kiếm tuyến tính và tìm kiếm nhị phân.
