# Bài 3: Hướng đối tượng trong Java

## Nội dung chính
- Khái niệm lớp và đối tượng.
- Thuộc tính, phương thức và hàm tạo.
- Từ khóa `this` và toán tử `new`.
- Phạm vi truy cập: `public`, `private`, `protected`.
- Nạp chồng phương thức.
- Các đặc trưng hướng đối tượng: đóng gói, đa hình và kế thừa.

## Tổng quan
Lập trình hướng đối tượng tổ chức chương trình quanh các lớp và đối tượng. Trong Java, lớp mô tả dữ liệu và hành vi, còn đối tượng là thể hiện cụ thể được tạo ra từ lớp. Cách tiếp cận này giúp chương trình dễ mở rộng, dễ bảo trì và phù hợp với các bài toán có cấu trúc phức tạp.

## Lớp và đối tượng

### Khái niệm lớp
Lớp (class) là khuôn mẫu để tạo đối tượng. Một lớp thường gồm:

- Thuộc tính hoặc trường dữ liệu.
- Phương thức mô tả hành vi.
- Hàm tạo để khởi tạo đối tượng.

```java
class ClassName {
    <data_type> field1;
    <data_type> field2;

    // Constructor
    // Method declarations
}
```

### Khái niệm đối tượng
Đối tượng (object) là một thể hiện cụ thể của lớp. Khi một đối tượng được tạo ra từ lớp, đối tượng đó có dữ liệu riêng và có thể gọi các phương thức do lớp định nghĩa.

## Thuộc tính

Thuộc tính lưu trữ trạng thái của đối tượng. Trong Java, thuộc tính thường được khai báo kèm phạm vi truy cập.

```java
class ClassName {
    <modifier> <data_type> field1;
}
```

Các phạm vi truy cập thường dùng:

| Phạm vi | Ý nghĩa |
|---|---|
| `public` | Có thể truy cập từ bên ngoài lớp |
| `private` | Chỉ truy cập được bên trong lớp |
| `protected` | Truy cập được trong lớp và lớp kế thừa |

**Ví dụ:**

```java
public class XeMay {
    public String nhasx;
    public String model;
    private float chiphisx;
    protected int thoigiansx;
    protected int so;
    public static int sobanhxe = 2;
}
```

**Giải thích:** Các thuộc tính `nhasx` và `model` có thể truy cập công khai. Thuộc tính `chiphisx` được che giấu bên trong lớp. Thuộc tính `sobanhxe` là biến tĩnh dùng chung ở mức lớp.

## Phương thức

Phương thức là khối lệnh thực hiện một hành vi của lớp hoặc xử lý dữ liệu của đối tượng.

```java
<modifier> <return_type> <method_name>(<parameters>) {
    <statements>;
}
```

Một số từ khóa có thể dùng với phương thức:

| Từ khóa | Ý nghĩa |
|---|---|
| `public` | Cho phép gọi từ bên ngoài lớp |
| `protected` | Cho phép gọi trong lớp và lớp kế thừa |
| `private` | Chỉ gọi được trong lớp |
| `static` | Phương thức thuộc lớp, không cần tạo đối tượng |
| `final` | Không cho lớp con ghi đè |
| `abstract` | Chỉ khai báo, lớp con phải cài đặt |
| `synchronized` | Hỗ trợ đồng bộ trong môi trường đa luồng |

**Ví dụ:**

```java
public class XeMay {
    private float chiphisx;

    public float tinhgiaban() {
        return 1.5f * chiphisx;
    }
}
```

**Giải thích:** Phương thức `tinhgiaban()` sử dụng chi phí sản xuất để tính giá bán.

## Hàm tạo

### Khái niệm
Hàm tạo (constructor) là phương thức đặc biệt được gọi tự động khi tạo đối tượng. Hàm tạo có cùng tên với lớp và không có kiểu trả về.

Nếu lớp không khai báo hàm tạo, Java cung cấp một hàm tạo mặc định. Tuy nhiên, nên tự khai báo hàm tạo khi cần kiểm soát giá trị khởi tạo của đối tượng.

### Ví dụ hàm tạo

```java
public class XeMay {
    public String nhasx;
    public String model;
    private float chiphisx;
    protected int thoigiansx;
    protected int so;

    public XeMay() {
    }

    public XeMay(String sNhasx, String sModel,
                 float fChiphisx, int iThoigiansx, int iSo) {
        this.nhasx = sNhasx;
        this.model = sModel;
        this.chiphisx = fChiphisx;
        this.thoigiansx = iThoigiansx;
        this.so = iSo;
    }
}
```

**Giải thích:** Hàm tạo thứ nhất không có tham số. Hàm tạo thứ hai nhận tham số và gán giá trị cho các thuộc tính của đối tượng.

