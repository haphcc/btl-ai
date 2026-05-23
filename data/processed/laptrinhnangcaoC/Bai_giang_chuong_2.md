# Bai_giang_chuong_2



<!-- page 1 -->

HỌC VIỆN NGÂN HÀNG
KHOA HỆ THỐNG THÔNG TIN QUẢN LÝ

# CHƯƠNG II  DANH SÁCH LIÊN KẾT

LẬP TRÌNH NÂNG CAO

**Giảng viên**: Lê Văn Hùng
 0906238311
 hunglv@hvnh.edu.vn


<!-- page 2 -->

# 1. Khái niệm

Danh sách liên kết đơn là một tập hợp các Node được phân bố động, được sắp xếp theo cách sao cho mỗi Node chứa một giá trị (**Data**) và một con trỏ (**Next**). Con trỏ sẽ trỏ đến phần tử kế tiếp của danh sách liên kết đó. Nếu con trỏ mà trỏ tới **NULL**, nghĩa là đó là phần tử cuối cùng của **linked list**.

Mỗi Node trong danh sách liên kết đơn được chia thành hai thành phần chính đó là:

- **Phần data**: lưu trữ dữ liệu của node
- **Phần liên kết**: Lưu trữ địa chỉ của phần tử kế tiếp trong danh sách, hoặc lưu trữ giá trị NULL nếu là phần tử cuối cùng trong danh sách.

| Data | Next |
| :--- | :--- |
| 10 | pointer |


<!-- page 3 -->

# 1. Khái niệm

Danh sách liên kết đơn là một tập hợp các Node được phân bố động, được sắp xếp theo cách sao cho mỗi Node chứa một giá trị (**Data**) và một con trỏ (**Next**). Con trỏ sẽ trỏ đến phần tử kế tiếp của danh sách liên kết đó. Nếu con trỏ mà trỏ tới **NULL**, nghĩa là đó là phần tử cuối cùng của **linked list**.

