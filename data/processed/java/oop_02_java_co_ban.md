# Bài 2: Java cơ bản

## Nội dung chính
- Kiến trúc nền tảng Java và thư viện lớp chuẩn.
- Cấu trúc chương trình Java cơ bản.
- Cách biên dịch và chạy chương trình Java.
- Từ khóa, định danh, biến, hằng và kiểu dữ liệu.
- Mảng, ép kiểu và giá trị literal.
- Toán tử và thứ tự ưu tiên toán tử.
- Cấu trúc điều khiển cơ bản trong Java.

## Tổng quan
Bài này trình bày các thành phần nền tảng của Java. Người học cần hiểu chương trình Java được tổ chức trong lớp, cách viết phương thức `main`, cách khai báo biến, sử dụng kiểu dữ liệu, toán tử, mảng và các cấu trúc điều khiển.

## Kiến trúc Java

### Java Platform
Nền tảng Java gồm hai thành phần chính:

- Java Virtual Machine (JVM).
- Java API.

Chương trình Java được viết trong file `.java`, biên dịch thành file `.class` và chạy trong môi trường JVM trên từng hệ thống cụ thể.

### Thư viện lớp Java
JDK cung cấp nhiều gói thư viện chuẩn:

| Gói | Chức năng chính |
|---|---|
| `java.lang` | Các lớp cơ bản của ngôn ngữ |
| `java.applet` | Hỗ trợ applet |
| `java.awt` | Thành phần giao diện AWT |
| `java.io` | Vào/ra dữ liệu |
| `java.util` | Tiện ích, cấu trúc dữ liệu, lớp hỗ trợ |
| `java.net` | Lập trình mạng |
| `java.awt.event` | Xử lý sự kiện giao diện |
| `java.rmi` | Gọi phương thức từ xa |
| `java.security` | Bảo mật |
| `java.sql` | Kết nối cơ sở dữ liệu |

## Cấu trúc chương trình Java

### Quy trình phát triển
1. Viết mã nguồn trong file `.java`.
2. Biên dịch bằng `javac` để tạo file `.class`.
3. Chạy chương trình bằng lệnh `java`.

```bash
javac Hello.java
java Hello
```

### Ví dụ chương trình đầu tiên

**Ví dụ:**

```java
// Tên file: Hello.java
/* Tác giả: Barak Obama */
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```

**Giải thích:**
- Dòng bắt đầu bằng `//` là chú thích một dòng.
- Khối nằm giữa `/*` và `*/` là chú thích nhiều dòng.
- `public class Hello` khai báo lớp tên `Hello`.
- Tên lớp chứa `main` phải trùng với tên file `Hello.java`.
- Phương thức `main` là điểm bắt đầu thực thi chương trình.
- Lệnh `System.out.println()` in dữ liệu ra màn hình.

### Phương thức `main`

```java
public static void main(String[] args)
```

Ý nghĩa các thành phần:

| Thành phần | Ý nghĩa |
|---|---|
| `public` | Có thể được gọi từ bên ngoài lớp |
| `static` | Là phương thức thuộc lớp, có thể gọi mà không cần tạo đối tượng |
| `void` | Không trả về giá trị |
| `String[] args` | Tham số dòng lệnh truyền vào chương trình |

## Chú thích và khối lệnh

Java hỗ trợ ba dạng chú thích:

```java
/* Chú thích nhiều dòng */
// Chú thích một dòng
/** Chú thích tài liệu */
```

Các lệnh trong Java thường kết thúc bằng dấu chấm phẩy `;`. Các khối lệnh được đặt trong cặp dấu `{}`.

## Từ khóa trong Java

Một số nhóm từ khóa quan trọng:

| Nhóm | Từ khóa tiêu biểu |
|---|---|
| Kiểu dữ liệu nguyên thủy | `byte`, `short`, `int`, `long`, `float`, `double`, `char`, `boolean` |
| Vòng lặp | `do`, `while`, `for`, `break`, `continue` |
| Rẽ nhánh | `if`, `else`, `switch`, `case`, `default`, `break` |
| Phạm vi và tính chất phương thức | `private`, `public`, `protected`, `final`, `static`, `abstract`, `synchronized` |
| Giá trị đặc biệt | `true`, `false`, `null` |
| Phương thức | `return`, `void` |
| Gói | `package`, `import` |
| Xử lý lỗi | `try`, `catch`, `finally`, `throw`, `throws` |
| Đối tượng | `new`, `extends`, `implements`, `class`, `instanceof`, `this`, `super` |

