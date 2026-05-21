# Chương 4.2: Cây nhị phân tìm kiếm

## Nội dung chính
- Định nghĩa cây nhị phân tìm kiếm.
- Ưu điểm của cây nhị phân tìm kiếm.
- Cấu trúc dữ liệu node và cây.
- Tạo cây rỗng, tạo node, thêm node.
- Tìm kiếm bằng đệ quy và không đệ quy.
- Xóa node trong ba trường hợp.
- Nhận xét độ phức tạp.

## Tổng quan
Cây nhị phân tìm kiếm là cây nhị phân có quy tắc bố trí khóa: khóa trong cây con trái nhỏ hơn khóa ở nút hiện hành, khóa trong cây con phải lớn hơn khóa ở nút hiện hành. Quy tắc này giúp định hướng quá trình tìm kiếm, thêm và xóa.

## Định nghĩa cây nhị phân tìm kiếm

Cây nhị phân tìm kiếm là cây nhị phân bảo đảm:

- Các nút trong cây con trái nhỏ hơn nút hiện hành.
- Các nút trong cây con phải lớn hơn nút hiện hành.

Nhờ trật tự này, khi tìm kiếm có thể quyết định đi sang trái hay sang phải thay vì duyệt toàn bộ cây.

## Ưu điểm

Với cây gồm `n` phần tử:

- Trường hợp tốt nhất: chiều cao `h = log2(n)`.
- Trường hợp xấu nhất: chiều cao `h = n`.

Trường hợp xấu nhất xảy ra khi cây bị suy biến thành dạng gần như danh sách liên kết.

## Cấu trúc dữ liệu

```cpp
typedef struct tagTNode {
    int Key;
    struct tagTNode *pLeft;
    struct tagTNode *pRight;
} TNode;

typedef TNode* TREE;
```

## Các thao tác trên cây nhị phân tìm kiếm

- Tạo cây rỗng.
- Tạo node có trường `Key` bằng `x`.
- Thêm node vào cây.
- Xóa node có `Key` bằng `x`.
- Tìm node có khóa bằng `x`.

## Tạo cây rỗng

Cây rỗng có địa chỉ nút gốc bằng `NULL`.

```cpp
void CreateTree(TREE &T) {
    T = NULL;
}
```

## Tạo một node

```cpp
TNode* CreateTNode(int x) {
    TNode *p;
    p = new TNode;
    if (p == NULL) {
        exit(1);
    } else {
        p->Key = x;
        p->pLeft = NULL;
        p->pRight = NULL;
    }
    return p;
}
```

## Thêm một node

Ràng buộc: sau khi thêm, cây vẫn phải là cây nhị phân tìm kiếm.

```cpp
int InsertNode(TREE &T, int x) {
    if (T) {
        if (T->Key == x) {
            return 0;
        }
        if (T->Key > x) {
            return InsertNode(T->pLeft, x);
        }
        return InsertNode(T->pRight, x);
    }

    T = new TNode;
    if (T == NULL) {
        return -1;
    }
    T->Key = x;
    T->pLeft = T->pRight = NULL;
    return 1;
}
```

**Ví dụ:** Khi thêm `x = 50` vào cây có các nút 44, 18, 88, 13, 37, 59, 108, 15, 23, 40, 55, 71, ta so sánh để đi sang phải của 44, sang trái của 88, sang trái của 59 và tiếp tục theo quy tắc khóa.

## Tìm kiếm node

### Tìm kiếm không đệ quy

```cpp
TNode* SearchNode(TREE root, int x) {
    TNode *p = root;
    while (p != NULL) {
        if (x == p->Key) {
            return p;
        } else if (x < p->Key) {
            p = p->pLeft;
        } else {
            p = p->pRight;
        }
    }
    return NULL;
}
```

### Tìm kiếm đệ quy

```cpp
TNode* SearchTNode(TREE T, int x) {
    if (T != NULL) {
        if (T->Key == x) {
            return T;
        } else if (x > T->Key) {
            return SearchTNode(T->pRight, x);
        } else {
            return SearchTNode(T->pLeft, x);
        }
    }
    return NULL;
}
```

## Xóa một node

Khi xóa node có khóa `x`, phải bảo đảm cây sau khi xóa vẫn là cây nhị phân tìm kiếm.

Có ba trường hợp:

1. `x` là nút lá.
2. `x` chỉ có một cây con.
3. `x` có đầy đủ hai cây con.

### Trường hợp 1: Node là nút lá
Xóa node và gán liên kết từ cha của nó thành rỗng. Việc này không ảnh hưởng đến các node khác.

### Trường hợp 2: Node có một cây con
Trước khi xóa `x`, móc nối cha của `x` với cây con duy nhất của `x`, sau đó xóa node `x`.

### Trường hợp 3: Node có hai cây con
Dùng cách xóa gián tiếp:

1. Tìm node thế mạng `y`.
2. Chuyển thông tin của `y` lên node `x`.
3. Xóa node `y`, khi đó `y` chỉ rơi vào trường hợp 1 hoặc 2.

Có hai cách tìm node thế mạng:

- `y` là node có khóa nhỏ nhất bên cây con phải của `x`.
- `y` là node có khóa lớn nhất bên cây con trái của `x`.

## Nhận xét độ phức tạp

Các thao tác tìm kiếm, thêm và xóa có độ phức tạp trung bình `O(h)`, với `h` là chiều cao của cây.

- Trường hợp tốt nhất: cây có `n` nút và `h = log2(n)`, chi phí tương đương tìm kiếm nhị phân trên mảng có thứ tự.
- Trường hợp xấu nhất: cây suy biến thành danh sách liên kết, chi phí có thể tăng theo số nút.

## Tóm tắt chương
- Cây nhị phân tìm kiếm tổ chức khóa theo quy tắc trái nhỏ hơn, phải lớn hơn.
- Tìm kiếm, thêm, xóa đều dựa trên quy tắc so sánh khóa.
- Xóa node cần xét ba trường hợp: nút lá, một con, hai con.
- Hiệu quả phụ thuộc vào chiều cao cây.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Cây nhị phân tìm kiếm | Cây nhị phân có khóa trái nhỏ hơn và khóa phải lớn hơn node hiện hành |
| `Key` | Khóa dùng để so sánh trong cây |
| Node lá | Node không có cây con |
| Node thế mạng | Node dùng để thay thế khi xóa node có hai cây con |
| Chiều cao cây | Độ dài lớn nhất từ gốc đến lá |
| Suy biến | Cây mất cân bằng thành dạng gần danh sách |

## Câu hỏi ôn tập
1. Cây nhị phân tìm kiếm có quy tắc bố trí khóa như thế nào?
2. Vì sao cây nhị phân tìm kiếm hỗ trợ tìm kiếm hiệu quả?
3. Trình bày thuật toán thêm node vào cây.
4. Tìm kiếm đệ quy và không đệ quy khác nhau như thế nào?
5. Khi xóa node có một cây con cần xử lý ra sao?
6. Khi xóa node có hai cây con, node thế mạng được chọn như thế nào?
7. Độ phức tạp của tìm kiếm trên cây phụ thuộc vào yếu tố nào?
