# Chương 4: Kế thừa

## Nội dung chính
- Kế thừa đơn trong C++.
- Lớp cơ sở và lớp dẫn xuất.
- Thành viên `protected`.
- Ép kiểu con trỏ giữa lớp cơ sở và lớp dẫn xuất.
- Các kiểu kế thừa `public`, `protected`, `private`.
- Constructor, destructor trong lớp dẫn xuất.
- Đa kế thừa và lớp cơ sở ảo.

## Tổng quan
Kế thừa (inheritance) là cơ chế cho phép một lớp mới tái sử dụng thuộc tính và phương thức của lớp đã có. Cơ chế này giúp giảm trùng lặp mã, mở rộng hệ thống và mô hình hóa quan hệ `is-a` giữa các lớp.

## 4.1. Kế thừa đơn

Kế thừa là cơ chế cho phép một lớp mới (derived class) tái sử dụng thuộc tính và phương thức của lớp khác (base class).

Kế thừa đơn (single inheritance) là trường hợp một lớp dẫn xuất chỉ kế thừa từ một lớp cơ sở duy nhất. Nhờ đó, lớp con có thể sử dụng lại phương thức và thuộc tính của lớp cha, đồng thời bổ sung chức năng riêng.

**Ví dụ:** Quan hệ `Dog is an Animal` là quan hệ `is-a`: `Dog` là một loại `Animal`.

```cpp
class Animal {
public:
    void eat();
};

class Dog : public Animal {
public:
    void bark();
};
```

## 4.2. Base class và Derived class

| Thành phần | Ý nghĩa |
|---|---|
| Base class | Lớp gốc, chứa thành phần chung |
| Derived class | Lớp kế thừa, mở rộng chức năng |

Ưu điểm của kế thừa:

- Giảm trùng lặp code.
- Dễ bảo trì.
- Dễ mở rộng hệ thống.

Trong kế thừa, lớp cơ sở đóng vai trò nền tảng, chứa dữ liệu và hành vi chung. Lớp dẫn xuất được xây dựng dựa trên lớp cơ sở, có thể kế thừa toàn bộ hoặc một phần và bổ sung hành vi riêng.

## 4.3. Thành viên `protected`

Trong C++, mỗi thành viên của lớp có thể khai báo với một trong ba mức truy cập:

| Mức truy cập | Ý nghĩa |
|---|---|
| `public` | Truy cập ở mọi nơi |
| `private` | Chỉ truy cập trong lớp hiện tại |
| `protected` | Dùng được trong base class và derived class |

`protected` được dùng khi muốn ẩn thông tin với bên ngoài nhưng vẫn cho phép lớp con kế thừa và sử dụng.

## 4.4. Ép kiểu con trỏ

Khi sử dụng con trỏ giữa lớp cơ sở và lớp dẫn xuất, có thể thực hiện ép kiểu. Việc này cần cẩn thận để tránh lỗi runtime.

| Kiểu ép | Mô tả |
|---|---|
| Upcasting | Chuyển `Derived*` sang `Base*`, an toàn và thường tự động |
| Downcasting | Chuyển `Base*` sang `Derived*`, cần ép kiểu và có thể nguy hiểm nếu không kiểm soát |

```cpp
Derived *d = new Derived();
Base *b = d;        // Upcasting
Derived *d2 = (Derived*) b; // Downcasting, cần cẩn thận
```

## 4.5. Kế thừa `public`, `protected`, `private`

Khi một lớp kế thừa từ lớp khác, có thể chỉ định cách kế thừa. Kiểu kế thừa quyết định mức độ hiển thị của các thành viên từ lớp cơ sở khi sang lớp dẫn xuất.

| Kiểu kế thừa | Thành viên `public` của Base | Thành viên `protected` của Base |
|---|---|---|
| `public` | Trở thành `public` trong Derived | Trở thành `protected` trong Derived |
| `protected` | Trở thành `protected` trong Derived | Trở thành `protected` trong Derived |
| `private` | Trở thành `private` trong Derived | Trở thành `private` trong Derived |

Kế thừa `public` là kiểu thường dùng nhất khi mô hình hóa quan hệ `is-a`.

## 4.6. Constructor và Destructor trong lớp dẫn xuất