## Định danh

Định danh dùng để đặt tên cho lớp, biến, phương thức và các thành phần khác trong chương trình.

Quy tắc đặt định danh:

- Có thể gồm chữ cái, chữ số, dấu gạch dưới `_` và ký hiệu `$`.
- Ký tự đầu tiên không được là chữ số.
- Java phân biệt chữ hoa và chữ thường.
- Không được trùng với từ khóa.

**Ví dụ:** `Hello`, `_prime`, `var8`, `tvLang`.

## Biến và phạm vi biến

### Khái niệm biến
Biến là vùng nhớ dùng để lưu trữ giá trị trong chương trình. Mỗi biến có tên, kiểu dữ liệu và giá trị.

### Khai báo biến

```java
int count;
int total = 10;
total = 20;
```

### Biến toàn cục và biến cục bộ
- Biến khai báo trong lớp có thể được sử dụng bởi các phương thức của lớp tùy theo phạm vi truy cập.
- Biến cục bộ được khai báo trong một khối lệnh và chỉ dùng được trong khối đó.

## Kiểu dữ liệu

### Nhóm kiểu dữ liệu
Java có hai nhóm kiểu dữ liệu:

- Kiểu nguyên thủy (primitive type).
- Kiểu tham chiếu (reference type).

### Kiểu nguyên thủy

| Nhóm | Kiểu |
|---|---|
| Số nguyên | `byte`, `short`, `int`, `long` |
| Số thực | `float`, `double` |
| Ký tự | `char` |
| Logic | `boolean` |

Kiểu `char` dùng mã Unicode. Kiểu `boolean` chỉ nhận hai giá trị `true` hoặc `false`.

### Kiểu tham chiếu
Kiểu tham chiếu trỏ đến đối tượng hoặc cấu trúc dữ liệu được tạo trong chương trình. Ví dụ:

- `String`.
- Các lớp bao như `Integer`, `Long`, `Double`, `Boolean`.
- Các lớp thư viện như `Font`.
- Các lớp do người lập trình tự định nghĩa.

### Ký tự đặc biệt

| Ký hiệu | Ý nghĩa |
|---|---|
| `\b` | Lùi một ký tự |
| `\t` | Tab |
| `\n` | Xuống dòng |
| `\r` | Về đầu dòng |
| `\"` | Dấu nháy kép |
| `\'` | Dấu nháy đơn |
| `\\` | Dấu gạch chéo ngược |
| `\f` | Sang trang |
| `\uxxxx` | Ký tự Unicode |

## Mảng

Mảng dùng để lưu nhiều phần tử cùng kiểu dữ liệu.

**Ví dụ:**

```java
int[] iarray;
iarray = new int[100];

int[] numbers = {1, 2, 3, 5, 6};
char[] letters = {'a', 'b', 'c'};

numbers[3] = 0;
letters[1] = 'z';

int length = numbers.length;
```

**Giải thích:**
- Chỉ số mảng bắt đầu từ `0`.
- Mảng cần được khởi tạo trước khi sử dụng.
- Thuộc tính `length` cho biết số phần tử của mảng.

Các khai báo như `int[5] iarray;` hoặc `int iarray[5];` không phải cú pháp khai báo mảng Java hợp lệ theo nội dung bài học.

## Ép kiểu

Ép kiểu cho phép chuyển giá trị từ kiểu này sang kiểu khác.

```java
float fNum = 20.25f;
int iCount = (int) fNum;
```

Chuyển kiểu mở rộng thường không làm mất thông tin. Chuyển kiểu thu hẹp có thể làm mất dữ liệu.

## Literal

Literal là giá trị được viết trực tiếp trong chương trình và không thay đổi.

```java
int a = 1;
long b = 1L;
float c = 1.5F;
double d = 2.0D;
char ch = 'A';
String text = "Hello";
```

Chuỗi ký tự đặt trong dấu nháy kép. Ký tự đơn đặt trong dấu nháy đơn.

## Toán tử

### Các nhóm toán tử

