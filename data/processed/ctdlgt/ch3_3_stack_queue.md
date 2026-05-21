# Chương 3.3: Stack và Queue

## Nội dung chính
- Khái niệm stack và cơ chế LIFO.
- Các thao tác trên stack: `Push`, `Pop`, `isEmpty`, `Top`.
- Cài đặt stack bằng mảng và danh sách liên kết.
- Ứng dụng của stack.
- Khái niệm queue và cơ chế FIFO.
- Các thao tác trên queue: `EnQueue`, `DeQueue`, `isEmpty`, `Front`.
- Cài đặt queue bằng mảng và danh sách liên kết.

## Tổng quan
Stack và queue là hai cấu trúc dữ liệu tuyến tính đặc biệt. Stack làm việc theo nguyên tắc vào sau ra trước, còn queue làm việc theo nguyên tắc vào trước ra trước. Hai cấu trúc này được dùng nhiều trong biên dịch, đệ quy, biểu thức, tìm kiếm đồ thị và quản lý tiến trình.

## Stack

Stack, hay ngăn xếp, là cấu trúc chứa các đối tượng làm việc theo cơ chế LIFO (Last In First Out). Phần tử được thêm sau sẽ được lấy ra trước.

### Các thao tác trên stack
| Thao tác | Ý nghĩa |
|---|---|
| `Push(o)` | Thêm đối tượng `o` vào stack |
| `Pop()` | Lấy một đối tượng ra khỏi stack |
| `isEmpty()` | Kiểm tra stack rỗng |
| `Top()` | Trả về phần tử đầu stack mà không hủy nó |

## Cài đặt stack bằng mảng

### Cấu trúc dữ liệu

```cpp
typedef struct tagStack {
    int a[max];
    int t;
} Stack;
```

Trong đó `t` là chỉ số phần tử đầu stack.

### Khởi tạo

```cpp
void CreateStack(Stack &s) {
    s.t = -1;
}
```

### Kiểm tra rỗng và đầy

```cpp
int IsEmpty(Stack s) {
    if (s.t == -1) {
        return 1;
    }
    return 0;
}

int IsFull(Stack s) {
    if (s.t >= max) {
        return 1;
    }
    return 0;
}
```

### Thêm phần tử

```cpp
int Push(Stack &s, int x) {
    if (IsFull(s) == 0) {
        s.t++;
        s.a[s.t] = x;
        return 1;
    }
    return 0;
}
```

### Lấy phần tử

```cpp
int Pop(Stack &s, int &x) {
    if (IsEmpty(s) == 0) {
        x = s.a[s.t];
        s.t--;
        return 1;
    }
    return 0;
}
```

### Nhận xét
Các thao tác trên stack có chi phí `O(1)`. Cài đặt bằng mảng đơn giản và hiệu quả, nhưng bị giới hạn bởi kích thước `N`. Nếu `N` quá nhỏ thì thiếu chỗ, nếu quá lớn thì lãng phí bộ nhớ.

## Cài đặt stack bằng danh sách liên kết

Khi cài đặt bằng danh sách liên kết, stack linh hoạt hơn về kích thước. Thêm và hủy cùng một phía, thường là đầu danh sách.

```cpp
int IsEmpty(List &s) {
    if (s.Head == NULL) {
        return 1;
    }
    return 0;
}
```

```cpp
void Push(List &s, Node *tam) {
    if (s.Head == NULL) {
        s.Head = tam;
        s.Tail = tam;
    } else {
        tam->Next = s.Head;
        s.Head = tam;
    }
}
```

```cpp
int Pop(List &s, int &trave) {
    Node *p;
    if (IsEmpty(s) != 1) {
        p = s.Head;
        trave = p->Info;
        s.Head = s.Head->Next;
        if (s.Head == NULL) {
            s.Tail = NULL;
        }
        delete p;
        return 1;
    }
    return 0;
}
```

## Ứng dụng của stack

Stack được dùng trong:

- Trình biên dịch và thông dịch để lưu môi trường của thủ tục.
- Khử đệ quy.
- Lưu vết trong quay lui, vét cạn.
- Lưu dữ liệu khi giải bài toán đồ thị như tìm đường đi.
- Chuyển đổi cơ số đếm.
- Soạn thảo văn bản.
- Định giá biểu thức số học.

### Chuyển biểu thức trung tố sang hậu tố
Stack có thể dùng để chuyển biểu thức trung tố có dấu ngoặc sang hậu tố.

Ví dụ:

```text
E  = ((a+b)*a-b)/c-a+(a+b)/(a-b)    // Trung tố
E1 = +-/-*+ababca/+ab-ab            // Tiền tố
E2 = ab+a*b-c/a-ab+ab-/             // Hậu tố
```

Quy tắc ưu tiên được nêu:

```text
pri($) < pri(() < pri(+) = pri(-) < pri(*) = pri(/)
```

