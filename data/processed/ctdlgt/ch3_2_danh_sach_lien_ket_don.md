# Chương 3.2: Danh sách liên kết đơn

## Nội dung chính
- Tổ chức của danh sách liên kết đơn.
- Cấu trúc dữ liệu của node và list.
- Tạo node mới.
- Thêm node vào đầu, cuối và sau một node `q`.
- Xóa node đầu, xóa node sau `q`, xóa node có khóa `x`.
- Tìm kiếm, duyệt, in và hủy toàn bộ danh sách.
- Sắp xếp danh sách liên kết đơn.

## Tổng quan
Danh sách liên kết đơn là danh sách trong đó mỗi phần tử chỉ liên kết với phần tử đứng ngay sau nó. Cấu trúc này linh hoạt khi thêm hoặc xóa phần tử vì không cần dịch chuyển phần tử như mảng.

## Tổ chức danh sách liên kết đơn

Mỗi phần tử trong danh sách liên kết đơn là một cấu trúc có hai phần:

- Thành phần dữ liệu: lưu thông tin của bản thân phần tử.
- Thành phần liên kết: lưu địa chỉ của phần tử đứng sau trong danh sách, hoặc `NULL` nếu là phần tử cuối.

## Cấu trúc dữ liệu

### Cấu trúc node

```cpp
typedef struct tagNode {
    Data Info;              // Lưu thông tin bản thân
    struct tagNode *pNext;  // Lưu địa chỉ node đứng sau
} Node;
```

### Cấu trúc list

```cpp
typedef struct tagList {
    Node *pHead; // Địa chỉ node đầu tiên
    Node *pTail; // Địa chỉ node cuối cùng
} LIST;
```

## Các thao tác cơ bản

Các thao tác trên danh sách liên kết đơn:

- Tạo danh sách rỗng.
- Tạo node có trường `Info` bằng `x`.
- Tìm phần tử có `Info` bằng `x`.
- Thêm phần tử có khóa `x`.
- Hủy phần tử trong danh sách.
- Duyệt danh sách.
- Sắp xếp danh sách.

## Tạo node mới

Hàm tạo node mới trả về địa chỉ node vừa tạo.

```cpp
Node* CreateNode(Data x) {
    Node *p;
    p = new Node;
    if (p == NULL) {
        exit(1);
    }
    p->Info = x;
    p->pNext = NULL;
    return p;
}
```

## Thêm phần tử vào danh sách

Các vị trí cần thêm:

- Thêm vào đầu list.
- Thêm vào cuối list.
- Thêm vào sau một phần tử `q`.

### Thêm vào đầu danh sách
Thuật toán thêm node `p` vào đầu:

1. Nếu list rỗng:
   - `pHead = p`.
   - `pTail = pHead`.
2. Ngược lại:
   - `p->pNext = pHead`.
   - `pHead = p`.

```cpp
void AddHead(LIST &l, Node *p) {
    if (l.pHead == NULL) {
        l.pHead = p;
        l.pTail = l.pHead;
    } else {
        p->pNext = l.pHead;
        l.pHead = p;
    }
}
```

### Thêm vào cuối danh sách
Thuật toán thêm node `p` vào cuối:

1. Nếu list rỗng:
   - `pHead = p`.
   - `pTail = pHead`.
2. Ngược lại:
   - `pTail->pNext = p`.
   - `pTail = p`.

```cpp
void AddTail(LIST &l, Node *p) {
    if (l.pHead == NULL) {
        l.pHead = p;
        l.pTail = l.pHead;
    } else {
        l.pTail->pNext = p;
        l.pTail = p;
    }
}
```

### Thêm sau node `q`
Thuật toán thêm node `p` vào sau node `q`:

1. Nếu `q != NULL`:
   - `p->pNext = q->pNext`.
   - `q->pNext = p`.
   - Nếu `q == pTail` thì cập nhật `pTail = p`.
2. Nếu `q == NULL`, có thể xử lý như thêm vào đầu danh sách.

```cpp
void InsertAfterQ(LIST &l, Node *p, Node *q) {
    if (q != NULL) {
        p->pNext = q->pNext;
        q->pNext = p;
        if (l.pTail == q) {
            l.pTail = p;
        }
    } else {
        AddHead(l, p);
    }
}
```

## Hủy phần tử trong danh sách

Nguyên tắc: phải cô lập phần tử cần hủy trước khi hủy. Vì node được cấp phát bằng `new`, khi xóa cần giải phóng bằng `delete`.

Các vị trí cần hủy:

- Hủy phần tử đầu list.
- Hủy phần tử có khóa bằng `x`.
- Hủy phần tử đứng sau node `q`.

### Hủy phần tử đầu

