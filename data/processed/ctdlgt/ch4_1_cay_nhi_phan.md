# Chương 4.1: Cây nhị phân

## Nội dung chính
- Các khái niệm cơ bản về cây: bậc, nút gốc, nút lá, mức và đường đi.
- Cấu trúc dữ liệu của cây nhị phân.
- Các phép duyệt cây nhị phân: NLR, LNR, LRN.
- Biểu diễn cây tổng quát bằng cây nhị phân.
- Biểu diễn cây nhị phân có liên kết cha.

## Tổng quan
Cây nhị phân là cấu trúc dữ liệu phân cấp trong đó mỗi nút có tối đa hai cây con: cây con trái và cây con phải. Chương này tập trung vào cách biểu diễn cây nhị phân và các phép duyệt cơ bản.

## Một số khái niệm

| Khái niệm | Giải thích |
|---|---|
| Bậc của một nút | Số cây con của nút đó |
| Bậc của cây | Bậc lớn nhất của các nút trong cây |
| Nút gốc | Nút không có nút cha |
| Nút lá | Nút có bậc bằng 0 |
| Mức của nút | Mức gốc bằng 0; mức cây con bằng mức cha cộng 1 |
| Độ dài đường đi | Số nhánh cần đi từ gốc đến nút cần xét |

## Cây nhị phân

Cây nhị phân là cây trong đó mỗi nút có tối đa hai cây con:

- Cây con trái.
- Cây con phải.

## Cấu trúc dữ liệu của cây nhị phân

```cpp
typedef struct tagTNode {
    Data Key;
    struct tagTNode *pLeft;
    struct tagTNode *pRight;
} TNode;

typedef TNode* TREE;
```

Mỗi node gồm dữ liệu `Key`, con trỏ đến cây con trái và con trỏ đến cây con phải.

## Duyệt cây nhị phân

Có ba trình tự thăm gốc:

- Duyệt trước.
- Duyệt giữa.
- Duyệt sau.

### Duyệt trước NLR
Duyệt trước thăm nút gốc trước, sau đó duyệt cây con trái rồi cây con phải.

Thứ tự: `Node - Left - Right`.

```cpp
void NLR(TREE root) {
    if (root != NULL) {
        // Xử lý root
        NLR(root->pLeft);
        NLR(root->pRight);
    }
}
```

**Ví dụ:** Với cây trong slide, kết quả duyệt trước được nêu là:

```text
A B D H I N E J O K C F L P G M
```

### Duyệt giữa LNR
Duyệt giữa thăm cây con trái trước, sau đó thăm nút gốc, cuối cùng thăm cây con phải.

Thứ tự: `Left - Node - Right`.

```cpp
void LNR(TREE root) {
    if (root != NULL) {
        LNR(root->pLeft);
        // Xử lý root
        LNR(root->pRight);
    }
}
```

**Ví dụ:** Với cây trong slide, kết quả duyệt giữa được nêu là:

```text
H D N I B J O E K A F P L C M G
```

### Duyệt sau LRN
Duyệt sau thăm cây con trái trước, sau đó cây con phải, cuối cùng mới thăm nút gốc.

Thứ tự: `Left - Right - Node`.

```cpp
void LRN(TREE root) {
    if (root != NULL) {
        LRN(root->pLeft);
        LRN(root->pRight);
        // Xử lý root
    }
}
```

**Ví dụ:** Với cây trong slide, kết quả duyệt sau được nêu là:

```text
N I D O J K E B P L F M G C A
```

## Ứng dụng duyệt sau

Duyệt sau có thể dùng để tính giá trị biểu thức dựa trên cây biểu thức.

**Ví dụ:** Slide nêu biểu thức:

```text
(3 + 1) * 3 / (9 - 5 + 2) - (3 * (7 - 4) + 6) = -13
```

## Biểu diễn cây tổng quát bằng cây nhị phân

Cây tổng quát có thể có số cây con thay đổi lớn, gây khó khăn và lãng phí khi biểu diễn. Vì vậy, nếu không cần thiết dùng cây tổng quát trực tiếp, có thể chuyển sang cây nhị phân.

Quy tắc chuyển:

1. Giữ nút con trái nhất làm nút con trái.
2. Các nút con còn lại chuyển thành các nút con phải.

Trong cây nhị phân mới:

- Con trái biểu diễn quan hệ cha - con trong cây tổng quát.
- Con phải biểu diễn quan hệ anh em trong cây tổng quát ban đầu.

## Biểu diễn cây nhị phân có liên kết cha

Đôi khi cần quan tâm quan hệ hai chiều cha - con. Khi đó node có thêm con trỏ `pParent`.

```cpp
typedef struct tagTNode {
    DataType Key;
    struct tagTNode *pParent;
    struct tagTNode *pLeft;
    struct tagTNode *pRight;
} TNODE;

typedef TNODE* TREE;
```

## Tóm tắt chương
- Cây nhị phân là cây mà mỗi nút có tối đa hai cây con.
- Node cây nhị phân thường gồm dữ liệu, con trỏ trái và con trỏ phải.
- Ba phép duyệt cơ bản là NLR, LNR và LRN.
- Cây tổng quát có thể được biểu diễn bằng cây nhị phân theo quy tắc con trái - anh em phải.
- Có thể bổ sung `pParent` nếu cần truy xuất ngược từ con về cha.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Cây nhị phân | Cây có tối đa hai cây con tại mỗi nút |
| Nút gốc | Nút không có cha |
| Nút lá | Nút không có cây con |
| Bậc | Số cây con của một nút |
| NLR | Duyệt trước: Node - Left - Right |
| LNR | Duyệt giữa: Left - Node - Right |
| LRN | Duyệt sau: Left - Right - Node |
| `pLeft` | Con trỏ đến cây con trái |
| `pRight` | Con trỏ đến cây con phải |

## Câu hỏi ôn tập
1. Cây nhị phân là gì?
2. Bậc của nút và bậc của cây được hiểu như thế nào?
3. Nút gốc và nút lá khác nhau ra sao?
4. Cấu trúc node của cây nhị phân gồm những thành phần nào?
5. Trình bày thứ tự duyệt NLR, LNR, LRN.
6. Vì sao có thể chuyển cây tổng quát thành cây nhị phân?
7. Con trỏ `pParent` dùng trong trường hợp nào?
