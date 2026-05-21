# Chương 4: Đồ thị

## Nội dung chính
- Khái niệm đồ thị vô hướng, đồ thị có hướng, đỉnh và cạnh.
- Cạnh kề, đỉnh kề, cạnh song song, khuyên.
- Đơn đồ thị, đa đồ thị, giả đồ thị và đa đồ thị có hướng.
- Bậc của đỉnh, bậc vào, bậc ra, đỉnh cô lập, đỉnh treo.
- Ma trận kề và biểu diễn đồ thị.
- Đẳng cấu đồ thị.
- Đường đi, chu trình, liên thông, thành phần liên thông, đỉnh khớp, cầu.
- Một số đồ thị đặc biệt.
- Đường đi Euler, chu trình Euler, đường đi Hamilton, chu trình Hamilton.
- Đồ thị có trọng số và thuật toán Dijkstra.

## Tổng quan
Đồ thị là mô hình toán học dùng để biểu diễn các đối tượng và quan hệ giữa chúng. Đỉnh biểu diễn đối tượng, cạnh hoặc cung biểu diễn quan hệ. Đồ thị được dùng rộng rãi trong mạng máy tính, giao thông, lập lịch, tối ưu đường đi và nhiều bài toán rời rạc khác.

## Đồ thị vô hướng

### Định nghĩa
Một đồ thị vô hướng $G=(V,E)$ gồm:

- $V$: tập các đỉnh.
- $E$: tập các cạnh, mỗi cạnh nối hai đỉnh không xét hướng.

### Khái niệm liên quan
- Cạnh kề: hai cạnh có chung một đỉnh.
- Đỉnh kề: hai đỉnh được nối bởi một cạnh.
- Cạnh song song: hai hoặc nhiều cạnh nối cùng một cặp đỉnh.
- Khuyên: cạnh nối một đỉnh với chính nó.

### Phân loại
| Loại đồ thị | Đặc điểm |
|---|---|
| Đơn đồ thị vô hướng | Không có cạnh song song, không có khuyên |
| Đa đồ thị vô hướng | Có thể có cạnh song song |
| Giả đồ thị | Có thể có cạnh song song và khuyên |

## Đồ thị có hướng

Trong đồ thị có hướng, cạnh có chiều và được gọi là cung.

Một cung có:

- Đỉnh đầu.
- Đỉnh cuối.

Đa đồ thị có hướng có thể có các cung song song.

## Bậc của đỉnh

### Đồ thị vô hướng
Bậc của đỉnh là số cạnh liên thuộc với đỉnh đó. Khuyên được tính hai lần vào bậc.

Đỉnh cô lập là đỉnh có bậc 0. Đỉnh treo là đỉnh có bậc 1.

### Định lý tổng bậc
Với đồ thị vô hướng có $m$ cạnh:

$$
\sum_{v \in V} \deg(v) = 2m
$$

### Đồ thị có hướng
Với đồ thị có hướng:

- Bậc vào $\deg^-(v)$ là số cung đi vào $v$.
- Bậc ra $\deg^+(v)$ là số cung đi ra từ $v$.

Tổng bậc vào bằng tổng bậc ra và bằng số cung:

$$
\sum_{v \in V} \deg^-(v) = \sum_{v \in V} \deg^+(v) = |E|
$$

## Biểu diễn đồ thị bằng ma trận kề

Cho đồ thị có $n$ đỉnh. Ma trận kề là ma trận vuông $A=(a_{ij})$ kích thước $n \times n$.

### Đồ thị vô hướng

$$
a_{ij} =
\begin{cases}
1, & \text{nếu có cạnh nối } v_i \text{ và } v_j \\
0, & \text{nếu không có cạnh}
\end{cases}
$$

Ma trận kề của đồ thị vô hướng là ma trận đối xứng.

### Đồ thị có hướng

$$
a_{ij} =
\begin{cases}
1, & \text{nếu có cung từ } v_i \text{ đến } v_j \\
0, & \text{nếu không có cung}
\end{cases}
$$

