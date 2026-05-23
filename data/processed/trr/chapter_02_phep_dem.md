# Chương 2: Phép đếm

## Nội dung chính
- Nguyên lý cộng và nguyên lý nhân.
- Nguyên lý chuồng bồ câu.
- Nguyên lý bù trừ.
- Hoán vị, chỉnh hợp, tổ hợp.
- Hoán vị lặp, tổ hợp lặp và bài toán chia vật đồng chất vào hộp phân biệt.
- Hệ thức đệ quy và phương trình đặc trưng.
- Ví dụ cầu thang và Tháp Hà Nội.

## Tổng quan
Phép đếm nghiên cứu cách xác định số khả năng xảy ra của một quá trình rời rạc. Các nguyên lý cơ bản như cộng, nhân, chuồng bồ câu và bù trừ là nền tảng để xây dựng công thức hoán vị, chỉnh hợp, tổ hợp và giải các bài toán đếm phức tạp hơn.

## Nguyên lý cộng

### Khái niệm chính
Nếu một công việc có thể thực hiện theo một trong $k$ trường hợp loại trừ nhau, với số cách tương ứng là $n_1,n_2,\ldots,n_k$, thì tổng số cách thực hiện là:

$$
n_1+n_2+\cdots+n_k
$$

### Ví dụ
Nếu có 3 cách chọn áo màu trắng và 4 cách chọn áo màu xanh, hai nhóm lựa chọn không trùng nhau, thì có $3+4=7$ cách chọn áo.

## Nguyên lý nhân

### Khái niệm chính
Nếu một công việc gồm $k$ bước liên tiếp, bước thứ $i$ có $n_i$ cách thực hiện, thì tổng số cách thực hiện công việc là:

$$
n_1 n_2 \cdots n_k
$$

Nếu đi từ $A$ đến $B$ có 3 đường và từ $B$ đến $C$ có 4 đường, thì đi từ $A$ đến $C$ qua $B$ có:

$$
3 \cdot 4 = 12
$$

cách.

## Nguyên lý chuồng bồ câu

### Khái niệm chính
Nếu đặt $n$ đối tượng vào $k$ hộp và $n>k$, thì có ít nhất một hộp chứa từ hai đối tượng trở lên.

Tổng quát hơn, nếu đặt $n$ đối tượng vào $k$ hộp, thì có ít nhất một hộp chứa ít nhất:

$$
\left\lceil \frac{n}{k} \right\rceil
$$

đối tượng.

**Ví dụ:** Trong 367 người, luôn có ít nhất 2 người sinh cùng ngày tháng.

**Giải:** Có nhiều nhất 366 ngày sinh khác nhau nếu tính cả ngày 29/2. Vì $367>366$, theo nguyên lý chuồng bồ câu, tồn tại ít nhất 2 người cùng ngày sinh.

**Ví dụ:** Có 20 chim bồ câu trong 7 chuồng.

**Giải:** Có ít nhất một chuồng chứa:

$$
\left\lceil \frac{20}{7} \right\rceil = 3
$$

chim.

**Ví dụ:** Mọi tập con 6 phần tử của $\{1,2,3,4,5,6,7,8,9\}$ có hai phần tử tổng bằng 10.

**Giải:** Chia các số thành các cặp có tổng 10:

$$
(1,9),(2,8),(3,7),(4,6)
$$

và phần tử riêng $5$. Khi chọn 6 phần tử từ 5 nhóm này, theo nguyên lý chuồng bồ câu phải có một nhóm được chọn ít nhất 2 phần tử. Nhóm đó là một cặp có tổng bằng 10.

## Nguyên lý bù trừ

### Hai tập

$$
|A \cup B| = |A| + |B| - |A \cap B|
$$

### Ba tập

$$
|A \cup B \cup C|
= |A| + |B| + |C|
- |A \cap B| - |A \cap C| - |B \cap C|
+ |A \cap B \cap C|
$$

Trong bài toán lớp học tiếng Anh và tiếng Pháp, nếu biết số học sinh học từng môn và số học sinh học cả hai môn, dùng công thức bù trừ để tính số học sinh học ít nhất một trong hai môn.

## Hoán vị

### Khái niệm
Hoán vị của $n$ phần tử là một cách sắp xếp thứ tự toàn bộ $n$ phần tử.

### Công thức

$$
P_n = n!
$$

## Chỉnh hợp

Chỉnh hợp chập $k$ của $n$ phần tử là cách chọn $k$ phần tử từ $n$ phần tử và sắp thứ tự chúng.

### Công thức

$$
A_n^k = \frac{n!}{(n-k)!}
$$

## Tổ hợp

Tổ hợp chập $k$ của $n$ phần tử là cách chọn $k$ phần tử từ $n$ phần tử mà không xét thứ tự.