### Định giá biểu thức hậu tố
Thuật toán:

1. Khởi tạo stack rỗng.
2. Đọc lần lượt từng thành phần của biểu thức hậu tố.
3. Nếu là toán hạng, đẩy vào stack.
4. Nếu là toán tử, lấy hai toán hạng ở đỉnh stack, thực hiện phép toán, rồi đẩy kết quả vào stack.
5. Lặp đến khi đọc hết biểu thức; kết quả nằm trong stack.

## Queue

Queue, hay hàng đợi, là cấu trúc chứa các đối tượng làm việc theo cơ chế FIFO (First In First Out). Phần tử vào trước sẽ được lấy ra trước.

### Các thao tác trên queue
| Thao tác | Ý nghĩa |
|---|---|
| `EnQueue(o)` | Thêm đối tượng `o` vào cuối hàng đợi |
| `DeQueue()` | Lấy đối tượng ở đầu hàng đợi |
| `isEmpty()` | Kiểm tra hàng đợi rỗng |
| `Front()` | Trả về phần tử đầu hàng đợi mà không hủy nó |

## Cài đặt queue bằng mảng

```cpp
typedef struct tagQueue {
    int a[100];
    int Front;
    int Rear;
} Queue;
```

```cpp
void CreateQueue(Queue &q) {
    q.Front = -1;
    q.Rear = -1;
}
```

### Lấy phần tử khỏi queue

```cpp
int DeQueue(Queue &q, int &x) {
    if (q.Front != -1) {
        x = q.a[q.Front];
        q.Front++;
        if (q.Front > q.Rear) {
            q.Front = -1;
            q.Rear = -1;
        }
        return 1;
    }
    printf("Queue rong");
    return 0;
}
```

### Thêm phần tử vào queue

```cpp
void EnQueue(Queue &q, int x) {
    int i, f, r;
    if (q.Rear - q.Front + 1 == N) {
        printf("queue day roi khong the them vao duoc nua");
    } else {
        if (q.Front == -1) {
            q.Front = 0;
            q.Rear = -1;
        }
        if (q.Rear == N - 1) {
            f = q.Front;
            r = q.Rear;
            for (i = f; i <= r; i++) {
                q.a[i - f] = q.a[i];
            }
            q.Front = 0;
            q.Rear = r - f;
        }
        q.Rear++;
        q.a[q.Rear] = x;
    }
}
```

## Cài đặt queue bằng danh sách liên kết

```cpp
int IsEmpty(List &Q) {
    if (Q.pHead == NULL) {
        return 1;
    }
    return 0;
}
```

```cpp
void EnQueue(List &Q, Node *tam) {
    if (Q.pHead == NULL) {
        Q.pHead = tam;
        Q.pTail = tam;
    } else {
        Q.pTail->Next = tam;
        Q.pTail = tam;
    }
}
```

```cpp
int DeQueue(List &Q, int &trave) {
    Node *p;
    if (IsEmpty(Q) != 1) {
        if (Q.pHead != NULL) {
            p = Q.pHead;
            trave = p->Info;
            Q.pHead = Q.pHead->Next;
            if (Q.pHead == NULL) {
                Q.pTail = NULL;
            }
            delete p;
            return 1;
        }
    }
    return 0;
}
```

## Ứng dụng của queue

Queue được dùng để:

- Lưu vết quá trình tìm kiếm theo chiều rộng.
- Tổ chức quản lý và phân phối tiến trình trong hệ điều hành.
- Tổ chức bộ đệm bàn phím: nhấn phím, đưa vào bộ đệm, CPU xử lý.

## Tóm tắt chương
- Stack làm việc theo cơ chế LIFO.
- Queue làm việc theo cơ chế FIFO.
- Stack và queue có thể cài đặt bằng mảng hoặc danh sách liên kết.
- Cài đặt bằng mảng đơn giản nhưng giới hạn kích thước.
- Cài đặt bằng danh sách liên kết linh hoạt hơn nhờ cấp phát động.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Stack | Ngăn xếp |
| LIFO | Vào sau ra trước |
| Push | Thêm phần tử vào stack |
| Pop | Lấy phần tử khỏi stack |
| Queue | Hàng đợi |
| FIFO | Vào trước ra trước |
| EnQueue | Thêm phần tử vào queue |
| DeQueue | Lấy phần tử khỏi queue |
| Front | Phần tử đầu queue |

## Câu hỏi ôn tập
1. Stack hoạt động theo cơ chế nào?
2. Queue hoạt động theo cơ chế nào?
3. Trình bày thao tác `Push` và `Pop`.
4. Cài đặt stack bằng mảng có hạn chế gì?
5. Stack được dùng trong những bài toán nào?
6. Trình bày thao tác `EnQueue` và `DeQueue`.
7. Vì sao BFS thường dùng queue?
8. So sánh cài đặt stack/queue bằng mảng và danh sách liên kết.