```cpp
int RemoveHead(LIST &l, Data &x) {
    Node *p;
    if (l.pHead != NULL) {
        p = l.pHead;
        x = p->Info;
        l.pHead = l.pHead->pNext;
        delete p;
        if (l.pHead == NULL) {
            l.pTail = NULL;
        }
        return 1;
    }
    return 0;
}
```

### Hủy phần tử sau `q`

```cpp
int RemoveAfterQ(LIST &l, Node *q, Data &x) {
    Node *p;
    if (q != NULL) {
        p = q->pNext;
        if (p != NULL) {
            if (p == l.pTail) {
                l.pTail = q;
            }
            q->pNext = p->pNext;
            x = p->Info;
            delete p;
        }
        return 1;
    }
    return 0;
}
```

### Hủy phần tử có khóa `x`
Các bước:

1. Tìm phần tử `p` có khóa bằng `x`, đồng thời giữ node `q` đứng trước `p`.
2. Nếu `p != NULL`, hủy `p`:
   - Nếu `q != NULL`, hủy phần tử sau `q`.
   - Nếu `q == NULL`, phần tử cần xóa nằm đầu list, hủy đầu list.
3. Nếu không tìm thấy thì báo không tìm thấy.

```cpp
int RemoveX(LIST &l, Data x) {
    Node *p = l.pHead;
    Node *q = NULL;

    while ((p != NULL) && (p->Info != x)) {
        q = p;
        p = p->pNext;
    }

    if (p == NULL) {
        return 0;
    }

    if (q != NULL) {
        Data removed;
        RemoveAfterQ(l, q, removed);
    } else {
        Data removed;
        RemoveHead(l, removed);
    }
    return 1;
}
```

## Tìm kiếm trong danh sách liên kết đơn

Tìm tuần tự node có `Info == x`.

```cpp
Node* Search(LIST l, Data x) {
    Node *p = l.pHead;
    while ((p != NULL) && (p->Info != x)) {
        p = p->pNext;
    }
    return p;
}
```

Nếu tìm thấy, hàm trả về địa chỉ node. Nếu không tìm thấy, hàm trả về `NULL`.

## Duyệt danh sách

Duyệt danh sách là thao tác xử lý lần lượt các phần tử trong danh sách. Có thể dùng để:

- Đếm phần tử.
- Tìm tất cả phần tử thỏa điều kiện.
- Hủy toàn bộ danh sách.

```cpp
void PrintList(LIST l) {
    Node *p = l.pHead;
    while (p != NULL) {
        printf("%d ", p->Info);
        p = p->pNext;
    }
}
```

## Hủy toàn bộ danh sách

```cpp
void RemoveList(LIST &l) {
    Node *p;
    while (l.pHead != NULL) {
        p = l.pHead;
        l.pHead = p->pNext;
        delete p;
    }
    l.pTail = NULL;
}
```

## Sắp xếp danh sách

Slide nêu hai cách tiếp cận khi sắp xếp danh sách liên kết:

- Thay đổi thành phần `Info` giữa các node.
- Thay đổi liên kết giữa các node.

Cách thay đổi `Info` đơn giản hơn vì không phải cập nhật nhiều con trỏ, nhưng chỉ phù hợp khi dữ liệu có thể hoán đổi trực tiếp.

## Tóm tắt chương
- Danh sách liên kết đơn gồm các node, mỗi node có dữ liệu và con trỏ đến node kế tiếp.
- `pHead` trỏ node đầu, `pTail` trỏ node cuối.
- Thêm/xóa ở đầu danh sách có chi phí thấp.
- Khi xóa node cần cô lập node trước rồi giải phóng bằng `delete`.
- Duyệt danh sách thực hiện bằng cách đi theo `pNext`.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Node | Nút của danh sách liên kết |
| `Info` | Trường dữ liệu của node |
| `pNext` | Con trỏ đến node kế tiếp |
| `pHead` | Con trỏ đến node đầu danh sách |
| `pTail` | Con trỏ đến node cuối danh sách |
| `NULL` | Giá trị chỉ không có node kế tiếp |
| `new` | Cấp phát vùng nhớ động |
| `delete` | Giải phóng vùng nhớ động |

## Câu hỏi ôn tập
1. Node trong danh sách liên kết đơn gồm những thành phần nào?
2. `pHead` và `pTail` dùng để làm gì?
3. Trình bày thuật toán thêm node vào đầu danh sách.
4. Trình bày thuật toán thêm node vào cuối danh sách.
5. Khi xóa node sau `q`, cần cập nhật những liên kết nào?
6. Tìm kiếm trong danh sách liên kết đơn thực hiện như thế nào?
7. Vì sao cần dùng `delete` khi hủy node?
8. Có những cách nào để sắp xếp danh sách liên kết?
