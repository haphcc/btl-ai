# Chương 6: Đồ thị

## Nội dung chính
- Khái niệm đồ thị, đỉnh, cạnh, đồ thị có hướng, vô hướng và có trọng số.
- Đường đi, chu trình và tính liên thông.
- Biểu diễn đồ thị bằng danh sách kề và ma trận kề.
- So sánh bộ nhớ giữa danh sách kề và ma trận kề.
- Tìm kiếm theo chiều sâu DFS.
- Tìm kiếm theo chiều rộng BFS.
- Thành phần liên thông, đỉnh cắt và cạnh cầu.

## Tổng quan
Đồ thị là cấu trúc dữ liệu dùng để biểu diễn quan hệ giữa các đối tượng. Mỗi đối tượng là một đỉnh, quan hệ giữa hai đối tượng là một cạnh. Chương này trình bày cách biểu diễn đồ thị và hai thuật toán duyệt quan trọng: DFS và BFS.

## 1. Các khái niệm

Một đồ thị `G = (V, E)` gồm:

- `V`: tập hữu hạn các nút hoặc đỉnh (vertices).
- `E`: tập hữu hạn các cặp đỉnh gọi là cạnh (edge).

Nếu `(v1, v2)` thuộc `E`, có một cạnh nối giữa `v1` và `v2`.

### Đồ thị có hướng và vô hướng
- Nếu cạnh `(v1, v2)` khác cạnh `(v2, v1)`, đó là đồ thị có hướng. Cạnh `(v1, v2)` có hướng từ `v1` đến `v2`.
- Nếu thứ tự các đỉnh trên cạnh không được quan tâm, đó là đồ thị vô hướng.

### Đường đi, chu trình, liên thông
- Đường đi đơn là đường đi mà mọi đỉnh trên đó, trừ đỉnh đầu và đỉnh cuối, đều khác nhau.
- Chu trình là đường đi đơn có đỉnh đầu và đỉnh cuối trùng nhau.
- Đồ thị liên thông nếu với mọi cặp đỉnh phân biệt `vi`, `vj` đều có đường đi từ `vi` đến `vj`.
- Đồ thị có trọng số là đồ thị mà mỗi cạnh gắn với một giá trị.

## 2. Biểu diễn đồ thị

Có hai cách thường dùng để biểu diễn đồ thị:

- Danh sách kề (adjacency list).
- Ma trận kề (adjacency matrix).

Danh sách kề thường dùng cho đồ thị thưa, khi số cạnh `|E|` nhỏ hơn nhiều so với `|V|^2`. Ma trận kề thường dùng cho đồ thị dày, khi `|E|` gần `|V|^2`.

## Danh sách kề

Với đồ thị `G = (V, E)`, danh sách kề là một mảng `Adj` có `|V|` danh sách. Mỗi danh sách ứng với một đỉnh.

Với mỗi đỉnh `u`, danh sách `Adj[u]` chứa tất cả các đỉnh `v` sao cho có cạnh `(u, v)` thuộc `E`.

### Độ dài danh sách kề
- Với đồ thị vô hướng, tổng độ dài tất cả danh sách kề là `2|E|`.
- Với đồ thị có hướng, tổng độ dài tất cả danh sách kề là `|E|`.

### Đồ thị có trọng số
Danh sách kề có thể biểu diễn đồ thị có trọng số bằng cách lưu kèm trọng số `w(u, v)` với đỉnh `v` trong danh sách kề của `u`.

## Ma trận kề

Giả sử các đỉnh được đánh số từ `1` đến `|V|`. Ma trận kề của `G` là ma trận vuông `A = (aij)` kích thước `|V| x |V|`.

```text
aij = 1 nếu (i, j) thuộc E
aij = 0 nếu (i, j) không thuộc E
```

Với đồ thị vô hướng, ma trận kề là ma trận đối xứng:

```text
A = A^T
```

Tổng các phần tử trên dòng `i` hoặc cột `j` của ma trận kề là bậc của đỉnh tương ứng trong đồ thị vô hướng.

### Ma trận trọng số
Với đồ thị có trọng số, trọng số `w(u, v)` của cạnh `(u, v)` được lưu ở hàng `u`, cột `v`. Nếu không có cạnh, có thể lưu `NIL`, `0` hoặc `∞` tùy quy ước.

## So sánh cách biểu diễn

| Cách biểu diễn | Bộ nhớ | Phù hợp |
|---|---|---|
| Danh sách kề | `Θ(V + E)` | Đồ thị thưa |
| Ma trận kề | `Θ(V^2)` | Đồ thị nhỏ hoặc đồ thị dày |

Ma trận kề đơn giản, nhưng bộ nhớ không phụ thuộc vào số cạnh. Nếu đồ thị không có trọng số, mỗi phần tử ma trận có thể biểu diễn bằng một bit.

## 3. Các thuật toán tìm kiếm trên đồ thị

Hai thuật toán tìm kiếm chính:

- DFS (Depth-First Search): tìm kiếm theo chiều sâu.
- BFS (Breadth-First Search): tìm kiếm theo chiều rộng.