| Nhóm | Toán tử |
|---|---|
| Số học | `+`, `-`, `*`, `/`, `%`, `++`, `--` |
| So sánh | `==`, `!=`, `>`, `<`, `>=`, `<=` |
| Logic | `||`, `&&`, `!` |
| Gán | `=`, `+=`, `-=`, `*=`, `/=`, `%=` |
| Điều kiện | `condition ? expr1 : expr2` |

**Ví dụ:**

```java
int z = (x < y) ? 30 : 40;
```

**Giải thích:** Nếu `x < y` đúng thì `z` nhận giá trị `30`, ngược lại `z` nhận giá trị `40`.

### Thứ tự ưu tiên toán tử

| Mức ưu tiên | Toán tử |
|---|---|
| Cao | `.`, `[]`, `()` |
| | `++`, `--`, `!`, `~` |
| | `*`, `/`, `%` |
| | `+`, `-` |
| | `<<`, `>>`, `>>>` |
| | `<`, `>`, `<=`, `>=` |
| | `==`, `!=` |
| | `&`, `^`, `&&`, `||` |
| | `?:` |
| Thấp | `=` |

## Ví dụ biến và toán tử

**Ví dụ:**

```java
import java.lang.*;
import java.io.*;

class VariableDemo {
    static int x, y;

    public static void main(String[] args) {
        x = 10;
        y = 20;
        int z = x + y;

        System.out.println("x = " + x);
        System.out.println("y = " + y);
        System.out.println("z = x + y = " + z);
        System.out.println("So nho hon la so: " + Math.min(x, y));

        char c = 80;
        System.out.println("ky tu c la: " + c);
    }
}
```

**Giải thích:** Chương trình khai báo hai biến tĩnh `x`, `y`, tính tổng `z`, in kết quả và dùng `Math.min()` để tìm số nhỏ hơn.

## Cấu trúc điều khiển

### Rẽ nhánh
Java sử dụng `if`, `else` và `switch` để điều khiển luồng chương trình theo điều kiện.

```java
if (condition) {
    // Lệnh khi điều kiện đúng
} else {
    // Lệnh khi điều kiện sai
}
```

```java
switch (value) {
    case 1:
        break;
    default:
        break;
}
```

### Vòng lặp
Các vòng lặp cơ bản gồm `while`, `do while` và `for`.

```java
while (condition) {
    // Lặp khi điều kiện còn đúng
}
```

```java
do {
    // Thực hiện ít nhất một lần
} while (condition);
```

```java
for (int i = 0; i < 10; i++) {
    // Lệnh lặp
}
```

## Tóm tắt bài
- Chương trình Java được viết trong lớp và bắt đầu chạy từ phương thức `main`.
- File `.java` được biên dịch thành `.class`, sau đó chạy bằng lệnh `java`.
- Java có kiểu nguyên thủy và kiểu tham chiếu.
- Biến, định danh, toán tử, mảng và cấu trúc điều khiển là nền tảng để viết chương trình Java.
- Mọi câu lệnh cần được tổ chức rõ ràng trong khối lệnh và lớp.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| `main` | Phương thức bắt đầu thực thi chương trình Java |
| `javac` | Lệnh biên dịch mã nguồn Java |
| `java` | Lệnh chạy chương trình Java đã biên dịch |
| Định danh | Tên dùng cho lớp, biến, phương thức |
| Kiểu nguyên thủy | Kiểu dữ liệu cơ bản như `int`, `double`, `char`, `boolean` |
| Kiểu tham chiếu | Kiểu trỏ đến đối tượng hoặc dữ liệu phức tạp |
| Mảng | Cấu trúc lưu nhiều phần tử cùng kiểu |
| Ép kiểu | Chuyển giá trị từ kiểu dữ liệu này sang kiểu khác |

## Câu hỏi ôn tập
1. Trình bày cấu trúc cơ bản của một chương trình Java.
2. Vì sao tên lớp chứa `main` phải phù hợp với tên file nguồn?
3. Phân biệt kiểu nguyên thủy và kiểu tham chiếu.
4. Nêu quy tắc đặt định danh trong Java.
5. Mảng trong Java được khai báo và khởi tạo như thế nào?
6. Ép kiểu là gì? Khi nào có thể bị mất dữ liệu?
7. Java hỗ trợ những nhóm toán tử nào?
8. Phân biệt `while`, `do while` và `for`.