### Công thức

$$
C_n^k = \binom{n}{k} = \frac{n!}{k!(n-k)!}
$$

## Hoán vị lặp

Nếu có $n$ phần tử, trong đó có $n_1$ phần tử loại 1, $n_2$ phần tử loại 2, ..., $n_k$ phần tử loại $k$ giống nhau, với:

$$
n_1+n_2+\cdots+n_k=n
$$

số hoán vị phân biệt là:

$$
\frac{n!}{n_1!n_2!\cdots n_k!}
$$

## Tổ hợp lặp

Số cách chọn $k$ phần tử từ $n$ loại phần tử, cho phép lặp và không xét thứ tự, là:

$$
\binom{n+k-1}{k}
$$

### Bài toán chia vật đồng chất vào hộp phân biệt
Số cách chia $k$ vật đồng chất vào $n$ hộp phân biệt, cho phép hộp rỗng, là:

$$
\binom{n+k-1}{k}
$$

## Hệ thức đệ quy

Hệ thức đệ quy mô tả một dãy số bằng cách xác định số hạng hiện tại thông qua các số hạng trước đó.

### Ví dụ cầu thang
Nếu mỗi lần có thể bước 1 hoặc 2 bậc, số cách đi lên $n$ bậc thường được mô tả bởi:

$$
F_n = F_{n-1}+F_{n-2}
$$

### Ví dụ Tháp Hà Nội
Với $n$ đĩa, số bước chuyển tối thiểu thỏa mãn:

$$
T_n = 2T_{n-1}+1,\quad T_1=1
$$

Suy ra:

$$
T_n = 2^n - 1
$$

## Hệ thức đệ quy tuyến tính

### Thuần nhất
Hệ thức đệ quy tuyến tính thuần nhất cấp $k$ có dạng:

$$
a_n = c_1a_{n-1}+c_2a_{n-2}+\cdots+c_ka_{n-k}
$$

### Phương trình đặc trưng
Phương trình đặc trưng tương ứng:

$$
r^k - c_1r^{k-1}-c_2r^{k-2}-\cdots-c_k=0
$$

Với cấp 1:

$$
a_n = ca_{n-1}
$$

thì nghiệm có dạng:

$$
a_n = a_0c^n
$$

Với cấp 2:

$$
a_n = c_1a_{n-1}+c_2a_{n-2}
$$

xét phương trình:

$$
r^2-c_1r-c_2=0
$$

## Tóm tắt chương
- Nguyên lý cộng dùng cho các trường hợp loại trừ nhau.
- Nguyên lý nhân dùng cho công việc gồm nhiều bước liên tiếp.
- Nguyên lý chuồng bồ câu bảo đảm tồn tại hộp chứa nhiều đối tượng.
- Nguyên lý bù trừ tránh đếm trùng.
- Hoán vị xét thứ tự toàn bộ, chỉnh hợp xét chọn có thứ tự, tổ hợp xét chọn không thứ tự.
- Hệ thức đệ quy mô tả dãy thông qua các giá trị trước đó.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Nguyên lý cộng | Đếm tổng các trường hợp rời nhau |
| Nguyên lý nhân | Nhân số cách của các bước liên tiếp |
| Nguyên lý chuồng bồ câu | Nếu nhiều đối tượng hơn hộp thì có hộp chứa ít nhất hai đối tượng |
| Nguyên lý bù trừ | Công thức đếm hợp các tập có phần giao |
| Hoán vị | Sắp xếp toàn bộ phần tử |
| Chỉnh hợp | Chọn có xét thứ tự |
| Tổ hợp | Chọn không xét thứ tự |
| Hệ thức đệ quy | Công thức xác định số hạng qua số hạng trước |

## Công thức cần nhớ
- $P_n=n!$
- $A_n^k=\dfrac{n!}{(n-k)!}$
- $C_n^k=\binom{n}{k}=\dfrac{n!}{k!(n-k)!}$
- $|A \cup B|=|A|+|B|-|A \cap B|$
- $\left\lceil \dfrac{n}{k}\right\rceil$
- $\binom{n+k-1}{k}$
- $T_n=2T_{n-1}+1=2^n-1$

## Câu hỏi ôn tập
1. Khi nào dùng nguyên lý cộng?
2. Khi nào dùng nguyên lý nhân?
3. Phát biểu nguyên lý chuồng bồ câu.
4. Viết công thức bù trừ cho hai tập.
5. Phân biệt hoán vị, chỉnh hợp và tổ hợp.
6. Hoán vị lặp được tính như thế nào?
7. Bài toán chia vật đồng chất vào hộp phân biệt dùng công thức nào?
8. Hệ thức đệ quy của bài toán Tháp Hà Nội là gì?