![Sơ đồ danh sách liên kết](https://i.imgur.com/5y1y1y1.png)


<!-- page 4 -->

# 1. Khái niệm

- **Danh sách các kiểu danh sách liên kết:**
- **Danh sách liên kết đơn**(Single linked list): Chỉ có sự kết nối từ phần tử phía trước tới phần tử phía sau.
- **Danh sách liên kết đôi**(Double linked list): Có sự kết nối 2 chiều giữa phần tử phía trước với phần tử phía sau.
- **Danh sách liên kết vòng**(Circular Linked List): Có thêm sự kết nối giữa 2 phần tử đầu tiên và phần tử cuối cùng để tạo thành vòng khép kín.


<!-- page 5 -->

# 1. Khái niệm

| Nội dung | Mảng | Danh sách liên kết |
| :--- | :--- | :--- |
| **Kích thước** | - Kích thước cố định<br>- Cần chỉ rõ kích thước trong khi khai báo | - Kích thước thay đổi trong quá trình thêm/ xóa phần tử<br>- Kích thước tối đa phụ thuộc vào bộ nhớ |
| **Cấp phát bộ nhớ** | - Tĩnh: Bộ nhớ được cấp phát trong quá trình biên dịch | - Động: Bộ nhớ được cấp phát trong quá trình chạy |
| **Thứ tự & sắp xếp** | - Được lưu trữ trên một dãy ô nhớ liên tục | - Được lưu trữ trên các ô nhớ ngẫu nhiên |
| **Truy cập** | - Truy cập tới phần tử ngẫu nhiên trực tiếp bằng cách sử dụng chỉ số mảng: $O(1)$ | - Truy cập tới phần tử ngẫu nhiên cần phải duyệt từ đầu/cuối đến phần tử đó: $O(n)$ |


<!-- page 6 -->

# 2. Cài đặt danh sách liên kết

```c
struct LinkedList{
    int data;
    struct LinkedList *next;
};
```

Khai báo trên sẽ được sử dụng cho mọi Node trong linked list. Trường `data` sẽ lưu giữ giá trị và `next` sẽ là con trỏ để trỏ đến thẳng kế tiếp của nó.

**Tại sao next lại là kiểu LinkedList của chính nó?** Bởi vì nó là con trỏ trỏ của chính bản thân nó, và nó trỏ tới một thằng Node kế tiếp cũng có kiểu LinkedList.


<!-- page 7 -->

# Tạo mới một danh sách liên kết rỗng

```c
node InitHead(){
    node head;
    head = NULL;
    return head;
}
```


<!-- page 8 -->

# Tạo mới một danh sách liên kết

```c
typedef struct LinkedList *node; //Từ giờ dùng kiểu dữ liệu LinkedList có thể thay bằng node

node CreateNode(int value){
    node temp; // declare a node
    temp = (node)malloc(sizeof(struct LinkedList)); // Cấp phát vùng nhớ dùng malloc()
    temp->next = NULL;// Cho next trỏ tới NULL
    temp->data = value; // Gán giá trị cho Node
    return temp;//Trả về node mới đã có giá trị
}
```

**Lưu ý:** Không giống với mảng, cần khai báo `arr[size]`. Trong linked list, vì mỗi Node sẽ có con trỏ liên kết đến Node tiếp theo. Do đó, với danh sách liên kết đơn, bạn chỉ cần lưu giữ Node đầu tiên(HEAD). Có head rồi bạn có thể đi tới bất cứ Node nào.

- `malloc` là hàm cấp phát bộ nhớ của C. Với C++ chúng ta dùng `new`
- `sizeof` là hàm trả về kích thước của kiểu dữ liệu, dùng làm tham số cho hàm `malloc`


<!-- page 9 -->

# Thêm Node vào danh sách liên kết

## Thêm vào cuối danh sách:

- **Trường hợp 1:** Nếu danh sách liên kết đơn rỗng thì node mới được xem là node đầu tiên và cũng là node cuối cùng.
- **Trường hợp 2:** Nếu danh sách liên kết đơn không rỗng thì:
    - Cho con trỏ liên kết (next) của node cuối danh sách hiện tại trỏ đến đến node mới.
    - Cho con trỏ cuối của danh sách liên kết đơn (*tail) trỏ vào node mới.


<!-- page 10 -->

# Thêm Node vào danh sách liên kết

```cpp
node AddTail(node head, int value){
    node temp,p;// Khai báo 2 node tạm temp và p
    temp = CreateNode(value);//Gọi hàm createNode để khởi tạo node temp có next trỏ tới
    if(head == NULL){
        head = temp;        //Nếu linked list đang trống thì Node temp là head luôn
    }
    else{
        p = head;// Khởi tạo p trỏ tới head
        while(p->next != NULL){
            p = p->next;//Duyệt danh sách liên kết đến cuối. Node cuối là node có next
        }
        p->next = temp;//Gán next của thằng cuối = temp. Khi đó temp sẽ là thằng cuối(
    }
    return head;
}
```

10


<!-- page 11 -->

# Thêm vào vị trí đầu danh sách

Việc thêm vào đầu chính là việc cập nhật lại thằng **head**. Ta gọi Node mới (**temp**), ta có:
- Nếu **head** đang trỏ tới **NULL**, nghĩa là linked list đang trống, Node mới thêm vào sẽ làm **head** luôn.
- Ngược lại, ta phải thay thế thằng **head** cũ bằng **head** mới. Việc này phải làm theo thứ tự như sau:
    - Cho **next** của **temp** trỏ tới **head** hiện hành
    - Đặt **temp** làm **head** mới

```cpp
node AddHead(node head, int value){
    node temp = CreateNode(value); // Khởi tạo node temp với data = value
    if(head == NULL){
        head = temp; // //Nếu linked list đang trống thì Node temp là head luôn
    }else{
        temp->next = head; // Trỏ next của temp = head hiện tại
        head = temp; // Đổi head hiện tại = temp(Vì temp bây giờ là head mới mà)
    }
    return head;
}
```


<!-- page 12 -->

# Thêm vào vị trí bất kỳ

**Thêm vào vị trí bất kỳ**

*Thêm Node vào giữa danh sách liên kết*


<!-- page 13 -->

# MIS
MANAGEMENT INFORMATION SYSTEMS
BANKING ACADEMY OF VIETNAM

Để làm được điều này, giả sử ta có một node mới cần chèn vào danh sách liên kết đơn, ta gọi node đó là Node Q, khi đó ta cần thực hiện các bước sau:
- Cho node Q trỏ vào node đứng sau vị trí cần chèn.
- Cho Node đứng trước vị trí cần chèn trỏ vào Node Q.
Lưu ý: Chỉ thực hiện được khi danh sách đã có ít nhất một phần tử.

```cpp
node AddAt(node head, int value, int position){
    if(position == 0 || head == NULL){
        head = AddHead(head, value); // Nếu vị trí chèn là 0, tức là thêm vào đầu
    }else{
        // Bắt đầu tìm vị trí cần chèn. Ta sẽ dùng k để đếm cho vị trí
        int k = 1;
        node p = head;
        while(p != NULL && k != position){
            p = p->next;
            ++k;
        }

        if(k != position){
            // Nếu duyệt hết danh sách lk rồi mà vẫn chưa đến vị trí cần chèn, ta sẽ m
            // Nếu bạn không muốn chèn, hãy thông báo vị trí chèn không hợp lệ
            head = AddTail(head, value);
            // printf("Vi tri chen vuot qua vi tri cuoi cung!\n");
        }else{
            node temp = CreateNode(value);
            temp->next = p->next;
            p->next = temp;
        }
    }
    return head;
}
```

13


<!-- page 14 -->

# Xóa một nút khỏi danh sách_Xóa đầu

- **Xóa đầu đơn giản lắm, bây giờ chỉ cần cho thằng kế tiếp của head làm head là được thôi. Mà thằng kế tiếp của head chính là head->next.**

```c
0
1 node DelHead(node head){
2     if(head == NULL){
3         printf("\ncha co gi de xoa het!");
4     }else{
5         head = head->next;
6     }
7     return head;
8 }
9
```


<!-- page 15 -->

# Xóa một nút khỏi danh sách_Xóa cuối

- **Xóa cuối mới nhọc nè, nhọc ở chỗ phải duyệt đến thằng cuối – 1, cho next của cuối – 1 đó bằng NULL.**

```cpp
node DelTail(node head){
    if (head == NULL || head->next == NULL){
        return DelHead(head);
    }
    node p = head;
    while(p->next->next != NULL){
        p = p->next;
    }
    p->next = p->next->next; // Cho next bằng NULL
    // Hoặc viết p->next = NULL cũng được
    return head;
}
```


<!-- page 16 -->

# Xóa ở vị trí bất kỳ

Việc xóa ở vị trí bất kỳ cũng khá giống xóa ở cuối kia. Đơn giản là chúng ta bỏ qua một phần tử, như ảnh sau:

![Sơ đồ xóa phần tử C trong danh sách liên kết](https://i.imgur.com/5y1y15G.png)

- **Head**: Trỏ đến phần tử đầu tiên (A).
- **prev**: Trỏ đến phần tử đứng trước phần tử cần xóa (B).
- **tmp**: Trỏ đến phần tử cần xóa (C).
- Mũi tên đỏ gạch chéo thể hiện việc ngắt kết nối từ B đến C.
- Mũi tên đen nối từ B đến D thể hiện việc cập nhật lại liên kết để bỏ qua C.


<!-- page 17 -->

# Xóa ở vị trí bất kỳ

```c
node DelAt(node head, int position){
    if(position == 0 || head == NULL || head->next == NULL){
        head = DelHead(head); // Nếu vị trí chèn là 0, tức là thêm vào đầu
    }else{
        // Bắt đầu tìm vị trí cần chèn. Ta sẽ dùng k để đếm cho vị trí
        int k = 1;
        node p = head;
        while(p->next->next != NULL && k != position){
            p = p->next;
            ++k;
        }
        if(k != position){
            // Nếu duyệt hết danh sách lk rồi mà vẫn chưa đến vị trí cần chèn, ta sẽ n
            // Nếu bạn không muốn xóa, hãy thông báo vị trí xóa không hợp lệ
            head = DelTail(head);
            // printf("Vi tri xoa vuot qua vi tri cuoi cung!\n");
        }else{
            p->next = p->next->next;
        }
    }
    return head;
}
```


<!-- page 18 -->

# Lấy giá trị ở vị trí bất kỳ

- Chúng ta sẽ viết một hàm để truy xuất giá trị ở chỉ số bất kỳ nhé. Trong trường hợp chỉ số vượt quá chiều dài của linked list - 1, hàm này trả về vị trí cuối cùng. Do hạn chế là chúng ta không thể raise error khi chỉ số không hợp lệ. Tôi mặc định chỉ số bạn truyền vào phải là số nguyên không âm. Nếu bạn muốn kiểm tra chỉ số hợp lệ thì nên kiểm tra trước khi gọi hàm này.

```cpp
int Get(node head, int index){
    int k = 0;
    node p = head;
    while(p->next != NULL && k != index){
        ++k;
        p = p->next;
    }
    return p->data;
}
```


<!-- page 19 -->

# Tìm kiếm trong danh sách

Hàm tìm kiếm này sẽ trả về chỉ số của Node đầu tiên có giá trị bằng với giá trị cần tìm. Nếu không tìm thấy, chúng ta trả về -1.

```cpp
int Search(node head, int value){
    int position = 0;
    for(node p = head; p != NULL; p = p->next){
        if(p->data == value){
            return position;
        }
        ++position;
    }
    return -1;
}
```


<!-- page 20 -->

# Duyệt danh sách

Việc duyệt danh sách liên kết cực đơn giản. Khởi tạo từ Node head, bạn cứ thế đi theo con trỏ next cho tới trước khi Node đó NULL.

```c
void Traverser(node head){
    printf("\n");
    for(node p = head; p != NULL; p = p->next){
        printf("%5d", p->data);
    }
}
```


<!-- page 21 -->

# Hàm nhập danh sách liên kết

```c
node Input(){
    node head = InitHead();
    int n, value;
    do{
        printf("\nNhap so luong phan tu n = ");
        scanf("%d", &n);
    }while(n <= 0);

    for(int i = 0; i < n; ++i){
        printf("\nNhap gia tri can them: ");
        scanf("%d", &value);
        head = AddTail(head, value);
    }
    return head;
}
```


<!-- page 22 -->

# Hàm đếm số phần tử của danh sách

```cpp
int Length(node head){
    int length = 0;
    for(node p = head; p != NULL; p = p->next){
        ++length;
    }
    return length;
}
```