## Đẳng cấu đồ thị

Hai đồ thị đẳng cấu nếu tồn tại một song ánh giữa tập đỉnh của chúng sao cho quan hệ kề được bảo toàn.

Điều kiện cần để hai đồ thị đẳng cấu:

- Cùng số đỉnh.
- Cùng số cạnh.
- Cùng số đỉnh theo từng bậc.
- Bậc của đỉnh được bảo toàn qua ánh xạ.

## Đường đi, chu trình và liên thông

### Đường đi
Đường đi là dãy đỉnh và cạnh liên tiếp nhau. Đường đi đơn là đường đi không lặp cạnh. Đường đi sơ cấp là đường đi không lặp đỉnh.

### Chu trình
Chu trình là đường đi có đỉnh đầu trùng đỉnh cuối.

### Liên thông
Đồ thị vô hướng liên thông nếu giữa mọi cặp đỉnh đều có đường đi.

Nếu đồ thị không liên thông, nó gồm nhiều thành phần liên thông.

### Đỉnh khớp và cầu
- Đỉnh khớp là đỉnh mà khi loại bỏ nó làm tăng số thành phần liên thông.
- Cầu là cạnh mà khi loại bỏ nó làm tăng số thành phần liên thông.

## Một số đồ thị vô hướng đặc biệt

| Đồ thị | Ký hiệu/Đặc điểm |
|---|---|
| Đồ thị đủ | $K_n$, mọi cặp đỉnh phân biệt đều kề nhau |
| Đồ thị $k$-đều | Mọi đỉnh đều có bậc $k$ |
| Đồ thị lưỡng phân | Tập đỉnh chia thành hai phần, cạnh chỉ nối giữa hai phần |
| Đồ thị lưỡng phân đủ | Mọi đỉnh phần này nối với mọi đỉnh phần kia |
| Đồ thị bù | Cạnh xuất hiện khi cạnh tương ứng không có trong đồ thị gốc |
| Cycle | $C_n$, chu trình $n$ đỉnh |
| Wheel | $W_n$, thêm một đỉnh tâm nối với các đỉnh của cycle |
| Hypercube | $Q_n$, đồ thị lập phương $n$ chiều |

## Euler

### Đường đi Euler
Đường đi Euler là đường đi đi qua mỗi cạnh của đồ thị đúng một lần.

### Chu trình Euler
Chu trình Euler là chu trình đi qua mỗi cạnh đúng một lần.

### Điều kiện trong đồ thị vô hướng liên thông
- Có chu trình Euler khi mọi đỉnh đều có bậc chẵn.
- Có đường đi Euler nhưng không có chu trình Euler khi có đúng hai đỉnh bậc lẻ.

### Thuật toán Fleury
Ý tưởng của thuật toán Fleury:

1. Bắt đầu từ đỉnh phù hợp.
2. Mỗi bước chọn một cạnh chưa đi qua.
3. Không chọn cầu nếu còn lựa chọn khác.
4. Xóa cạnh đã đi qua khỏi đồ thị.
5. Lặp đến khi đi qua hết các cạnh.

## Hamilton

### Đường đi Hamilton
Đường đi Hamilton là đường đi qua mỗi đỉnh đúng một lần.

### Chu trình Hamilton
Chu trình Hamilton là chu trình qua mỗi đỉnh đúng một lần và quay về đỉnh xuất phát.

### Định lý Ore
Nếu đồ thị đơn có $n \ge 3$ đỉnh và với mọi cặp đỉnh không kề $u,v$:

$$
\deg(u)+\deg(v) \ge n
$$

thì đồ thị có chu trình Hamilton.

### Định lý Dirac
Nếu đồ thị đơn có $n \ge 3$ đỉnh và mọi đỉnh đều có bậc ít nhất $\frac{n}{2}$:

$$
\deg(v) \ge \frac{n}{2}
$$

thì đồ thị có chu trình Hamilton.

## Đồ thị có trọng số và đường đi ngắn nhất