Khi tạo đối tượng từ lớp dẫn xuất, chương trình tự động gọi constructor của lớp cơ sở trước để khởi tạo phần chung, sau đó mới gọi constructor của lớp dẫn xuất.

Khi hủy đối tượng, thứ tự diễn ra ngược lại:

- Thứ tự tạo: `Base -> Derived`.
- Thứ tự hủy: `Derived -> Base`.

Thứ tự này giúp quản lý tài nguyên đúng cách.

```cpp
class Base {
public:
    Base() {}
    ~Base() {}
};

class Derived : public Base {
public:
    Derived() {}
    ~Derived() {}
};
```

## 4.7. Đa kế thừa

Đa kế thừa (multiple inheritance) cho phép một lớp kế thừa từ nhiều lớp cơ sở, nhờ đó kết hợp nhiều đặc tính.

Ưu điểm:

- Linh hoạt.
- Kết hợp nhiều tính năng.

Nhược điểm:

- Phức tạp.
- Dễ trùng lặp.
- Có thể phát sinh diamond problem.

Giải pháp được nêu trong slide là dùng virtual inheritance.

```cpp
class A {};
class B {};

class C : public A, public B {};
```

## 4.8. Lớp cơ sở ảo

Trong đa kế thừa, nếu nhiều lớp dẫn xuất cùng kế thừa từ một lớp cơ sở chung, lớp cháu có thể thừa hưởng nhiều bản sao của lớp cơ sở, gây trùng lặp dữ liệu và mơ hồ. Đây là diamond problem.

Để tránh vấn đề này, khai báo lớp cơ sở với từ khóa `virtual` khi kế thừa. Khi đó lớp cháu chỉ có một bản duy nhất của lớp cơ sở chung.

```cpp
class Animal {
public:
    int age;
};

class Mammal : virtual public Animal {};
class Bird : virtual public Animal {};
class Bat : public Mammal, public Bird {};
```

**Ví dụ:** `Mammal` kế thừa từ `Animal`, `Bird` cũng kế thừa từ `Animal`, `Bat` kế thừa từ cả `Mammal` và `Bird`. Nếu không dùng `virtual`, `Bat` có hai bản sao của `Animal`. Nếu dùng `virtual`, `Bat` chỉ có một bản sao `Animal`.

## Tóm tắt chương
- Kế thừa giúp tái sử dụng và mở rộng lớp.
- Kế thừa đơn có một lớp cơ sở và một lớp dẫn xuất.
- `protected` cho phép lớp con truy cập thành viên nhưng vẫn ẩn với bên ngoài.
- Kiểu kế thừa ảnh hưởng đến mức truy cập của thành viên lớp cơ sở trong lớp dẫn xuất.
- Constructor được gọi theo thứ tự `Base -> Derived`, destructor theo `Derived -> Base`.
- Đa kế thừa mạnh nhưng cần cẩn trọng; lớp cơ sở ảo giúp giải quyết diamond problem.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Inheritance | Kế thừa, tái sử dụng thuộc tính và phương thức của lớp khác |
| Base class | Lớp cơ sở hoặc lớp cha |
| Derived class | Lớp dẫn xuất hoặc lớp con |
| Single inheritance | Kế thừa đơn |
| Multiple inheritance | Đa kế thừa |
| `protected` | Phạm vi truy cập cho lớp hiện tại và lớp dẫn xuất |
| Upcasting | Ép con trỏ lớp dẫn xuất lên lớp cơ sở |
| Downcasting | Ép con trỏ lớp cơ sở xuống lớp dẫn xuất |
| Virtual base class | Lớp cơ sở ảo |
| Diamond problem | Vấn đề mơ hồ do nhiều bản sao lớp cơ sở trong đa kế thừa |

## Câu hỏi ôn tập
1. Kế thừa là gì?
2. Phân biệt base class và derived class.
3. Kế thừa đơn khác đa kế thừa như thế nào?
4. Thành viên `protected` dùng trong trường hợp nào?
5. Upcasting và downcasting khác nhau ra sao?
6. Kiểu kế thừa `public`, `protected`, `private` ảnh hưởng đến thành viên lớp cơ sở như thế nào?
7. Thứ tự gọi constructor và destructor trong kế thừa là gì?
8. Diamond problem là gì và lớp cơ sở ảo giải quyết vấn đề này như thế nào?