## DFS

### Ý tưởng
DFS tìm sâu hơn trong đồ thị bất cứ khi nào có thể. Khi các cạnh của một đỉnh đã được thăm hết, thuật toán quay lui để thăm các cạnh khác.

### Các bước
Xuất phát từ một đỉnh `v`:

1. Đánh dấu `v` đã được duyệt.
2. Với mỗi đỉnh `w` chưa duyệt kề với `v`, thực hiện DFS từ `w`.
3. Lặp lại cho đến khi tất cả các đỉnh liên quan được duyệt.

### Mã giả

```text
DFS(v)
    VISITED(v) = 1
    for mỗi đỉnh w lân cận của v
        if VISITED(w) == 0
            DFS(w)
    return
```

### Độ phức tạp
- Nếu đồ thị biểu diễn bằng danh sách kề: `O(E)`.
- Nếu đồ thị biểu diễn bằng ma trận kề: `O(n^2)`.

## BFS

### Ý tưởng
BFS duyệt theo chiều rộng. Sau khi thăm đỉnh `v`, các đỉnh chưa thăm kề với `v` được thăm kế tiếp; sau đó mới đến các đỉnh kề với các đỉnh này.

### Các bước
Xuất phát từ một đỉnh `v`:

1. Đánh dấu `v` đã được duyệt.
2. Chọn đỉnh đã duyệt nhưng còn đỉnh kề chưa duyệt; ưu tiên đỉnh được đánh dấu sớm.
3. Đánh dấu tất cả các đỉnh kề chưa duyệt.
4. Lặp lại cho đến khi tất cả các đỉnh được duyệt.

### Mã giả

```text
BFS(v)
    VISITED(v) = 1
    Khởi tạo queue Q với v
    while Q không rỗng
        lấy v ra khỏi Q
        for mỗi w kề với v
            if VISITED(w) == 0
                đưa w vào Q
                VISITED(w) = 1
    return
```

### Độ phức tạp
- Nếu đồ thị biểu diễn bằng danh sách kề: `O(E)`.
- Nếu đồ thị biểu diễn bằng ma trận kề: `O(n^2)`.

## 4. Tính liên thông của đồ thị

Đồ thị liên thông là đồ thị mà hai đỉnh bất kỳ đều liên thông với nhau.

Nếu đồ thị không liên thông, nó được chia thành các thành phần liên thông. Mỗi tập con trong phân hoạch cùng với các cạnh nối các đỉnh của chúng tạo thành một đồ thị thành phần.

## Đỉnh cắt và cạnh cầu

### Đỉnh cắt
Đỉnh `v` được gọi là đỉnh cắt nếu bỏ nó cùng các cạnh liên thuộc làm tăng số thành phần liên thông của đồ thị con.

### Cạnh cầu
Cạnh `e` được gọi là cạnh cầu nếu xóa nó làm tăng số thành phần liên thông của đồ thị con.

## Tóm tắt chương
- Đồ thị gồm tập đỉnh và tập cạnh.
- Đồ thị có thể có hướng, vô hướng hoặc có trọng số.
- Danh sách kề tiết kiệm bộ nhớ cho đồ thị thưa.
- Ma trận kề đơn giản và phù hợp với đồ thị nhỏ hoặc dày.
- DFS duyệt sâu và có quay lui.
- BFS duyệt theo từng lớp và dùng queue.
- Tính liên thông mô tả khả năng đi từ một đỉnh đến các đỉnh khác.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Đồ thị | Cấu trúc gồm đỉnh và cạnh |
| Đỉnh | Node hoặc vertex trong đồ thị |
| Cạnh | Quan hệ nối giữa hai đỉnh |
| Đồ thị có hướng | Cạnh có chiều |
| Đồ thị vô hướng | Cạnh không xét chiều |
| Đồ thị có trọng số | Cạnh có giá trị trọng số |
| Danh sách kề | Mảng các danh sách đỉnh kề |
| Ma trận kề | Ma trận biểu diễn cạnh giữa các cặp đỉnh |
| DFS | Tìm kiếm theo chiều sâu |
| BFS | Tìm kiếm theo chiều rộng |
| Thành phần liên thông | Một phần liên thông của đồ thị không liên thông |
| Đỉnh cắt | Đỉnh mà khi xóa làm tăng số thành phần liên thông |
| Cạnh cầu | Cạnh mà khi xóa làm tăng số thành phần liên thông |

## Câu hỏi ôn tập
1. Đồ thị `G = (V, E)` gồm những thành phần nào?
2. Phân biệt đồ thị có hướng và vô hướng.
3. Đường đi đơn và chu trình khác nhau như thế nào?
4. Danh sách kề biểu diễn đồ thị như thế nào?
5. Ma trận kề của đồ thị vô hướng có đặc điểm gì?
6. So sánh danh sách kề và ma trận kề về bộ nhớ.
7. Trình bày ý tưởng của DFS.
8. Trình bày ý tưởng của BFS.
9. Thành phần liên thông là gì?
10. Đỉnh cắt và cạnh cầu được định nghĩa như thế nào?