Đồ thị có trọng số là đồ thị mà mỗi cạnh có một giá trị trọng số. Trọng số có thể biểu diễn bằng ma trận khoảng cách hoặc ma trận trọng số.

### Bài toán đường đi ngắn nhất
Bài toán yêu cầu tìm đường đi có tổng trọng số nhỏ nhất từ một đỉnh nguồn đến một đỉnh hoặc đến tất cả các đỉnh còn lại.

## Thuật toán Dijkstra

### Ý tưởng
Thuật toán Dijkstra tìm đường đi ngắn nhất từ một đỉnh nguồn đến các đỉnh còn lại trong đồ thị có trọng số không âm.

### Các bước
1. Gán khoảng cách từ nguồn đến chính nó bằng 0, đến các đỉnh khác bằng $\infty$.
2. Chọn đỉnh chưa xét có khoảng cách tạm thời nhỏ nhất.
3. Cố định đỉnh đó.
4. Cập nhật khoảng cách đến các đỉnh kề nếu tìm được đường đi ngắn hơn.
5. Lặp đến khi mọi đỉnh cần xét đã được cố định.

### Công thức cập nhật
Nếu đang xét đỉnh $u$ và có cạnh từ $u$ đến $v$ trọng số $w(u,v)$, cập nhật:

$$
d(v) = \min(d(v), d(u)+w(u,v))
$$

## Tóm tắt chương
- Đồ thị gồm tập đỉnh và tập cạnh hoặc cung.
- Đồ thị có thể vô hướng, có hướng, đơn, đa đồ thị hoặc giả đồ thị.
- Tổng bậc của đồ thị vô hướng bằng hai lần số cạnh.
- Ma trận kề biểu diễn quan hệ kề giữa các đỉnh.
- Liên thông, đỉnh khớp và cầu mô tả cấu trúc kết nối của đồ thị.
- Euler xét việc đi qua cạnh, Hamilton xét việc đi qua đỉnh.
- Dijkstra giải bài toán đường đi ngắn nhất với trọng số không âm.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Đồ thị | Cấu trúc gồm đỉnh và cạnh |
| Đỉnh | Đối tượng trong đồ thị |
| Cạnh | Liên kết giữa hai đỉnh |
| Cung | Cạnh có hướng |
| Bậc | Số cạnh liên thuộc với đỉnh |
| Bậc vào | Số cung đi vào một đỉnh |
| Bậc ra | Số cung đi ra từ một đỉnh |
| Ma trận kề | Ma trận biểu diễn cạnh giữa các đỉnh |
| Đẳng cấu | Hai đồ thị có cấu trúc kề tương ứng |
| Đường đi Euler | Đường đi qua mỗi cạnh đúng một lần |
| Chu trình Hamilton | Chu trình qua mỗi đỉnh đúng một lần |
| Dijkstra | Thuật toán tìm đường đi ngắn nhất |

## Công thức cần nhớ
- $\sum_{v \in V}\deg(v)=2m$
- $\sum_{v \in V}\deg^-(v)=\sum_{v \in V}\deg^+(v)=|E|$
- Điều kiện Ore: $\deg(u)+\deg(v)\ge n$
- Điều kiện Dirac: $\deg(v)\ge \frac{n}{2}$
- Dijkstra: $d(v)=\min(d(v),d(u)+w(u,v))$

## Câu hỏi ôn tập
1. Đồ thị vô hướng được định nghĩa như thế nào?
2. Phân biệt cạnh song song và khuyên.
3. Đơn đồ thị, đa đồ thị và giả đồ thị khác nhau ra sao?
4. Bậc vào và bậc ra là gì?
5. Phát biểu định lý tổng bậc của đồ thị vô hướng.
6. Ma trận kề của đồ thị vô hướng có tính chất gì?
7. Nêu điều kiện cần để hai đồ thị đẳng cấu.
8. Phân biệt đường đi Euler và đường đi Hamilton.
9. Điều kiện tồn tại chu trình Euler trong đồ thị vô hướng liên thông là gì?
10. Thuật toán Dijkstra cập nhật khoảng cách như thế nào?