## Từ khóa `this`

`this` là biến ẩn có trong mọi lớp Java. Nó tham chiếu đến đối tượng hiện tại đang thực thi phương thức hoặc hàm tạo.

```java
public A(int par1, String par2) {
    this.field1 = par1;
    this.field2 = par2;
}
```

`this` thường được dùng khi tên tham số trùng với tên thuộc tính hoặc khi cần gọi phương thức của chính đối tượng hiện tại.

```java
this.method1();
```

## Tạo đối tượng bằng `new`

Đối tượng được tạo bằng toán tử `new`. Khi gọi `new`, Java cấp phát bộ nhớ và gọi hàm tạo tương ứng.

```java
XeMay xe = new XeMay("Honda", "Wave", 1000.0f, 2025, 1);
```

## Nạp chồng phương thức

Nạp chồng phương thức (method overloading) cho phép nhiều phương thức trong cùng một lớp có cùng tên nhưng khác danh sách tham số.

**Ví dụ:**

```java
public class XeMay {
    private float chiphisx;

    public float tinhgiaban() {
        return 2 * chiphisx;
    }

    public float tinhgiaban(float huehong) {
        return 2 * chiphisx + huehong;
    }
}
```

**Giải thích:** Hai phương thức cùng tên `tinhgiaban`, nhưng một phương thức không có tham số và một phương thức có tham số `huehong`.

## Các đặc trưng hướng đối tượng

### Đóng gói
Đóng gói (encapsulation) là việc che giấu dữ liệu và chi tiết cài đặt bên trong lớp, chỉ cung cấp các phương thức cần thiết để bên ngoài tương tác với đối tượng.

Trong Java, lớp là đơn vị đóng gói cơ bản. Dữ liệu được biểu diễn bằng thuộc tính, còn hành vi được biểu diễn bằng phương thức.

### Đa hình
Đa hình (polymorphism) cho phép cùng một lời gọi phương thức có thể dẫn đến các cách thực hiện khác nhau tùy theo đối tượng cụ thể.

**Ví dụ:**

```java
class AObject {
    public void show() {
        System.out.println("AObject");
    }
}

class BObject extends AObject {
    public void show() {
        System.out.println("BObject");
    }
}

public class Demo {
    public static void main(String[] args) {
        AObject[] arrObject = new AObject[2];
        arrObject[0] = new AObject();
        arrObject[1] = new BObject();

        arrObject[0].show();
        arrObject[1].show();
    }
}
```

**Giải thích:** Biến kiểu lớp cha có thể tham chiếu đến đối tượng lớp con. Khi gọi `show()`, phiên bản phương thức phù hợp với đối tượng thực tế sẽ được thực thi.

### Kế thừa
Kế thừa (inheritance) cho phép xây dựng lớp mới từ lớp đã có. Lớp mới kế thừa thuộc tính và phương thức của lớp cũ, đồng thời có thể bổ sung hoặc thay đổi hành vi.

```java
class A extends B {
    // A kế thừa từ B
}
```

Trong quan hệ này, `B` là lớp cha hoặc lớp cơ sở, còn `A` là lớp con.

## Tóm tắt bài
- Lớp là khuôn mẫu, đối tượng là thể hiện cụ thể của lớp.
- Thuộc tính mô tả trạng thái, phương thức mô tả hành vi.
- Hàm tạo được gọi khi tạo đối tượng bằng `new`.
- `this` tham chiếu đến đối tượng hiện tại.
- Lập trình hướng đối tượng trong Java dựa trên đóng gói, đa hình và kế thừa.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| `class` | Khuôn mẫu tạo đối tượng |
| `object` | Thể hiện cụ thể của lớp |
| `field` | Thuộc tính hoặc dữ liệu của lớp |
| `method` | Hành vi hoặc thao tác của lớp |
| `constructor` | Hàm tạo dùng để khởi tạo đối tượng |
| `this` | Tham chiếu đến đối tượng hiện tại |
| `overloading` | Nạp chồng phương thức cùng tên nhưng khác tham số |
| `encapsulation` | Đóng gói dữ liệu và hành vi trong lớp |
| `polymorphism` | Đa hình, một lời gọi có thể có nhiều cách thực hiện |
| `inheritance` | Kế thừa từ lớp đã có |

## Câu hỏi ôn tập
1. Lớp và đối tượng khác nhau như thế nào?
2. Thuộc tính và phương thức có vai trò gì trong một lớp?
3. Hàm tạo có đặc điểm gì khác phương thức thông thường?
4. Khi nào cần sử dụng từ khóa `this`?
5. Phân biệt `public`, `private` và `protected`.
6. Nạp chồng phương thức là gì?
7. Trình bày ý nghĩa của đóng gói, đa hình và kế thừa.
